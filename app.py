from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Review Intelligence Tool — V1</h1>"


if __name__ == "__main__":
    app.run()
