from re import S
from time import struct_time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia  # "python.linting.pylintArgs",
import webbrowser  # "--disable=C0303"
import os  # for music


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):  
    engine.say(audio)
    engine.runAndWait()


def wishme():  
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        speak("I'am Jarvis. Thy wish is mine own hest ")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
        speak("I'am Jarvis. Thy wish is mine own hest ")

    else:
        speak("Good evening!")
        speak("I'am Jarvis. Thy wish is mine own hest ")


def takeCommand(): 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
       
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")  
        query = r.recognize_google(audio, language='en-in')

        print(f"User said: {query}\n")

    except Exception as e:
       

        print("Say that again please...")
        return "None"  
    return query


if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "D:\\VSC\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'quit' in query:
            speak(' Adios !')
            exit()
