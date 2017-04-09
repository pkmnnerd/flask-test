from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is the homepage"

@app.route("/<path:path>")
def rest(path):
    return "You have hit the " + path + " endpoint."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
