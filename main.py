import loadEnv

from random import sample
from constants import *
from time import sleep
from UploadVideo import StartUploadVideo
from Session import BotSession
import Download
import Utils
import Notify
import requests as rq

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

# upload do vídeo
uploaded = False
while not uploaded:

    # pega um bot
    bot = Utils.GetBotToUploadVideo(randomly=True)
    if not bot:
        Notify.SendEmail("BOT NOT FOUND", "Não foi possível encontrar um bot para fazer o upload do vídeo.")
        exit()

    rq.post(MY_API_URL_UPDATE, json={"id":int(bot['id'])})
    # fica tentando postar o vídeo até conseguir
    uploaded = StartUploadVideo(bot=bot,title=title)

Notify.SendEmail("VIDEO UPLOADED", uploaded[1])



video_id = -1
comments_id = {}

def Start(video_id_):
    global video_id, comments_id
    video_id = str(video_id_)
    bots = rq.get(env["MY_API_URL"]).json()

    for b in bots:

        if(b["uploadVideo"] or b["cookieExpired"]):
            continue
        
        bot_session = BotSession(b["id"])
        if(bot_session.Like(video_id)):
            print("Curti")
        else:
            print("Não curti")
        sleep(TIME_BETWEEN_THE_LIKE_AND_COMMENT)
        comment_id = bot_session.Comment(video_id, COMMENT.GetRandom())
        
        if(comment_id):
            print("Comentei")
            comments_id[b["id"]] = comment_id
        else:
            print("Não comentei")

        bot_session.Close()

        sleep(TIME_BETWEEN_LIKE_AND_COMMENT_VIDEO)
    
    print("Start like comments")
    for b in bots:

        random_ids = GetRandomIds(exclude_id=b["id"])

        if(b["cookieExpired"]):
            continue
        
        bot_session = BotSession(b["id"])

        for _, post_id in random_ids:
            if(bot_session.Like(post_id)):
                print("Curti um comentário")
                sleep(TIME_BETWEEN_LIKES_ON_COMMENTS)
            else:
                print("Não curti um comentário")

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
    
