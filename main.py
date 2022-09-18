import loadEnv

from constants import MY_API_URL_UPDATE
from time import sleep
from UploadVideo import StartUploadVideo
import Download
import Utils
import Notify
import requests

#! REVISADO
#! REVISADO
#! REVISADO

# download do chromedriver
for c in range(20):
    try:
        Download.Driver()
        break
    except:
        sleep(60)

# download do vídeo
title = Download.Video()

# pega um bot
bot = Utils.GetBotToUploadVideo(randomly=True)
if not bot:
    Notify.SendEmail("BOT NOT FOUND", "Não foi possível encontrar um bot para fazer o upload do vídeo.")
    exit()

requests.post(MY_API_URL_UPDATE, json={"id":int(bot['id']), "newData":{"uploadVideo":True}})

# upload do vídeo
uploaded = False
while not uploaded:
    # fica tentando postar o vídeo até conseguir
    uploaded = StartUploadVideo(bot=bot,title=title)

Notify.SendEmail("VIDEO UPLOADED", uploaded[1])