import pyttsx3
import datetime
import os
import speech_recognition as sr
import wikipedia
import random
import requests
import webbrowser
#YOU'VE TO CHANGE THE USER PROFILE OF WINDOWS, AND ADD APIKEY FROM WEATHERAPI.
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour=int(datetime.datetime.now().hour)
    
    if hour <12:
        speak("Good Morning Hacker!")
    elif hour>11 and hour<17 :
        speak("Good Afternoon Hacker!")
    else:
        speak("Good Evening Hacker!")
    speak("I am your Friend ....so How may i Help u?")
def takecommand():
    ''' I'm taking Commands
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... ")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognizing... ")
            query=r.recognize_google(audio,language="en-in")
            print(f"As u Said: {query}")
            speak("Working On it Bro!")

        except Exception as e:
            print(e)
            print("-_- An Error Reape at Plz")
            return "None"
        return query
def gettingsingleinput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... ")
        r.pause_threshold=1
        audio=r.listen(source)
        query=r.recognize_google(audio,language="en-in")
    return query
def get_weather(state):
    api_key = "key"  # Replace "YOUR_API_KEY" with your actual API key
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": state
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if 'error' in data:
        speak("Sorry, I couldn't fetch the weather information at the moment.")
    else:
        current = data['current']
        temperature = current['temp_c']
        condition = current['condition']['text']
        speak(f"The current temperature in {state} is {temperature} degrees Celsius with {condition}.")
        print(f"The current temperature in {state} is {temperature} degrees Celsius with {condition}.")
def get_news(category):
    api_key = "key"  # Replace "YOUR_API_KEY" with your actual API key
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "category": category
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    articles = data.get('articles', [])
    if not articles:
        speak("Sorry, I couldn't fetch the news at the moment.")
    else:
        news_list = []
        for article in articles:
            title = article['title']
            news_list.append(title)
        speak(news_list)

if __name__=="__main__":
    wish()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching WikiPedia....")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=3)
            speak("According To WikiPedia")
            print("Here's What I found on Wikipedia Results: ",results)
            speak(results)
        elif 'open youtube' in query:
            speak('Opening Youtube')
            speak("What u wanna Search")
            n=input()
            speak('ok opening Bro!')
            webbrowser.open('https://www.youtube.com/results?search_query='+n)
        elif 'bye' in query:
            speak("I am Now Logging Off Nice to work With u Hope u Will Come Again Cause , I'm your Only Friend")
            break
        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open('google.com')
        elif 'open discord' in query:
            speak('Opening Discord')
            webbrowser.open('discord.com')
        elif 'play music' in query:
            music="C:\\Users\\HP\\Desktop\\songs"
            song=os.listdir(music)
            n=random.randint(0,len(song)-1)
            speak('Playing Random Song From your Playlist')
            os.startfile(os.path.join(music,song[n]))
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Bruhh! The Time is {strtime}")
        elif 'weather' in query:
            speak('Speak the state') 
            n=gettingsingleinput()
            get_weather(n)
        elif 'news' in query:
            speak('whats the topic')
            m=gettingsingleinput()
            get_news(m)
    
