#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import requests
import config1 as config

try:
    # Obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        while True:
            # 监听一秒钟用于设定相关阈值
            print("Say something!")
            audio = r.listen(source)

            print "trying to recognize ... "
            print("Speech Recognition results:")
            resultTmp = ""
            try:
                resultTmp = r.recognize_baidu(audio, app_key=config.APP_KEY, secret_key=config.SECRET_KEY)
            except Exception:
                continue

            # print resultTmp[u'alternative'], type(resultTmp[u'alternative'])
            print resultTmp
            userQ = resultTmp.encode("utf-8", "ignore").replace("，", " ").strip()
            # Call OpenAPI
            openAPI = "http://idc.emotibot.com/api/ApiKey/openapi.php?appid=82c7dab9ad508ea06b781129b956496e&cmd=chat&userid=demo_1&text={0}&location="
            result = requests.get(openAPI.format(userQ)).json()
            try :
                for textBlob in result["data"]:
                    text = textBlob["value"]
                    print text
                    if text:
                        tts = sr.TTS(app_key=config.APP_KEY, secret_key=config.SECRET_KEY)
                        tts.say(text.encode("utf-8", "ignore"), per=1)
            except Exception:
                continue

except KeyboardInterrupt:
    pass


# Test TTS
# tts = sr.TTS(app_key=config.APP_KEY, secret_key=config.SECRET_KEY)
# tts.say(resultTmp.encode("utf-8", "ignore"))
# tts.say("如同所有的事物充滿了我的靈魂，\
#         你從所有的事物中浮現，充滿了我的靈魂. \
#         你像我的靈魂，一隻夢的蝴蝶.你如同憂鬱這個字.\
#         我喜歡你是寂靜的，好像你已遠去.")
