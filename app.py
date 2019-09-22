from flask import Flask, Response, request, jsonify
from flask_pymongo import pymongo
from database import DatabaseConnection
from flask import render_template

app = Flask(__name__)
db = DatabaseConnection()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/process/addUser', methods=['POST']) #signup fuction
def addNewUser():
    pw1 = request.form["password"]
    pw2 = request.form["re_password"]
    if (pw1 == pw2):
        document = {
            "name": request.form["name"],
            "email": request.form["email"],
            "password": request.form["password"],

            }
        db.insert("users", document)
        return Response("User successfully added", status=200, content_type = "text/html")
    else:
            return Response("Passwords do not match! Try again!", status=200, content_type = "text/html")

@app.route('/process/letUserIn', methods=['POST']) #signin fuction
def letNewUserIn():
    document = {
        "email": request.form["email"],
        "password": request.form["password"]
        }
    #document = {
        #"email": request.form["email"],
        #"password": request.form["password"],

    #}
    result = db.findOne("users", document)

    if (db.findOne("users", document)):
        response = "Hello " + document.get("email") + "!"
        return Response(response, status=200, content_type = "text/html")
    else:
        return Response("Invalid Request", status=200, content_type = "text/html")
