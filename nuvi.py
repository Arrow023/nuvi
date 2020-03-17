import speech_recognition as sr
import pyttsx3
import time
from flask import Flask, render_template,send_file
import random
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('rate',170)
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
values={'name':'','age':'','temp':'','description':'','prescription':''}
portno=random.randint(1024,5000)
app=Flask(__name__)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r=sr.Recognizer()
    while(True):
        with sr.Microphone() as source:
            print('Listening to source.....')
            r.pause_threshold=0.5
            audio=r.listen(source)
        try:
            print('Recognizing....')
            query=r.recognize_google(audio,language='en-in')
            print(f'User said:{query}\n')
            return query
        
        except Exception as e:
            #print(e)
            speak("sorry! I couldn't get you.")
            
        
def getData():
    speak("Please..say..Patient's name")
    query=takeCommand().lower()
    values['name']=query
    print("Patient's Name:",values['name'])
    speak("What is the age?")
    query=takeCommand()
    values['age']=query
    print("Patient's age: ",values['age'])
    speak("What's the current body temperature?")
    query=takeCommand().lower()
    values['temp']=query
    print("")
    speak("What's the problem of the patient?")
    query=takeCommand().lower()
    values['description']=query 
    speak("What's the treatment required?")
    query=takeCommand().lower()
    values['prescription']=query
    speak("Thank you! for providing the information.")

if __name__ == "__main__":
    print("Starting Nuvi....")
    time.sleep(1)
    print("Building cache....")
    time.sleep(1)
    print("Request for access..")
    time.sleep(1)
    speak("Hello. My name is Nuvi. I'm your personal, medical assistant.")
    getData()
    #values={'name':'Rajesh','age':'20','temp':'90.5','description':'cough & cold','prescription':'just a regular checkup'}
    f=open("formdata.txt","w")
    for i in values.keys():
        f.write(values[i]+"\n")
    f.close()
    speak("Your report is ready. You can visit 127.0.0.1:"+str(portno)+" for view")
    @app.route('/')
    def start():
        return render_template('medical.html',pname=values['name'],page=values['age'],ptemp=values['temp'],pdes=values['description'],ppres=values['prescription'])
    app.run(port=portno)


        
    

    

    


    
    

    