# Lexical Analysis

![GitHub repo size](https://img.shields.io/github/repo-size/ranjanikrishnan/Lexical-analysis)
![Python](https://img.shields.io/badge/python-v3.7-blue)

## Project Description
- A lexical analysis API which calculates the lexical density of the inputted text.
- Lexical density ​ is defined as the number of ​ lexical words​ (or content words) divided by the
total number of words.
- For example, in the sentence -

    "Kim loves going to the cinema",

    Kim, loves, going, and cinema are lexical words and the density is 67%.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python (version 3.7)
* Docker
* Docker-Compose 

### Local Setup
- Clone the repo
    ```
    git clone https://github.com/ranjanikrishnan/Lexical-analysis
    ```
- Install the dependencies
    ```
    pip install -r requirements.txt
    ```
- Create .env file and update environment variables (refer .env.example)

- Seed the database

    ```
    python mongo/seed_db.py 
    ```
- Start the app
    ```
    python src/app.py
    ```

### Docker Setup

- Run the following:

    ```
    docker-compose up
    ```

### Project details
Exposed APIs -
- GET http://localhost:5000/api/docs - Swagger Documentation
- POST http://localhost:5000/complexity - Lexical Analysis API
    - http://localhost:5000/complexity - Returns the lexical density of the inputted text. The input text is provided via the request.
    - http://localhost:5000/complexity?mode=verbose - Returns the lexical density of the text broken down into sentences. The input text is provided via the request.
 

### Tests

- To get the test coverage, run the following:

    ```
    pytest --cov=src tests/
    ```
