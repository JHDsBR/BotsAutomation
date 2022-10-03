# import loadEnv

from random import sample
from constants import *
from time import sleep
from UploadVideo import StartUploadVideo
import Download
import Utils
import Notify
import requests as rq
from Session import BotSession
import Driver as Driver_

#! REVISADO
#! REVISADO
#! REVISADO

# download do chromedriver
for c in range(20):
    try:
        Download.Driver(version)
        
        # testar o driver
        d = Driver_.CreateDriver()
        d.get("https://www.google.com/")
        d.quit()
        
        break
    except Exception as e:
        version = None
        if "version of ChromeDriver only supports Chrome version" in str(e):
            print("Deu erro de versão")
            for c in str(e).split():
                print(c)
                print(c.count("."))
                if c.count(".") >= 2:
                    version = c.split(".")[0]
                    print(version)
                    break
        else:
            print("Não deu erro de versão")
            sleep(10)

# download do vídeo
title = Download.Video()

if not title:
    exit()

# upload do vídeo
uploaded = False
while not uploaded:

    # pega um bot
    bot = Utils.GetBotToUploadVideo(randomly=True)
    if not bot:
        Notify.SendEmail("BOT NOT FOUND", "Não foi possível encontrar um bot para fazer o upload do vídeo.")
        exit()

    # rq.post(MY_API_URL_UPDATE, json={"id":int(bot['id'])})        
    Utils.Request(rq, MY_API_URL_UPDATE, "POST", body={"id":int(bot['id'])})

    # fica tentando postar o vídeo até conseguir
    uploaded = StartUploadVideo(bot=bot,title=title)

Notify.SendEmail("VIDEO UPLOADED", uploaded[1])

Utils.Start(uploaded[0], BotSession)



