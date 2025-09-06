import functools

from flask import (
    Blueprint, g, redirect, request, session, Response
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import abort

from flask_cors import cross_origin

import requests
import os

cors_required_headers = [
    ('Access-Control-Allow-Origin', '*'),
    ('Access-Control-Allow-Methods', '*'),
    ('Access-Control-Allow-Headers', 'Content-Type')
]

bp = Blueprint('auth', __name__, url_prefix="/auth")

def username_is_duplicate(username: str) -> bool:
    """
    Examines the array of accounts in the database to check if the passed username is a duplicate.

    Parameters:
        username: The username in question
    
    Returns:
        True if username is a duplicate, False otherwise
    """
    assert isinstance(username, str), 'username is not a string'
    ACCOUNTS_ENDPOINT: str | None = os.getenv('ACCOUNTS_ENDPOINT')
    assert ACCOUNTS_ENDPOINT, "ACCOUNTS_ENDPOINT cannot be located in .env"
    if not ACCOUNTS_ENDPOINT:
        print('Unknown registration endpoint.')
        abort(404, 'Unknown registration endpoint.')
    response = requests.get(ACCOUNTS_ENDPOINT)
    if not response:
        print('The registration fails to process.')
        abort(404, 'The registration fails to process.')
    accounts = response.json()
    duplicate_exists: bool = any(account['username'] == username for account in accounts)
    return duplicate_exists

@cross_origin # Enables CORS
@bp.route('duplicatecheck/register/<username>', methods=['GET'])
def duplicate_check_register_link(username: str):
    print(username)
    if request.method == 'GET':
        if (username_is_duplicate(username)):
            return Response(status=403, headers=cors_required_headers, response='The username has already been picked.')
        return Response(status=200, headers=cors_required_headers, response="The username has not been picked.")
    return Response(status=403, headers=cors_required_headers, response='Inaccessible')

@cross_origin # Enables CORS
@bp.route('duplicatecheck/login/<username>', methods=['GET'])
def duplicate_check_login_link(username: str):
    print(username)
    if request.method == 'GET':
        if (username_is_duplicate(username)):
            return Response(status=200, headers=cors_required_headers, response='The username has already been picked.')
        return Response(status=403, headers=cors_required_headers, response="The username has not been picked.")
    return Response(status=403, headers=cors_required_headers, response='Inaccessible')

@cross_origin # Enables CORS
@bp.route('register', methods=['POST'])
def register():
    if request.method == 'POST':
        # origin = request.environ.get('HTTP_ORIGIN')
        request_json = request.json # gets the body data

        # Preventing duplicate usernames
        username = request_json['username']
        if (username_is_duplicate(username)):
            return Response(status=403, headers=cors_required_headers, response='The username has already been picked.')

        # Replace password with password hash
        request_json['password'] = generate_password_hash(request_json['password'])
        
        # Send the edited json to the JSON server
        accounts_endpoint: str | None = os.getenv('ACCOUNTS_ENDPOINT')
        if not accounts_endpoint:
            return Response(status=404, headers=cors_required_headers, response='Unknown registration endpoint.')
        accounts_response = requests.post(accounts_endpoint, json=request_json)
        if not accounts_response:
            return Response(status=404, headers=cors_required_headers, response='The registration fails to process.')
        
        # The response returns a JSON object
        # Get the user ID from the response JSON to add an entry to user_answers in db.json
        response_json = accounts_response.json()
        
        USER_ID = response_json['id']

        # Add an entry to user_answers in db.json
        submissions_endpoint: str | None = os.getenv('SUBMISSIONS_ENDPOINT')
        if not submissions_endpoint:
            return Response(status=404, headers=cors_required_headers, response='The registration fails to process.')
        requests.post(submissions_endpoint, json = {'id': USER_ID})
        return Response(status=200, headers=cors_required_headers)
    return Response(status=403, headers=cors_required_headers, response='Inaccessible')

@cross_origin # Enables CORS
@bp.route('login', methods=['POST'])
def login():
    if request.method == 'POST':
        # origin = request.environ.get('HTTP_ORIGIN')
        request_json = request.json # gets the body data
        USERNAME = request_json['username']
        PASSWORD = request_json['password']
        
        # Get a set of accounts
        ACCOUNTS_ENDPOINT: str | None = os.getenv('ACCOUNTS_ENDPOINT')
        assert ACCOUNTS_ENDPOINT, "ACCOUNTS_ENDPOINT cannot be located in .env"
        if not ACCOUNTS_ENDPOINT:
            return Response(status=404, headers=cors_required_headers, response='Unknown registration endpoint.')
        response = requests.get(ACCOUNTS_ENDPOINT)
        if not response:
            return Response(status=404, headers=cors_required_headers, response='The registration fails to process.')
        accounts = response.json()

        # Get the user's JSON object
        error = None
        user_found = next(filter(lambda user: user['username'] == USERNAME, accounts), None)
        if not user_found:
            error = 'This user does not exist.'
        
        elif not check_password_hash(user_found['password'], PASSWORD): # Verify if passwords match
            error = 'Invalid password.'
        
        if error is None:
            session.clear()
            session['username'] = user_found['username']
            session['user_id'] = user_found['id']

            # Verify if this user has a corresponding user_answers entry. If not, create one.
            USER_ID = user_found['id']

            submissions_endpoint: str | None = os.getenv('SUBMISSIONS_ENDPOINT')
            if not submissions_endpoint:
                return Response(status=404, headers=cors_required_headers, response='The registration fails to process.')
            
            # Verify if there is a corresponding user_answers entry
            all_user_answers_entries = requests.get(submissions_endpoint)
            if not all_user_answers_entries:
                return Response(status=404, headers=cors_required_headers, response='The registration fails to process.')
            all_user_answers_entries = all_user_answers_entries.json()
            entry_exists = any(entry['id'] == USER_ID for entry in all_user_answers_entries)

            # Create an entry if one does not exist
            if not entry_exists:
                requests.post(submissions_endpoint, json = {'id': USER_ID})

            # Determining the visibility of certain features will be done when loading the index page
            return Response(status=200, headers=cors_required_headers, response=f'The user ID is: {USER_ID}')
        else:
            return Response(status=403, headers=cors_required_headers, response=error)
    
    return Response(status=403, headers=cors_required_headers, response='Inaccessible')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        # Get a set of accounts
        ACCOUNTS_ENDPOINT: str | None = os.getenv('ACCOUNTS_ENDPOINT')
        assert ACCOUNTS_ENDPOINT, "ACCOUNTS_ENDPOINT cannot be located in .env"
        if not ACCOUNTS_ENDPOINT:
            return Response(status=404, headers=cors_required_headers, response='Unknown registration endpoint.')
        response = requests.get(ACCOUNTS_ENDPOINT)
        if not response:
            return Response(status=404, headers=cors_required_headers, response='The registration fails to process.')
        accounts = response.json()

        # Get the user's JSON object
        error = None
        user_found = next(filter(lambda user: user['id'] == user_id, accounts), None)
        if user_found:
            g.user = user_found.username

@cross_origin # Enables CORS
@bp.route('/logout', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        # Redirect to the LOGIN page
        return Response(status=200, headers=cors_required_headers, response='The user has logged out.')
    return Response(status=403, headers=cors_required_headers, response='Inaccessible.')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            print(f'Unable to proceed to {view.__name__} view function as login is required.')
            return redirect(os.getenv('LOGIN_REQUIRED_ENDPOINT'))

        return view(**kwargs)

    return wrapped_view