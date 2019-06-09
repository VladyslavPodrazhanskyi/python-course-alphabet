import os
from flask import Flask
from main import main
from config import run_config
app = Flask(__name__)

app.register_blueprint(main)
app.config.from_object(run_config())



if __name__ == '__main__':
    app.run()
