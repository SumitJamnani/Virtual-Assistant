import speech_recognition as sr
import pyttsx3 
from datetime import datetime
import calendar
import wikipedia
import webbrowser
import os
import smtplib
import private as p
import random

def rec():
        with sr.Microphone() as source:
            try:
                print("Listening...",end="\n\n")
                r=sr.Recognizer()
                audio=r.listen(source,timeout=5)
                qry = r.recognize_google(audio)
                print(f"you said : {qry}",end="\n\n")
                return qry.lower()
            except:
                tell("Can not unserstand, Say it again..")
                rec()

def tell(qry):
    eng=pyttsx3.init()
    eng.say(qry) 
    eng.runAndWait()

j=0
while j!=1:
    with sr.Microphone() as source:
        print("listening..")
        r=sr.Recognizer()
        audio=r.listen(source,timeout=5)
        qry = r.recognize_google(audio)
        print("You said : ",qry)    
    qry=qry.lower()
    if 'how are you' in qry:
        tell("I'm good")

    elif 'who are you' in qry:
        tell("i'm your virtual assistant")

    elif 'my' in qry:
        if 'name' in qry:
            tell("sumit jamnani")
        elif 'birthday' in qry:
            tell("5 mar 2000")

    elif 'date' in qry:
                    try:
                        date = datetime.now().strftime("%m/%d/%Y")
                        day=calendar.day_name[datetime.today().weekday()]
                        tell(f"The date is {date} and today is {day}")
                    except Exception as e:
                        pass

    elif 'time' in qry:
                    try: 
                        time = datetime.now().strftime("%H:%M:%S")  
                        day=calendar.day_name[datetime.today().weekday()]
                        tell(f"The time is {time} and today is {day}")
                    except Exception as e:
                        pass
                    
    elif 'wikipedia' in qry:
                    try:
                        tell("\nSearching Wikipedia...")
                        qry = qry.replace("wikipedia","")
                        results=wikipedia.summary(qry,sentences=2)
                        print(results)  
                        tell(results)
                    except Exception as e:
                        pass

    elif 'search' in qry or 'near me' in qry:
                    try:
                        tell("Searching")
                        qry=qry.replace("search","")
                        # qry=qry.replace(" ","+")
                        # data1="https://www.google.com/search?source=hp&q="+qry
                        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new_tab(qry)
                    except Exception as e:
                        pass

    elif 'open code' in qry:
        code_path = "C:\\Users\\sumit jamnani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif  'music' in qry:
                    try:
                        song_list="C:\\Users\\sumit jamnani\\music"
                        songs=os.listdir(song_list)
                        os.startfile(os.path.join(song_list,songs[1]))
                    except Exception as e:
                        print(e)

    elif 'mail' in qry:
                    try:
                        tell("who is reciever ?")
                        reciever=rec()
                        reciever=reciever.lower()
                        reciever=reciever.replace(" ","")
                        tell("what is your message ?")
                        content=rec()
                        print("Sending mail..")
                        server=smtplib.SMTP('smtp.gmail.com',587)
                        server.ehlo()
                        server.starttls()
                        server.login(p.username1,p.password)
                        server.sendmail(p.username1,reciever,content)
                        server.close()
                        tell("Mail send successfully")
                    except Exception as e:
                        print(e)

    elif 'exit' in qry:
            j=1

