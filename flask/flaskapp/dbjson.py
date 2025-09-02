import click
import requests
import os

def get_all_items_in_endpoint(env_endpoint: str = '') -> dict | None:
    """
    Get all items in the passed endpoint in the JSON database.

    Parameters:
        env_endpoint (str): An endpoint found in the local .env file
    
    Returns:
        A dictionary of items or None
    """
    assert isinstance(env_endpoint, str), 'endpoint is not a string'
    response = requests.get(os.getenv(env_endpoint))
    if response.json():
        returned_dict: dict = {}
        for item in response.json():
            returned_dict[item['id']] = item
        return returned_dict
    pass

@click.command('db-resetall')
def reset_all_db():
    account_dict = get_all_items_in_endpoint('ACCOUNTS_ENDPOINT')
    answers_dict = get_all_items_in_endpoint('SUBMISSIONS_ENDPOINT')
    if not (account_dict or answers_dict): # If there are no accounts or submissions in the database
        print('The entire database has been reset.')
        return
    if account_dict:
        assert isinstance(account_dict, dict), f'Unable to access accounts'
        for account in account_dict.values():
            response = requests.delete(f'{os.getenv('ACCOUNTS_ENDPOINT')}{account['id']}')
            print(f'Deleting account {account['id']} status: {response.status_code}')
    if answers_dict:
        assert isinstance(answers_dict, dict), 'Unable to access users\' answers'
        for submission in answers_dict.values():
            response = requests.delete(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{submission['id']}')
            print(f'Deleting submission {submission['id']} status: {response.status_code}')
    print('The entire database has been reset.')
    pass

@click.command('db-clearallanswers')
def clear_all_answers():
    answers_dict = get_all_items_in_endpoint('SUBMISSIONS_ENDPOINT')
    assert answers_dict and isinstance(answers_dict, dict), 'Unable to access users\' answers'
    for submission in answers_dict.values():
        empty_submission: dict = {
            'id': submission['id']
        }
        response = requests.put(f'{os.getenv('SUBMISSIONS_ENDPOINT')}{submission['id']}', json=empty_submission)
        print(f'Cleared submission {submission['id']} status: {response.status_code}')
    print('All submissions/answers have been cleared.')
    pass

@click.command('db-new')
def create_new_database():
    """ Overwrites or creates a new JSON database """
    text = '''
{
\t"admin-data": [
\t\t{
\t\t\t"id": "1025",
\t\t\t"answers_viewable": false,
\t\t\t"evaluation_viewable": false
\t\t}
\t],
\t"user_answers": [],
\t"accounts": []
}
    '''
    with open(f'flask/instance/db.json', 'wt') as db:
        db.write(text)
        print('A new JSON database has been created!')
        