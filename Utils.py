import random
from time import sleep
import requests

from constants import MY_API_URL

#! REVISADO
#! REVISADO
#! REVISADO

def Wait(minime=0, maxime=None):
    maxime = maxime if maxime else minime+random.random()*5
    sleep(minime+random.random()*(maxime-minime))


def Write(text:str, element, writeTime:float=3, timeDispersionBetweenWord:float=0.2):
    print("Write >>>")
    # print("---- Escrevendo",text)
    click_time = writeTime/len(text)
    for word in text:
        try:
            element.send_keys(word)
            sleep(click_time + random.random()*timeDispersionBetweenWord)
        except:
            pass
    print("Write <<<")


def GetBotToUploadVideo(randomly:bool=False):
    bots = requests.get(MY_API_URL).json()

    
    if(not randomly):
        for bot in bots:
            if bot["uploadVideo"]:
                if(bot["cookieExpired"]):
                    return GetBotToUploadVideo(True)
                return bot
    else:
        while True:
            if(len(bots) == 0):
                return 
            bot = random.choice(bots)
            if not bot["cookieExpired"]:
                return bot
            bots.remove(bot)
