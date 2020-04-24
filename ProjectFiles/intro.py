import pyttsx3
eng=pyttsx3.init()           # set synthesizer SAPI5
eng.setProperty('rate', 140) # setting up new property rate
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[2].id) # set female voice 
eng.say("Welcomes to you,")
eng.say("i am your vrtual assistant , Let's start,)
eng.runAndWait()
