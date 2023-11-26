#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(execp):
    """ close the current session """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ display a HTML page that return a list of all states """
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    """ display a HTML page that return a list of states if id exist """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state, id=id)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
