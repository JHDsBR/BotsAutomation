import random
from time import sleep
import requests
from constants import *
from random import sample
from time import sleep
import requests as rq
# from Session import BotSession

#! REVISADO
#! REVISADO
#! REVISADO

video_id = -1
comments_id = {}

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

def Request(session, url, method="GET", retry=10, body=None, headers=None):
    res = None
    for c in range(retry):
        try:
            if method.upper() == "POST":
                if body and not headers:
                    res = session.post(url, json=body)
                elif headers and not body: 
                    res = session.post(url, headers=headers)
                elif not headers and not body:
                    res = session.post(url)
                else:
                    res = session.post(url, json=body, headers=headers)
            else: 
                if body:
                    res = session.get(url, json=body)
                else:
                    res = session.get(url)
            break
        except Exception as e:
            print()
            print(e)
            print()
            pass
    
    return res
        

def Start(video_id_, BotSession):
    global video_id, comments_id
    video_id = str(video_id_)
    bots = rq.get(env["MY_API_URL"]).json()

    for b in bots:

        if(b["uploadVideo"] or b["cookieExpired"]):
            continue
        
        bot_session = BotSession(b["id"])
        if(bot_session.Like(video_id)[0]):
            print("Curti")
        else:
            print("N??o curti")
        sleep(TIME_BETWEEN_THE_LIKE_AND_COMMENT)
        comment_id = bot_session.Comment(video_id, COMMENT.GetRandom())
        
        if(comment_id):
            print("Comentei")
            comments_id[b["id"]] = comment_id
        else:
            print("N??o comentei")

        bot_session.Close()

        # sleep(TIME_BETWEEN_LIKE_AND_COMMENT_VIDEO)
    
    print("Start like comments")
    for b in bots:

        random_ids = GetRandomIds(exclude_id=b["id"])

        if(b["cookieExpired"]):
            continue
        
        bot_session = BotSession(b["id"])

        for _, post_id in random_ids:
            continue_ = True
            while True:
                ok, res = bot_session.Like(post_id)
                if ok:
                    print("Curti um coment??rio")
                    break
                elif "request frequently" in res.text.lower():
                    sleep(1.5)
                elif "vote power not enough" in res.text.lower():
                    continue_ = False
                    break
                else:
                    print("N??o curti um coment??rio")
                    break
            if continue_:
                sleep(TIME_BETWEEN_LIKES_ON_COMMENTS)
            else:
                break

        bot_session.Close()


    video_id = -1


def GetRandomIds(exclude_id):
    global video_id, comments_id
    
    comments_id_copy = comments_id.copy()
    
    try:
        del comments_id_copy[exclude_id]
    except:
        pass

    return sample(comments_id_copy.items(), MAX_LIKES_ON_COMMENTS if len(list(comments_id_copy.items())) > MAX_LIKES_ON_COMMENTS else len(list(comments_id_copy.items())))
    