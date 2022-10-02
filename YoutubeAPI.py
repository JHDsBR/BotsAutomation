import requests as rq
from Utils import Request
from constants import MY_YT_API_KEY

#! REVISADO
#! REVISADO
#! REVISADO

def Search(search):
    r = rq.get(f"https://youtube.googleapis.com/youtube/v3/search?relevanceLanguage=pt&part=snippet&order=date&q={'%'.join(search.split())}&key={MY_YT_API_KEY}")
    # r = Request(rq, f"https://youtube.googleapis.com/youtube/v3/search?relevanceLanguage=pt&part=snippet&order=date&q={'%'.join(search.split())}&key={MY_YT_API_KEY}")
    return r