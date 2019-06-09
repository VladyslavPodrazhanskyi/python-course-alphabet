from flask import Blueprint, current_app

main = Blueprint("main", __name__)

@main.route("/")
def hello_from_main():
    return current_app.config.get("DB_CONNECTION")

