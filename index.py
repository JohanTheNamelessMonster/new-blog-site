from flask import Flask,request,redirect,url_for,render_template
import requests
from flask_cors import CORS,cross_origin
from markupsafe import escape
from jinja2 import Environment,FileSystemLoader,select_autoescape
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import timeit
import json
import datetime as dt
from customModules.sort import sortJSON
from bson.objectid import ObjectId

load_dotenv()
client = MongoClient(os.getenv("URI"))

MathJAXScript = 'https://cdn.jsdelivr.net/npm/mathjax@4.0.0/tex-mml-chtml.js'

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def main():
    db = client[os.getenv("DB")]
    collection = db[os.getenv("COLLECTION")]
    posts = collection.find({"Page":"Home"})
    posts = sortJSON(posts)

    return render_template('landingpage.html',values=["About Me","Notes"],urls=[url_for('infoPage'),url_for("notesPage")],socials=["https://github.com/JohanTheNamelessMonster"],tools=[["https://tailwindcss.com/","Tailwind CSS"],["https://flask.palletsprojects.com/en/stable/","Flask"]],posts=posts,iconKit=os.getenv("ICON_KIT"))

@app.errorhandler(404)
def restore(error):
    return "<p>You are lost my guy... or gal. I'm too lazy to make a 404 page</p>"

@app.route("/notes")
def notesPage():
    db = client[os.getenv("DB")]
    collection = db[os.getenv("COLLECTION")]
    posts = collection.find({"Page":"Notes"})
    posts = sortJSON(posts)

    return render_template('landingpage.html',values=["About Me","Notes"],urls=[url_for('infoPage'),url_for("notesPage")],socials=["https://github.com/JohanTheNamelessMonster"],tools=[["https://tailwindcss.com/","Tailwind CSS"],["https://flask.palletsprojects.com/en/stable/","Flask"]],posts=posts,iconKit=os.getenv("ICON_KIT"))

@app.route("/page/<pageNumber>")
def showPostInFull(pageNumber):
    print("A post has been accessed")
    db = client[os.getenv("DB")]
    collection = db[os.getenv("COLLECTION")]
    if collection.count_documents({"_id" : ObjectId(pageNumber)}) > 0:
        res = collection.find_one({"_id":ObjectId(pageNumber)})
        if res["Page"] == "Notes":
            return render_template("postPage.html",values=["About Me","Notes"],urls=[url_for('infoPage'),url_for("notesPage")],socials=["https://github.com/JohanTheNamelessMonster"],tools=[["https://tailwindcss.com/","Tailwind CSS"],["https://flask.palletsprojects.com/en/stable/","Flask"]],data=res,paragraphs=res["Body"].split("|"),mJAXScript=MathJAXScript,iconKit=os.getenv("ICON_KIT"))
        else:
            return render_template("postPage.html",values=["About Me","Notes"],urls=[url_for('infoPage'),url_for("notesPage")],socials=["https://github.com/JohanTheNamelessMonster"],tools=[["https://tailwindcss.com/","Tailwind CSS"],["https://flask.palletsprojects.com/en/stable/","Flask"]],data=res,paragraphs=res["Body"].split("|"),iconKit=os.getenv("ICON_KIT"))
    else:
        return "Nothing to see here"

@app.route("/admin/secretPage",methods=["POST","GET"])
@cross_origin()
def adminPage():
    if request.method == 'POST':
        print("A new post has been requested")
        jsonBody = request.get_json()
        if jsonBody["data"]["password"] == os.getenv("HASHED_PASSWORD"):
            db = client[os.getenv("DB")]
            collection = db[os.getenv("COLLECTION")]
            try:
                if jsonBody["data"]["command"] == "CREATE":
                    x = collection.insert_one({
                    "Title":jsonBody["data"]["title"],
                    "Body":jsonBody["data"]["body"],
                    "createdAt":dt.datetime.now().isoformat(),
                    "Page":jsonBody["data"]["page"]
                    })

                    print("New Post Made")
                    return redirect(f"/page/{x.inserted_id}")
                elif jsonBody["data"]["command"] == "UPDATE":
                    x = collection.find_one_and_update({"_id": ObjectId(jsonBody["data"]["oid"])},{
                        "$set":{
                        "Title":jsonBody["data"]["title"],
                        "Body":jsonBody["data"]["body"],
                        "Page":jsonBody["data"]["page"]
                        }})
                    target = x["_id"]
                    print(f"Post {target} has been updated")
                    return redirect(f"/page/{target}")
                elif jsonBody["data"]["command"] == "DELETE":
                    x = collection.delete_one({"_id":ObjectId(jsonBody["data"]["oid"])})
                    print("A post has been deleted")
                    return redirect("/")
                else:
                    print("Post with no 'command' was given")
                    return "No command received!"
            except Exception as e:
                print(e.args)
                return f"New error caught: {e}"
        else:
            print("Post denied due to invalid password")
            return "Invalid Password"
    else:
        return render_template("adminPage.html",values=["About Me","Notes"],urls=[url_for('infoPage'),url_for("notesPage")],socials=["https://github.com/JohanTheNamelessMonster"],tools=[["https://tailwindcss.com/","Tailwind CSS"],["https://flask.palletsprojects.com/en/stable/","Flask"]],iconKit=os.getenv("ICON_KIT"))

@app.route("/aboutMe")
def infoPage():
    print("About me page was accessed")
    return render_template('aboutMe.html',values=["About Me","Notes"],urls=[url_for('infoPage'),url_for("notesPage")],socials=["https://github.com/JohanTheNamelessMonster"],tools=[["https://tailwindcss.com/","Tailwind CSS"],["https://flask.palletsprojects.com/en/stable/","Flask"]],iconKit=os.getenv("ICON_KIT"))