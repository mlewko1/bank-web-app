from flask import Flask, render_template
from storage.database import init_db

app = Flask(__name__)
init_db()


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
