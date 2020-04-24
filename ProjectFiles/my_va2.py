import speech_recognition as sr # for speech recognition
import pyttsx3                  # for text to speech
import wikipedia                # for searching wikipedia
import webbrowser               # for search in webbrowser
import os                       # for open any software
import smtplib                  # for send mail 
import calendar                 # for calender
import random                   # for random selection
from datetime import datetime   # for time
from pygame import mixer
 
# import la                       # import external file
import private as p             # import external file

eng=pyttsx3.init()           # set synthesizer SAPI5
eng.setProperty('rate', 150) # setting up new property rate
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[2].id) # set female voice 

def rec():
        with sr.Microphone() as source:
            try:
                print("Listening...",end="\n\n")
                r=sr.Recognizer()
                # r.adjust_for_ambient_noise(source)
                audio=r.listen(source,timeout=5)
                qry = r.recognize_google(audio)
                print(f"you said : {qry}",end="\n\n")
                return qry.lower()
            except:
                tell("Can not unserstand, Say it again..")
                rec()

def tell(qry):
    eng.say(qry)
    eng.runAndWait()

def greet():
    intro="How can i help you ?"
    time=(int)(datetime.now().hour)
    if time > 0 and time < 12:
        tell(f"Good Morning , {intro}")
    elif time < 17:
        tell(f"Good Afternoon , {intro}")
    else:
        tell(f"Good Evening , {intro}")

def ex():
    tell("sorry , i can not understant")

def main():
    i = 0 
    greet()
    while i!=1:
        with sr.Microphone() as source:
            try:
                print("Listening...",end="\n\n")
                r=sr.Recognizer()
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source,timeout=5)
                qry = r.recognize_google(audio)
                print(f"you said : {qry}",end="\n\n")
                qry=qry.lower()

                if 'hello' in qry:
                    if 'my' in qry:
                        if 'name' in qry:
                            tell("Hello, sumit jamnani")
                    else:
                        tell("Hii")

                elif 'my' in qry:
                    if 'name' in qry:
                        tell("Hello, lucky")
                    elif 'birthday'  in qry or 'birth date' in qry:
                         tell("As per my data. your date of birth is 5 march ")
                    elif 'girlfriend' in qry:
                        tell('I am your Girlfriend,...I Love you')
                    elif 'wife' in qry:
                        tell('HA HA HA HA HA HA, Best of Luck')

                elif 'news' in qry:
                    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en")

                elif 'open' in qry:
                    if 'code' in qry:
                        try:
                            code_path = "C:\\Users\\sumit jamnani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                            os.startfile(code_path)
                        except Exception as e:
                            ex()
                    else:                        
                        try:
                            qry=qry.replace("open","")
                            qry=qry.replace(".com","")
                            if(qry!=""):
                                webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new_tab(qry+".com")
                        except Exception as e:
                            ex()

                elif 'wikipedia' in qry:
                    try:
                        tell("\nSearching Wikipedia...")
                        qry = qry.replace("wikipedia","")
                        results=wikipedia.summary(qry,sentences=2)
                        print(results)  
                        tell(results)
                    except Exception as e:
                        ex()        

                elif 'search' in qry or 'near me' in qry:
                    try:
                        tell("Searching")
                        qry=qry.replace("search","")
                        qry=qry.replace(" ","+")
                        data1="https://www.google.com/search?source=hp&q="+qry
                        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new_tab(data1)
                    except Exception as e:
                        ex()

                elif 'music' in qry:
                    try:
                        song_list="C:\\Users\\sumit jamnani\\music"
                        songs=os.listdir(song_list)
                        os.startfile(os.path.join(song_list,songs[random.randrange(5)]))
                    except Exception as e:
                        ex()

                elif 'youtube' in qry:
                    qry=qry.replace("play","")
                    qry=qry.replace("on","")
                    qry=qry.replace(" ","+")
                    print(qry)
                    data1="https://www.youtube.com/search?source=hp&q="+qry
                    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new_tab(data1)

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

                elif 'sumit' in qry:   
                    if 'boyfriend' in qry:
                        tell("HAHAHAHHA!! ")
                    elif 'ghar' in qry:
                        mixer.init()
                        mixer.music.load("audio1.mpeg")
                        mixer.music.play()
                    elif 'where' in qry:
                        mixer.init()
                        mixer.music.load("audio3.mpeg")
                        mixer.music.play()
                                      
                elif 'who are you' in qry:
                    tell("I am Elja, your virtual assistant , Always ready for your commands")

                elif 'how are you' in qry:
                    tell("I am fine, thanks for asking..")

                elif 'good' in qry:
                    tell("Thank you, it is my work")

                elif 'thank you' in qry:
                    tell("NOO, it is my work")

                elif 'you do' in qry:
                    tell("I can")
                    print("I can... \n")
                    print("Play music\nMessage someone\nMail someone\nSearch anything\nOpen anything\nCurrent information\npersonal information\nTell jokes\netc.\n")

                elif 'date' in qry:
                    try:
                        date = datetime.now().strftime("%m/%d/%Y")
                        day=calendar.day_name[datetime.today().weekday()]
                        tell(f"The date is {date} and today is {day}")
                    except Exception as e:
                        ex()

                elif 'time' in qry:
                    try: 
                        time = datetime.now().strftime("%H:%M:%S")  
                        day=calendar.day_name[datetime.today().weekday()]
                        tell(f"The time is {time} and today is {day}")
                    except Exception as e:
                        ex()

                elif 'greet' in qry:
                    greet()

                elif 'exit' in qry:
                    mixer.init()
                    mixer.music.load("audio2.mpeg")
                    tell(mixer.music.play())
                    i=1

                else:
                    try:
                        qry = qry.replace("wikipedia","")
                        results=wikipedia.summary(qry,sentences=2)
                        print(results)
                        tell("According to Wikipedia")  
                        tell(results)
                    except Exception as e:
                        ex()     
 
            except Exception as e:
                print(e)

# if la.j==0:
#     main()
# else:
#     pass
main()
