import pyttsx3 

engine = pyttsx3.init()

# engine.say("pyttsx3 it is used to convert text to speech")
engine.runAndWait()

import datetime

engine = pyttsx3.init()
 
def speak(text):
    engine.say(text)
    engine.runAndWait()



    
def time():
    Time= datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is: ")
    speak(Time)

time()

def date():
    year=int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print(date)
    print(month)
    print(year)
date()

def greeting():
    hour = datetime.datetime.now().hour
    if hour>= 6 and hour <12:
        speak("good morning ma'am")
    elif hour>= 12 and hour <18:
        speak("good afternoon ma'am")
    elif hour >= 18 and hour < 24:
        speak("good evening ma'am!")
    else:
        speak("Good night ma'am")

greeting()

def wishme():
    speak("Welcome back ma'am!")
    time()
    date()
    greeting()
    speak("Jarvis at your service, please tell me how i can help you?")

wishme()

while True:
    text = input("Enter some text to convert into speech")
    speak(text)