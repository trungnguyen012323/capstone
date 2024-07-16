import os
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN": "dev-iuxikjrwwua3xm2p.us.auth0.com",
    "ALGORITHMS": ["RS256"],
    "API_AUDIENCE": "http://localhost:5000",
    
}

pagination = {
    "example": 10  # Limits returned rows of API
}

bearer_tokens = {
    "casting_assistant": "Bearer ...",
    "executive_producer": "Bearer ...",
    "casting_director": "Bearer ..."
}

# Database setup
database_name = "capstone"
username = "postgres"
password = "12345"
database_path = "postgresql://{}:{}@localhost:5432/{}".format(username, password, database_name)


def database_setup(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
