from flask import Flask

# create flask app
app = Flask(__name__)


# add all the routes

@app.route("/", methods=["GET"])
def root():
    return '<h1 style="color: blue">Welcome to my Flask Application VERSION-2...!</h1>'


# run the application
app.run(host="0.0.0.0", port=4000, debug=True)
