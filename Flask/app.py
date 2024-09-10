# Flask
# 1. WSGI - WEB SERVER GATEWAY INTERFACE
#  HTTPS:// -> IS A protocol
# google.com -> is a domain
# 2. jinja -> web templating system
#url to run project : https://salmon-artist-uoywv.pwskills.app:5000/
from flask import Flask,request,render_template
# import request  #library in form json or any other we can retrieve from here
app = Flask(__name__)

#Route
#methods - 
# get - when you type google.com in browser it's a get request
# post - when you are searching for data for example search of animal (sending some data)
 
@app.route("/") #this is my home page # this is a get request as no methods are here
def hello_world():
    return render_template("index.html")

@app.route("/aboutus") #this is for my about us page
def aboutus():
    return "We are ineuron"

@app.route("/demo",methods= ['POST'])
def math_operation():
    if(request.method=='POST'):
        operation = request.json['operation'] #json is medium to connect with applications
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = 0

        if operation == "add":
            result = num1 + num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "division":
            result = num1 / num2
        else:
            result = num1 - num2

        return "The operation is {} and the result is {}".format(operation,result)

@app.route("/operation",methods= ['POST'])
def operation():
    if(request.method=='POST'):
        operation = request.form['operation'] #json is medium to connect with applications
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0

        if operation == "add":
            result = num1 + num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "division":
            result = num1 / num2
        else:
            result = num1 - num2

        return render_template("result.html",result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000) #for local 127.0.0.1, if I am not able to access port it means port is not open
