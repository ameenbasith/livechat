from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "redwood"
socketio = SocketIO(app)


@app.route("/", methods=['POST', 'GET'])  # decorator outlining what methods are allowed
def home():
    return render_template("home.html")  # can pass in vars such as chats= etc...


if __name__ == "__main__":
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
