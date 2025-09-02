import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import abort

import requests
import os

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
        abort(404, 'Unknown registration endpoint.')
    response = requests.get(ACCOUNTS_ENDPOINT)
    if not response:
        abort(404, 'The registration fails to process.')
    accounts = set(response.json())
    duplicate_exists: bool = any(account['username'] == username for account in accounts)
    return duplicate_exists

@bp.route('register', methods=['POST'])
def register():
    if request.method == 'POST':
        # origin = request.environ.get('HTTP_ORIGIN')
        request_json = request.json # gets the body data

        # Preventing duplicate usernames
        username = request_json['username']
        if (username_is_duplicate(username)):
            abort(403, 'The username has already been picked.')

        # Replace password with password hash
        request_json['password'] = generate_password_hash(request_json['password'])
        
        # Send the edited json to the JSON server
        accounts_endpoint: str | None = os.getenv('ACCOUNTS_ENDPOINT')
        if not accounts_endpoint:
            abort(404, 'Unknown registration endpoint.')
        accounts_response = requests.post(accounts_endpoint, json=request_json)
        if not accounts_response:
            abort(404, 'The registration fails to process.')
        
        # The response returns a JSON object
        # Get the user ID from the response JSON to add an entry to user_answers in db.json
        response_json = accounts_response.json()
        
        USER_ID = response_json['id']

        # Add an entry to user_answers in db.json
        submissions_endpoint: str | None = os.getenv('SUBMISSIONS_ENDPOINT')
        if not submissions_endpoint:
            abort(404, 'The registration fails to process.')
        requests.post(submissions_endpoint, json = {'id': USER_ID})
        
    # Redirect to the LOGIN page
    return redirect(url_for('auth.login'))

@bp.route('login', methods=['POST'])
def login():
    if request.method == 'POST':
        # origin = request.environ.get('HTTP_ORIGIN')
        request_json = request.json() # gets the body data
        print(request_json)
        USERNAME = request_json['username']
        PASSWORD = request_json['password']
        
        # Get a set of accounts
        ACCOUNTS_ENDPOINT: str | None = os.getenv('ACCOUNTS_ENDPOINT')
        assert ACCOUNTS_ENDPOINT, "ACCOUNTS_ENDPOINT cannot be located in .env"
        if not ACCOUNTS_ENDPOINT:
            abort(404, 'Unknown registration endpoint.')
        response = requests.get(ACCOUNTS_ENDPOINT)
        if not response:
            abort(404, 'The registration fails to process.')
        accounts = response.json()

        # Get the user's JSON object
        error = None
        user_found = next(filter(lambda user: user['username'] == USERNAME, accounts), None)
        if not user_found:
            error = 'This user does not exist.'
        
        elif not check_password_hash(user_found.password, PASSWORD): # Verify if passwords match
            error = 'Invalid password.'
        
        if error is None:
            session.clear()
            session['username'] = user_found.username
            session['user_id'] = user_found.id

            # Determining the visibility of certain features will be done when loading the index page
            return redirect(url_for('index'))
    
    # Redirect to the LOGIN page
    return redirect(url_for('auth.login'))

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
            abort(404, 'Unknown registration endpoint.')
        response = requests.get(ACCOUNTS_ENDPOINT)
        if not response:
            abort(404, 'The registration fails to process.')
        accounts = response.json()

        # Get the user's JSON object
        error = None
        user_found = next(filter(lambda user: user['id'] == user_id, accounts), None)
        if user_found:
            g.user = user_found.username

@bp.route('/logout')
def logout():
    session.clear()
    
    # Redirect to the LOGIN page
    return redirect(url_for('auth.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('authjson.login'))

        return view(**kwargs)

    return wrapped_view