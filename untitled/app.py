
from flask import Flask
from main import main
from config import run_config


app = Flask(__name__)

app.config.from_object(run_config())
app.register_blueprint(main)


if __name__ == '__main__':
    app.run()
