from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, sendm SocketIO
import random
from string import ascii_uppercase