#!/usr/bin/env python
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

APP_KEY="WTMpWBYjN4DUgKqycABcdECD"
SECRET_KEY="f10f8ffe9e6332b1964e52b0408cb27e"
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Baidu thinks you said " + r.recognize_baidu(audio, app_key=APP_KEY, secret_key=SECRET_KEY))
except sr.UnknownValueError:
    print("Baidu could not understand audio")
except sr.RequestError as e:
    print("Baidu error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='cmn-Hans-CN'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))