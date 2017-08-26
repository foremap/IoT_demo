#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
import speech_recognition as sr

# Obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    # 监听一秒钟用于设定相关阈值
    r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)

print "trying to recognize ... "
print("Speech Recognition results:")
resultTmp = r.recognize_baidu(audio, app_key=config.APP_KEY, secret_key=config.SECRET_KEY)
# print resultTmp[u'alternative'], type(resultTmp[u'alternative'])
print resultTmp

# Test TTS
tts = sr.TTS(app_key=APP_KEY, secret_key=SECRET_KEY)
tts.say(resultTmp.encode("utf-8", "ignore"))
# tts.say("如同所有的事物充滿了我的靈魂，\
#         你從所有的事物中浮現，充滿了我的靈魂. \
#         你像我的靈魂，一隻夢的蝴蝶.你如同憂鬱這個字.\
#         我喜歡你是寂靜的，好像你已遠去.")
