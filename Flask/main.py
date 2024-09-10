#url to run project : https://salmon-artist-uoywv.pwskills.app:5000
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Welcome to the home page<h1>"

@app.route("/add",methods = ['POST'])
def addition():
    if request.method == "POST":
        result = int(request.json["num1"]) + int(request.json["num2"])
        return jsonify("The summation is {}".format(result))
        
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000) 