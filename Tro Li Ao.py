from datetime import date, datetime
import speech_recognition 
import pyttsx3
import playsound
from gtts import gTTS
import wikipedia
import time
import os
import webbrowser
import pyaudio
# from countdown import countdown

robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[1].id)
robot_mouth.setProperty('rate', 180)



def wiki(keyword):
    try:
        print("searching on wiki...")
        print(wikipedia.summary(keyword))
    except:
        print("can't open")
        print('')
    run= False    



robot_brain="hi, my name is Deli. What can i help you?"
print("Robot: " + robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()




robot_ear = speech_recognition.Recognizer()
robot_brain = ""




while True:
    with speech_recognition.Microphone() as mic:
        audio = robot_ear.record(mic, duration= 3)
        robot_ear.adjust_for_ambient_noise(mic)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except: 
        you =""
        

    print("You: " + you) 

    if you =="":
        robot_brain ="I can't hear you say anything, please try again sir"
        
    elif you == "hello":
        robot_brain ="hello Duy"   
        
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%d/%m/%Y")
    elif 'YouTube' in you:
        webbrowser.open('https://www.youtube.com/',new=1)
        robot_brain="ok opening youtube" 
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        time.sleep(10)    
            
    elif 'YouTube music' in you:
        webbrowser.open('https://www.youtube.com/watch?v=09R8_2nJtjg&list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA&start_radio=1',new=1)
        robot_brain="ok opening youtube music" 
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        time.sleep(10)
    elif 'EDM' in you:
        webbrowser.open('https://www.youtube.com/watch?v=uryVw968ZMM',new=1)
        robot_brain="ok opening edm music" 
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        time.sleep(10)
    elif 'Google' in you:
        webbrowser.open('https://www.google.com.vn/?hl=vi',new=1)
        robot_brain="ok opening google" 
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        time.sleep(10)
    elif 'bowlero' in you:
        webbrowser.open("https://www.youtube.com/watch?v=enWquTrqYTc",new=1)
        robot_brain="ok opening bolero"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        time.sleep(10)
    elif 'Facebook' in you:
        webbrowser.open("https://www.facebook.com/",new=1)
        robot_brain="ok opening Facebook"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        time.sleep(10)
    elif 'mail' in you:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox",new=1)
        robot_brain="ok opening Gmail"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        time.sleep(10)
    elif 'movie' in you:
        webbrowser.open("http://www.phimmoizz.net/",new=1)
        robot_brain="ok opening movie"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        time.sleep(10)    
    elif 'girlfriend' in you:
        webbrowser.open("https://www.facebook.com/profile.php?id=100031843731176",new=1)
        robot_brain="opening Trang Facebook"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        time.sleep(10)



    elif 'shut down' in you:
        os.system('shutdown -s')
    elif 'restart' in you:
        os.system('shutdown -r')

    elif 'time' in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    # elif("countdown" in you):
    #     timecount=you.replace("countdown","")
    #     timecount = timecount.replace('minutes',"")
    #     counter=countdown(int(timecount))
    #     robot_brain=counter
    #     while time > 0:
    #         time = time - 1
    #         seconds = (time // 60) % 60
    #         minutes = (time // 3600)
    #         print('Time Left -+==> ',':',minutes,':',seconds,)
    #         os.system("CLS")
       

        


    elif you == "no":
        robot_brain = "bye Duy"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break    
        
    
            
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    robot_brain = "Any things else?"
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()