import urllib
import json    
import os
from flask import (Flask,request, make_response,render_template)
from firebase import firebase
import selenium

import os

app=Flask(__name__)
firebase =firebase.FirebaseApplication('https://tesseract-23.firebaseio.com/',None)
result=firebase.get('patient',"")
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/webhook',methods=['POST'])
def webhook():
     if request.method == "POST":
        req = request.get_json(silent=True, force=True)
        res = processRequest(req)

        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r


def processRequest(req):

    # Get all the Query Parameter
    query_response = req["queryResult"]
    print(query_response)
    text = query_response.get('queryText', None)
    parameters = query_response.get('parameters', None)
    if (text in ['no','na','nope','noo','nooo','nop','yes','yup','hmm']):
        print("Gotcha")
        response="Connecting you to a specialist......Please click https://rajeshkumarkesavan.github.io/nuvi1.github.io/"
        res=get_data(response)
        os.system("python googlesafeweb_selenium.py")
    else:    
        password=parameters['pass']
        username=parameters['id'].lower()
        if(auth(username,password)):
            response= "Login Successful. Welcome "+username+". Let's help you out. 1.Connect to a doctor 2.View Medical records"
            res = get_data(response)
        else:
            response="Oops!!! You have entered incorrect ID or Password"
            res=get_data(response)

    return res
def auth(username,password):
    flag=False
    for i in result:
        if i is not None:
            if(i['id']==username and i['pass']==password):
                flag=True
    return flag
            


def get_data(response):
    return {
        "fulfillmentText": response
    }
app.run(port=5000)