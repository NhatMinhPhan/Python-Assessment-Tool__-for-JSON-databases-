# In each 'examination' folder, there are only 2 files: judge.py & response.py.
# Find respective 'response.py' in this 'examination' folder

import_failed = True

# @after_successful_import decorator
def after_successful_import(func):
    def wrapper(*args, **kwargs):
        if import_failed:
            print('Unable to proceed due to failed import of response.py')
            return
        return func(*args, **kwargs)
    return wrapper

# Import response.py
try:
    from . import examination
except:
    print('response.py not found or unreadable')
else:
    import_failed = False

@after_successful_import
def run() -> bool:
    """
    Invoke the judge (as in judge.py) and examine response.py.

    Returns:
        True if response.py satisfies the requirements set out by this instance of judge.py
        False otherwise
    """
    # Add custom code for response.py here
    pass

