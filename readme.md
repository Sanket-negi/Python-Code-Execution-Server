# Python Code Execution API 
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) 


This is a Python Code Execution API built with Flask that allows users to execute Python code in a secure and isolated environment. It provides an API for submitting Python code, running it, and retrieving the output. This can be integrated into platforms that need code execution features, like coding challenge platforms, learning tools, or testing environments.

## Features
Execute Python Code: Submit Python code via API, and get execution results.
Secure Execution: Code is executed in a controlled environment to prevent security risks.
Support for Python 3.x: The API uses Python 3.x for code execution.
Timeout Handling: Limits execution time to prevent infinite loops or long-running code.

## Tech Stack
- ` Python ` : versatile, high-level, interpreted, easy-to-learn programming language.
- ` Flask `: A lightweight Python web framework to build APIs.
- ` Subprocess `: Used to run Python code in a separate process.
- ` Timeouts ` : To prevent long or malicious code from running indefinitely.


## Prerequisites
Before getting started, make sure you have the following installed:

- Python 3.x  
- pip (Python package manager)
# Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:


```bash
git clone https://github.com/rahul-shrivastav/Python-Code-Execution-Server.git
```


### 2. Install Dependencies
Install the required Python dependencies by running:

```bash
pip install -r requirements.txt
```

### 3. Running the Flask Server
To start the Flask server locally, run:

```bash
python app.py
```

This will start the server on http://localhost:5000.

## API Reference

#### Execute the code

```http
POST /execute
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `code` | `string` | Code provided by the user to execute.  |

