import subprocess
import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
from plyer import notification
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import shutil
import pyjokes
import winshell
import ctypes
import time
import requests
from googlesearch import search
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def notifyMe(message):
    notification.notify(
        message = message,
        app_icon = None,
        timeout=10
    )




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("Hello! I am Laura.")
    print("Hello! I am Laura.")

def usrname():
    speak("What should i call you?")
    print("What should i call you?")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    print("Welcome ", uname)
    speak("How can i Help you?")
 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 
    except Exception as e: 
        print("Say that again please...") 
        return "None" 
    return query

def coro():
    speak("Which Country")
    print("Which Country")
    country = takeCommand()
    url="https://www.worldometers.info/coronavirus/country/{}/".format(country)
    r=requests.get(url)
    s=BeautifulSoup(r.text, "html.parser")
    data=s.find_all("div",class_="maincounter-number")
    print("Total Cases : ",data[0].text.strip())
    speak("Total Cases : ")
    speak(data[0].text.strip())
    print("Total Deaths : ",data[1].text.strip())
    speak("Total Deaths : ")
    speak(data[1].text.strip())
    print("Total Recovered : ",data[2].text.strip())
    speak("Total Recovered : ")
    speak(data[2].text.strip())

	
if __name__=="__main__" :
    wishMe()
    usrname()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'weather' in query:
            webbrowser.open("https://www.google.com/search?q=wather&oq=wather&aqs=chrome..69i57j0i10i131i433l2j0i10i433j0i10i131i433i457j0i402l2j0i10i131i433l3.1502j0j4&sourceid=chrome&ie=UTF-8")   
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stack overflow' in query :
            speak("Here you go to Stack Over flow. Happy coding!!")
            print("Here you go to Stack Over flow. Happy coding!!")
            webbrowser.open("stackoverflow.com")   
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Mokshada\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")

        

        elif 'open visual studio' in query:
            codePath = "C:\\Program Files (x86)\Microsoft Visual Studio\\2017\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)

        elif 'open r studio' in query:
            codePath = "C:\\Program Files\\RStudio\\bin\\rstudio.exe"
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            print("I am fine, Thank you")
            speak("How are you")
            print("How are you")

 
        elif 'fine' in query or 'good' in query:
            speak("It's good to know that you are fine")
            print("It's good to know that you are fine")

        elif 'change my name to' in query:
            query = query.replace("change my name to", "")
            uname = query
            speak("welcome")
            speak(uname)
            print("Welcome" + uname)

        elif 'what is your name' in query:
            speak("My friends call me laura")
            print("My friends call me laura")
            
        elif 'Gmail' in query:
            webbrowser.open("gmail.com")

        elif 'bye' in query:
            speak("Bye! Take Care")
            speak("Stay Home, Stay Safe")
            print("Bye! Take Care")
            print("Stay Home, Stay Safe")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            speak("Stay Home and Stay Safe")
            print("Thanks for giving me your time")
            print("Stay Home and Stay Safe")
            exit()

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculator" in query: 
             webbrowser.open("https://www.google.com/search?q=calculator&oq=cal&aqs=chrome.1.69i57j0i131i433j0i433j0j0i433j69i60l2j69i61.2772j0j7&sourceid=chrome&ie=UTF-8")


        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
 
        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif 'restart' in query:
            subprocess.call(["shutdown", "/r"])
             
        elif 'hibernate' in query or 'sleep' in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif 'log off' in query or 'sign out' in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
        
        elif 'news' in query:
             webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

        elif 'show to do list' in query:
            speak("Showing Notes")
            file = open("laura.txt", "r") 
            print(file.read())
            speak(file.read())

        elif 'laura' in query:
            speak("Laura in your service!!")
            print("Laura in your service!!")

 
        elif 'who are you' in query:
            speak("I am your virtual assistant laura")
            print("I am your virtual assistant laura")
 
        elif 'reasons for you' in query:
            speak("I was created as a Minor project")
            print("I was created as a Minor project")

        elif 'who i am' in query:
            speak("If you talk then definately your human.")
            print("If you talk then definately your human.")

        elif 'search' in query or 'play' in query: 
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query) 


        elif 'Corona' or 'Covid' in query:
            coro()
            message="Corona cases increasing rapidly so stay home , stay safe"
            notifyMe(message)
            time.sleep(2)

            
            
       
