from flask import Flask,render_template
app=Flask(__name__)
values={'name':'Rajesh','age':'20','temp':'90.5','description':'cough & cold','prescription':'just a regular checkup'}
@app.route("/")
def info():
    return render_template('medical.html',pname=values['name'],page=values['age'],ptemp=values['temp'],pdes=values['description'],ppres=values['prescription'])
app.run(port=3000)