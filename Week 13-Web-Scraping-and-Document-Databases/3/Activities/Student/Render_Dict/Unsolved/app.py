# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app = Flask(__name__)


# @TODO: Create a list of dictionaries
@app.route("/")
def index():
    player_dictionary = {"player_1": "Matt Carpenter",
                         "player_2": "Marcell Ozuna"}
    return render_template("index.html", dict=player_dictionary)

# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
# CODE GOES HERE

if __name__ == "__main__":
    app.run(debug=True)
