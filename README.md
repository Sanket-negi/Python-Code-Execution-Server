## Python Code Execution API
This is a Python Code Execution API built with Flask that allows users to execute Python code in a secure and isolated environment. It provides an API for submitting Python code, running it, and retrieving the output. This can be integrated into platforms that need code execution features, like coding challenge platforms, learning tools, or testing environments.

## Features
Execute Python Code: Submit Python code via API, and get execution results.
Secure Execution: Code is executed in a controlled environment to prevent security risks.
Support for Python 3.x: The API uses Python 3.x for code execution.
Timeout Handling: Limits execution time to prevent infinite loops or long-running code

## Tech Stack
Flask: A lightweight Python web framework to build APIs.
Docker (Optional but recommended for isolation): Provides isolated environments for running code securely.
Subprocess: Used to run Python code in a separate process.
Timeouts: To prevent long or malicious code from running indefinitely.


## Setup Instructions
# Prerequisites
Before getting started, make sure you have the following installed:

-Python 3.x
-pip (Python package manager)
-Docker (if using Docker for isolation)

#1. Clone the Repository
First, clone the repository to your local machine:

git clone https://github.com/your-username/Python-Code-Execution-Server

Then, navigate to the project directory:

cd Python-Code-Execution-Server

2. Install Dependencies
Install the required Python dependencies by running:

pip install -r requirements.txt

If you are using Docker for isolation, ensure Docker is installed and running on your machine.

3. Configure Environment Variables
Create a .env file (if necessary) for any specific configuration. For example, you can set a timeout limit or other variables if needed:

EXECUTION_TIMEOUT=5 # Timeout in seconds for code execution

4. Running the Flask Server
To start the Flask server locally, run:

python app.py

This will start the server on http://localhost:5000.

Alternatively, if you're using Docker for isolation, you can run the following command to build and start the application in a container:

docker-compose up --build

This will also start the server and make it accessible via http://localhost:5000.

API Endpoints
1. POST /execute
This endpoint receives Python code and executes it in a secure environment. The response will contain the output or any errors that occurred during execution.

Request Body
A JSON object with the code field containing the Python code to execute.

Example:

{ "code": "print('Hello, World!')" }

Response
A JSON object containing either the execution output or any error messages.

Example:

{ "output": "Hello, World!\n", "error": null }

output: The result of the code execution.
error: Any error messages if the code fails (e.g., syntax errors, runtime errors).
