from flask import Flask,request,redirect,url_for,render_template
from flask_cors import CORS,cross_origin
from markupsafe import escape
from jinja2 import Environment,FileSystemLoader,select_autoescape
from pymongo import MongoClient
from dotenv import load_dotenv
import os
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

app = Flask(__name__,template_folder='templates')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

pageNames:str = ["About Me","Projects","Contact Me"]

@app.route("/")
def main():
    db = client[os.getenv("DB")]
    collection = db[os.getenv("COLLECTION")]
    posts = collection.find({"Page":"Home"})
    posts = sortJSON(posts)
    dates = []
    for post in posts:
        timeStamp = post["createdAt"].split("T")
        dates.append(timeStamp)
    pageurls= [url_for('infoPage'),url_for("projectPage"),url_for("contactPage")]
    

    return render_template('landingPage.html',values=pageNames,urls=pageurls,posts=posts,dates=dates,iconKit=os.getenv("ICON_KIT"))

@app.errorhandler(404)
def lost404(error):
    return "<p>You are lost my guy... or gal. I'm too lazy to make a 404 page</p>"

@app.route("/page/<pageNumber>")
def showPostInFull(pageNumber):
    print("A post has been accessed")
    db = client[os.getenv("DB")]
    collection = db[os.getenv("COLLECTION")]
    if collection.count_documents({"_id" : ObjectId(pageNumber)}) > 0:
        res = collection.find_one({"_id":ObjectId(pageNumber)})
        pageurls= [url_for('infoPage'),url_for("projectPage"),url_for("contactPage")]

        if res["Page"] == "Notes":
            return render_template("postPage.html",values=pageNames,urls=pageurls,data=res,paragraphs=res["Body"].split("|"),mJAXScript=MathJAXScript,iconKit=os.getenv("ICON_KIT"))
        else:
            return render_template("postPage.html",values=pageNames,urls=pageurls,data=res,paragraphs=res["Body"].split("|"),iconKit=os.getenv("ICON_KIT"))
    else:
        return "Nothing to see here"

@app.route("/admin",methods=["POST","GET"])
@cross_origin()
def adminPage():
    if request.method == 'POST':
        app.logger.info("A new post has been requested")
        jsonBody = request.get_json()
        app.logger.info(jsonBody)
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
        pageurls= [url_for('infoPage'),url_for("projectPage"),url_for("contactPage")]
        return render_template("adminPage.html",values=pageNames,urls=pageurls,iconKit=os.getenv("ICON_KIT"))

@app.route("/aboutMe")
def infoPage():
    print("About me page was accessed")
    pageurls= [url_for('infoPage'),url_for("projectPage"),url_for("contactPage")]
    return render_template('aboutMe.html',values=pageNames,urls=pageurls,iconKit=os.getenv("ICON_KIT"))

@app.route("/contactMe")
def contactPage():
    print("Contact me page accessed")
    pageurls= [url_for('infoPage'),url_for("projectPage"),url_for("contactPage")]
    return render_template("contact.html",values=pageNames,urls=pageurls,iconKit=os.getenv("ICON_KIT"))

@app.route("/projects")
def projectPage():
    db = client[os.getenv("DB")]
    collection = db[os.getenv("COLLECTION")]
    posts = collection.find({"Page":"Notes"})
    posts = sortJSON(posts)
    pageurls= [url_for('infoPage'),url_for("projectPage"),url_for("contactPage")]
    return render_template('projects.html',values=pageNames,urls=pageurls,posts=posts,iconKit=os.getenv("ICON_KIT"))