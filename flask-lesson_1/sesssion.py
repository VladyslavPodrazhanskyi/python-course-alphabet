from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)



app.secret_key = b'"\xaa;\x0b\x12\x8a\xa1V+\x16\xc5\x91\xfb,\xcb#'
app.permanent_session_lifetime(seconds=10)


@app.route("/test_session")
def test_session():
    app.logger.warning("this is warning")
    app.logger.error("This is error")
    session["key"] = "value"
    return "hello"


if __name__=="__main__":
    app.run()