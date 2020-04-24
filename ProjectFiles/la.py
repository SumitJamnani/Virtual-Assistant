import pyttsx3
import speech_recognition as sr
import winsound

engine=pyttsx3.init()               # set synthesizer SAPI5
engine.setProperty('rate', 180)     # setting up new property rate  
j=0
r=sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say("Hey, kem cho, my name is Elja")
engine.runAndWait()
engine.say("i am your virtual assistant...")
engine.runAndWait()
engine.say("may i know your good name...")
engine.runAndWait()
with sr.Microphone() as source:
                print("Listening...",end="\n\n")
                audio=r.listen(source,timeout=5)
                text = r.recognize_google(audio)
                print(f"You said : {text}")
                if 'Narendra Modi' in text:
                    engine.say("Access granted, Saheeb, tamnee thoodi rookay")
                    engine.runAndWait()
                    j= 0
                elif 'Rahul Gandhi' in text:
                    engine.say("i am Elja, not sonia gandhi")
                    engine.runAndWait()
                    engine.say("HA HA HA HA HA HA HA. its a, joke, please dont get offended")
                    engine.runAndWait()
                    j= 1
                else:
                    engine.say("Access denied")
                    engine.runAndWait()
                    for i in range(5):        
                        winsound.Beep(2500, 500)
                    j= 1
