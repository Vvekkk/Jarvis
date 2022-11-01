# Jarvis
# JARVIS- AI Desktop Voice Assistant
I have developed a python program to get some general task done. It takes voice input and can do some general tasks like google assistant. We have used python built-in modules and library for this, some are -

from re import S
from time import struct_time
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia                            
import webbrowser                           
import os   #for music

# External Modules required:

pyttsx3 --> For speaking ability.
SpeechRecognition --> For listening ability.
wikipedia --> To search through the wikipedia for the query.
pyaudio --> Dependency for speech recognition module.

# Solving issues
If you are unable to install pyaudio, type the following commands:
pip install pipwin

pipwin install pyaudio

It should work now.
