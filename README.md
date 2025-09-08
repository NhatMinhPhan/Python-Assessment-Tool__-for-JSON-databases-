This program is created for experiential purposes and not for professional use.

# Python Assessment Tool

This tool aims to aid tutors in assessing their tutees' Python knowledge and skills currently with a JSON server, and is expected to implement a SQLite server in the near future as a more secure way of storing data.

For this iteration of the tool, it is used as follows: The tutor sets up a JSON server with a .json file, 2 separate .env files for the front- and back-end, a development server or server of another type to run the React code, and another development server to run the Flask code. In total, one will need at least 3 servers to operate the whole program. Then, according to the plan for the development of this tool, they would need to generate a Localhost tunnel, with [pinggy.io](https://pinggy.io/) for example, to connect with the tutees.

## Requirements

Besides React, Flask and the latter's accompanying packages, to properly use this tool, the following packages must be installed with [pip](https://pypi.org/project/pip/) and [npm](https://www.npmjs.com/package/json-server). A **virtual environment** (_venv_) must be created and set up to run this program.

- `json-server`: Installed with [npm](https://www.npmjs.com/package/json-server). This package is used to set up a JSON server for the JSON database, `db.json`.
- `flask-cors`: Installed with [pip](https://pypi.org/project/flask-cors/). This package is a Flask extension for handling Cross Origin Resource Sharing (CORS).
- `python-dotenv`: Installed with [pip](https://pypi.org/project/python-dotenv/). This package helps set key-value pairs in a `.env` file as environmental variables.
- `requests`: Installed with [pip](https://pypi.org/project/requests/). This package is used to handle and send HTTP requests.

## JSON Server & Database

### Summary

Create a `db.json` file in a folder called `instance` in the `flask` directory (in other words, `flask/instance/`).

Subsequently, enter the following command into the terminal: `json-server db.json`, if your current working directory is `flask/instance/`. Otherwise, modify the command according to whatever directory which you are working with.

**NOTE**: Even with encrypted data thanks to Flask and its accompanying packages and modules, users' credentials (usernames, passwords) are currently **not** stored securely and privately due to the manner of storage of the database used (JSON database). Operate with caution and care.

### Structure

Copy and paste the following block into db.json.

```
{
    "admin-data": [
    {
      "id": "1025",
      "answers_viewable": false,
      "evaluation_viewable": true
    }
    ]
    "accounts": [],
    "user_answers": []
}
```

#### Admin data (`"admin-data"`)

`"answers_viewable"`: `true` if the administrator/tutor allows tutees to view their submitted code (which they cannot edit), `false` to disable the visibility of the submitted code\
`"evaluation_viewable'`: `true` if the administrator/tutor allows tutees to view the results of the program's evaluation of their code, `false` to disable the visibility of the evaluation results

Note that the `"id"` in `"admin-data"` has no practical and considerable use or significance in the operations of this assessment tool, so it can be other than `"1025"`. However, it **should** not be removed, as it potentially allows the block containing `"answers_viewable"` and `"evaluation_viewable"` to be deemed as an item of the `"admin-data"` array.

## .env Files

There are **TWO** .env files needed for this tool to function properly:

- A `.env.local` file located in `react/python-assessment-tool` for the React code
- A `.env` file located in `flask/instance` (create the directory if it does not exist yet) for the Flask code

### .env.local for React

The `.env.local` file _(the former of the aforementioned .env files)_ must consist of the following (note that this project is developed with Vite, thereby resulting in the variables prefixed by "VITE"):

`VITE_TOTAL_QUESTIONS`: Total number of questions to give the tutees (**MUST** be used/modified for the assessment tool to display the correct number of questions)\
`VITE_USER_NAME`: Placeholder username\
`VITE_USER_ID`: Placeholder user ID\
`VITE_ANSWER_SUBMISSION_ENDPOINT`: JSON server endpoint that stores users' submissions of their code\
`VITE_ACCOUNTS`: JSON server endpoint that stores users' credentials

`VITE_FLASK_SERVER`: URL to the Flask (development) server's index page\
`VITE_FLASK_REGISTER_DUPLICATECHECK`: The Flask server route which verifies whether the username being registered is a duplicate of one in the database, meaning it has already been taken\
`VITE_FLASK_LOGIN_DUPLICATECHECK`: The Flask server route which verifies whether the username whose associated account the user is logging in is a duplicate of one in the database, meaning the aforementioned account is in the database\
`VITE_FLASK_REGISTER`: The Flask server route for registering new accounts\
`VITE_FLASK_LOGIN`: The Flask server route for logging in an account\
`VITE_FLASK_LOGOUT`: The Flask server route for logging out of an account\
`VITE_FLASK_EVAL_SUBMIT`: The Flask server route for processing code submissions\
`VITE_FLASK_EVAL_SET_VIEWABILITY`: The Flask server route for setting the visibility of certain frontend components, during the programming page\
`VITE_FLASK_EVAL_RESULTS`: The Flask server route for fetching the results of evaluating the user's code submission\
`VITE_FLASK_EVAL_USERCODE`: The Flask server route for fetching the user's code submission, now uneditable.

### .env for Flask

The `.env` file _(the latter of the aforementioned .env files)_ must include the following:

`SUBMISSIONS_ENDPOINT`: JSON server endpoint that stores users' submissions of their code\
`ACCOUNTS_ENDPOINT`: JSON server endpoint that stores users' credentials\
`LOGIN_REQUIRED_ENDPOINT`: Link to the **login page** of the React app (frontend)\
`ADMINDATA_ENDPOINT`: JSON server endpoint that stores admininstrative data, **specifically** visibility settings of certain frontend components\
`CENSORED_DIRECTORY_SECTION`: The text needed to censor out when displayed on the frontend (specifically the beginning of the directory, which sees), which is then replaced with an ellipsis (...)\
`FLASKAPP_CONTENT_DIRECTORY`: The directory (**absolute** path) where the entire content of `flaskapp` is found (e.g. `flask/flaskapp`)\
`VENV_LIB_DIRECTORY`: The directory (**absolute** path) where the libraries and packages are found in the **virtual environment** (_venv_)

## Assessment Setup

1. Set up your .env files: Refer to the _env files_ section for instructions on setting up the .env files. Especially, you must set `VITE_TOTAL_QUESTIONS` in the `.env.local` for the Flask code to the number of questions which will be asked to tutees.
2. Using the `examination_template` folder in `flask/flaskapp/examinations`, make copies of the folder inside that directory (`flask/flaskapp/examinations`) and name them `examination_<number>` from `0` to `VITE_TOTAL_QUESTIONS` above. As an example, `examination_0` and `examination_1` have been created and appear in `flask/flaskapp/examinations`.\
   Each `examination_<number>` folder will assess Question `<number + 1>` on the frontend. For instance, `examination_0` assesses Question 1, `examination_1` evaluates Question 2, and so on.
3. Modify the test cases according to the tutor's questions and needs. Use the `test_case_output` decorator to evaluate outputs of the tutee's Python functions, and use `test_case_exception` if the tutee's functions are expected to raise an exception/error.

Refer to the `plain_pyscripts` folder to view examples of how test cases should be structured in `judge.py`. For more information, head to the _Additional Material: plain_pyscripts_ section.

And finally, run the JSON server (mentioned above), and the two development servers and the Localhost tunnels below. You are now ready to begin the assessment!

## React Development Server

This section only discusses Vite which is used to work on this project.
For other tools like Vite, please refer to their documentation.

Remember to install dependencies included by `package.json` in `react/python-assessment-tool`.

To run the development server and launch Localhost, enter in the terminal: `yarn run dev` using Yarn or `npm run dev` using npm, while your working directory is `react/python-assessment-tool`.

## Flask Development Server

The Flask program used to operate the backend of this tool is structured around a Flask _"app factory"_. Therefore, to activate the program, at the parent current directory of this project, enter the following command in the terminal: `flask --app flask/flaskapp run --debug --no-reload`.

The reason for `--no-reload` in the command above is that the program heavily relies on file modification while evaluating the tutees' submitted Python code. Without it, the program's file modification will automatically reload the server, and inconveniently halt the evaluation process and affect other crucial processes between front- and backend for the program to run smoothly.

## Localhost Tunnel (yet to be tested)

The content of this section has **not** yet been verified or tested, and thus it is heavily subject to speculation.

Tutors will need to generate **TWO** Localhost tunnel, with [pinggy.io](https://pinggy.io/) for instance, to connect with the tutees directly from localhost. One is for the React development server, and the other is for the Flask development server. The JSON server preferably **should not** have its own Localhost tunnel.

The .env files will presumably have to be adjusted according to the URLS of the Localhost tunnels.

## Additional Material: _plain_pyscripts_

`plain_pyscripts` refers to a folder containing material foundational to the `judge.py` files and their `examination_<number>` folders which evaluate the tutees' Python submissions. It is not at all involved in the operation of the assessment tool, but one may examine or use it to evaluate Python code independent of any frontend or database.

Within the `plain_pyscripts` folder are examples showing what kinds of code this program can evaluate. You may run the individual `judge.py` in the folders to experience how the tool processes these examples, or run the `__init__.py` if you prefer a more "indirect" approach.

If you decide to use `__init__.py`, you can change the argument in the last line `run_judge('plain_pyscripts\\examination_collections')` to a directory of the example code of your choice. Specifically, swap `<examination-example>` in `run_judge('plain_pyscripts\\<examination-example>')` with the name of the directory of your chosen example code before you run the file.

The following is a description of each `examination` folder in `plain_pyscripts`:

- `examination_addints`: Assessing the method for computing the sum of a number of integers
- `examination_classes`: Assessing the use of Python classes
- `examination_collections`: Assessing the use of Python collections (namely lists and tuples)
- `examination_template`: The customizable template of `examination_<number>`
