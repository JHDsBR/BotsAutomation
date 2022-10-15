import loadEnv
import requests as rq
from os import environ as env
import Notify

countOfCookiesExpired = 0

try:
    bots = rq.get(env["MY_API_URL"]).json()

    for bot in bots:
        if bot["cookieExpired"]:
            countOfCookiesExpired += 1

    if countOfCookiesExpired != 0:
        Notify.SendEmail("UPDATE COOKIES", 
            f"Há {countOfCookiesExpired} {'Cookies para serem atualizados' if countOfCookiesExpired != 1 else 'Cookie para ser atualizado'}")
except Exception as e:
    Notify.SendEmail("ERROR UPDATE COOKIES", e) 