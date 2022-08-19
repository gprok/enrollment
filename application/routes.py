from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return "<h1>Login</h1>"

@app.route("/register")
def register():
    return "<h1>Register</h1>"

@app.route("/courses")
def courses():
    return "<h1>Courses</h1>"

@app.route("/enrollment")
def enrollment():
    return "<h1>Enrollment</h1>"