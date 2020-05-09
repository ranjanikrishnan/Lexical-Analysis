# Lexical Analysis

![GitHub repo size](https://img.shields.io/github/repo-size/ranjanikrishnan/Lexical-analysis)
![Python](https://img.shields.io/badge/python-v3.7-blue)


## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python (version 3.7)
* Docker
* Docker-Compose 

### Local
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

### Docker

- Run the following:

    ```
    docker-compose up
    ```

### Tests

- To get the test coverage, run the following:

    ```
    pytest --cov=src tests/
    ```
