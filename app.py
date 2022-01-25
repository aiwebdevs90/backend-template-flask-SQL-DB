import os
from flask import Flask, render_template

if os.path.exists("env.py"):
    import env

# Creating a Flask Instance
app = Flask(__name__)


#  Creating a route decorator for homepage
@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
