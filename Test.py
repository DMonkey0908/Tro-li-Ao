import time
import os

minute = int(input())
second = int
time = minute*3600 + second*60
print('{}:{}'.format(minute,second))
while time > 0:
    time = time - 1
    seconds = (time // 60) % 60
    minutes = (time // 3600)
    print('Time Left -+==> ',':',minutes,':',seconds,)
    os.system("CLS")
if time == 0:
    print('Time Is Over!') 
    elif you == "countdown":
        if "minutes" in you:
            cd= sr.Recognizer()
            with sr.Microphone() as source:
                audio = cd.record(source, timeout=5, phrase_time_limit=5)
            try:
                minutes = cd.recognize_google(audio)
            except:
                minutes=""        
            
            minute = int(input(cd))
            time = minute*3600 + second*60
            print('{}:{}'.format(minute,second))
            while time > 0:
                time = time - 1
                int(seconds) = (time // 60) % 60
                minutes = (time // 3600)
                print('Time Left -+==> ',':',minutes,':',seconds,)
                os.system("CLS")
            if time == 0:
            print('Time Is Over!')
