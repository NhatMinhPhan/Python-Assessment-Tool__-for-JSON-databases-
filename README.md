This work-in-progress is created for experiential purposes and not for professional use.

# Python Assessment Tool

This tool aims to aid tutors in assessing their tutees' Python knowledge and skills currently with a JSON server, and is expected to implement a SQLite server in the near future.

For this iteration of the tool, it is used as follows: The tutor sets up a JSON server with a .json file, an .env file, and a development server or server of another type to run the React code. Then, they need to generate a Localhost tunnel, with [pinggy.io](https://pinggy.io/) for example, to connect with the tutees.

## JSON Server

### Summary

Create a db.json file in react/python-assessment-tool and follow this [link](https://www.npmjs.com/package/json-server) to install the json-server package.

Subsequently, enter the following into the terminal: `json-server db.json`.

**NOTE**: Currently, users' credentials (username, password) are **not** stored securely and privately. Operate with caution and care.

### Structure

Copy and paste the following block into db.json.

```
{
    "accounts": [],
    "user_answers": []
}
```

## .env file

The .env file must consist of the following (note that this project is developed with Vite, thereby resulting in the variables prefixed by "VITE"):

`VITE_TOTAL_QUESTIONS`: Total number of questions to give the tutees\
`VITE_USER_NAME`: Placeholder username\
`VITE_USER_ID`: Placeholder user ID\
`VITE_ANSWER_SUBMISSION_ENDPOINT`: JSON server endpoint (or endpoint in a server of another type) that stores users' submissions of their code\
`VITE_ACCOUNTS`: JSON server endpoint (or endpoint in a server of another type) that stores users' credentials

## Development server

This section only discusses Vite which is used to work on this project.
For other tools like Vite, please refer to their documentation.

Remember to install dependencies included by package.json in react/python-assessment-tool.

To run the development server and use Localhost, enter in the terminal: `yarn run dev` using Yarn or `npm run dev` using npm.

## Localhost tunnel

Tutors need to generate a Localhost tunnel, with [pinggy.io](https://pinggy.io/) for instance, to connect with the tutees directly from localhost.
