from flask import Flask,request,redirect,url_for,render_template
from markupsafe import escape
from jinja2 import Environment,FileSystemLoader,select_autoescape
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import datetime as dt
from customModules.sort import sortJSON

load_dotenv()
client = MongoClient(os.getenv("URI"))

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

app = Flask(__name__)

@app.get("/")
def main():
    db = client[os.getenv("DB")]
    collection = db[os.getenv("COLLECTION")]

    if collection.count_documents({}) > 1:
        posts = collection.find()
        posts = sortJSON(posts)

    return render_template('landingpage.html',values=["About Me","Contact","Posts"],urls=[url_for('infoPage'),url_for("main"),url_for("main")],socials=["https://github.com/JohanTheNamelessMonster"],tools=[["https://tailwindcss.com/","Tailwind CSS"],["https://flask.palletsprojects.com/en/stable/","Flask"]],posts=posts)

@app.errorhandler(404)
def restore(error):
    return redirect(url_for("main"))

@app.route("/one/<name>")
def one(name=None):
    name = request.args.get("name", name)
    if not name:
        return f"Hello Bruh"
    else:
        return f"Hello {escape(name)}"

@app.route("/aboutMe")
def infoPage():
    return render_template('infoPage.html',values=["About Me","Contact","Posts"],urls=[url_for('infoPage'),url_for("main"),url_for("main")])