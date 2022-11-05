# Jarvis AI Desktop Voice Assistant
- This is my project. It will do daily tasks like Open Google, Open YouTube, Open VSCode, play music with the help of a single voice command.
- JARVIS full form is Just A Rather Very Intelligent System.
- It takes voice input and can do some general tasks like google assistant. I have used python built-in modules and library for this, some are -

- from re import S
- from time import struct_time
- import pyttsx3
- import speech_recognition as sr 
- import datetime
- import wikipedia
- import webbrowser
- import os   #for music

## What can Jarvis AI assistant do for you?
- It will greet as soon as you run the code according to the time.
- It can do Wikipedia searches for you.
- It is capable of opening websites like Google, Youtube, etc., in a web browser.
- It is capable of opening your code editor or IDE with a single voice command.
- It also tells the current time.
- It can also play music.

## Jarvis External Modules required:

    pyttsx3 --> For speaking ability.
    SpeechRecognition --> For listening ability.
    wikipedia --> To search through the wikipedia for the query.
    pyaudio --> Dependency for speech recognition module.

## Solving issues
If you are unable to install pyaudio, type the following commands:
pip install pipwin

    pipwin install pyaudio

It should work now. 
# NOTE JARVIS  REQUIRES INTERNET CONNECTION!

Let's start understaing our own JARVIS.

## Defining Speak Function
The first and foremost thing for an A.I. assistant is that it should be able to speak. To make our JARVIS talk, we will make a function called speak(). This function will take audio as an argument, and then it will pronounce it.

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
Now, the next thing we need is audio. We must supply audio so that we can pronounce it using the speak() function we made. We are going to install a module called pyttsx3.

    pip install pyttsx3
    import pyttsx3
After successfully installing pyttsx3, import this module into your program.

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

What is pyttsx3?

A python library that will help us to convert text to speech. In short, it is a text-to-speech library.

What is sapi5?
- Microsoft developed speech API.
- Helps in synthesis and recognition of voice.

What Is VoiceId?
- Voice id helps us to select different voices.
- voice[0].id = Male voice 
- voice[1].id = Female voice

## Defining Wish me Function :

Now, we will make a wishme() function that will make our JARVIS. wish or greet the user according to the time of computer or pc. To provide current or live time to A.I., we need to import a module called datetime. Import this module to your program by:

    import datetime
Now, let's start defining the wishme() function:

    def WishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon")
        else:
            speak("Good Evening")
        speak("I am Jarvis AI, Please tell me how may I help you")

## Defining Take command Function :
The next most important thing for our A.I. assistant is that it should take command with the help of the microphone of the user's system. So, now we will make a takeCommand() function.  With the help of the takeCommand() function, our A.I. assistant will return a string output by taking microphone input from the user.

 Before defining the takeCommand() function, we need to install a module called speechRecognition. Install this module by:

    pip install speechRecognition
After successfully installing this module, import this module into the program by writing an import statement.

    import speechRecognition as sr
Code

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
 
## Creating Our main() function: 
We will create a main() function, and inside this main() Function, we will call our speak function.

Code:

    if __name__=="__main__" :

## Coding logic of Jarvis

 Now, we will develop logic for different commands such as Wikipedia searches, playing music, etc.

## Defining Task 1 : To search something on Wikipedia 
 To do Wikipedia searches, we need to install and import the Wikipedia module into our program. Type the below command to install the Wikipedia module :

    pip install wikipedia
After successfully installing the Wikipedia module, import it into the program by writing an import statement.

    if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() 

        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

## Defining Task 2 : To open YouTube site in a web-browser
To open any website, we need to import a module called webbrowser. It is an in-built module,

Code

    elif 'open youtube' in query:
            webbrowser.open("youtube.com")

## Defining Task 3 : To know the current time
We are using the datetime() function and storing the current or live system time into a variable called strTime. After storing the time in strTime, we are passing this variable as an argument in speak function. Now, the time string will be converted into speech.

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        print(f"Sir, the time is {strTime}") 
        speak(f"Sir, the time is {strTime}")

## Defining Task 4 : To open the VS Code Program
To open the VS Code or any other application, we need the code path of the application.

    elif 'open code' in query:
        vsPath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsPath)

## Defining Task 5 : To End Jarvis 
To End the Jarvis

    elif 'quit' in query:
        exit(0)
## Recapitulate
- First of all, we have created a wishme() function that gives the greeting functionality according to our A.I system time.
- After wishme() function, we have created a takeCommand() function, which helps our A.I to take command from the user. This function is also responsible for returning the user's query in a string format.
- We developed the code logic for opening different websites like google, youtube, and stack overflow.
- Developed code logic for opening VS Code or any other application.

## Is it an A.I.?
Many people will argue that the virtual assistant that we have created is not an A.I, but it is the output of a bunch of the statement. But, if we look at the fundamental level, the sole purpose of A.I developed machine is that it can perform human tasks with the same effectiveness or even more effectively than humans.

It is a fact that our virtual assistant is not a very good example of A.I., but it is an A.I.!

## The E.N.D.
With this, you have successfully made your very first virtual assistant. I hope you all have liked this.
