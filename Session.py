# import loadEnv
import requests as rq
import json
import datetime
from constants import API_URL
from os import environ as env
from Utils import Request

#! REVISADO
#! REVISADO
#! REVISADO

class BotSession():

    def __init__(self, id) -> None:
        self.id = id
        self.session = rq.Session()
        self.Login()


    def Login(self):
        
        res = Request(self.session, f"{env['MY_API_URL']}/{self.id}")

        if not res:
            return False

        if res.status_code != 200:
            return False

        for cok in json.loads(res.json()["cookie"]):
            self.session.cookies.set(cok["name"], cok["value"], domain=env["DOMINIO"])

        
        # é bom implementar uma verificação de login bem sucedido
        

    # necessário fazer login antes
    def GetTokenCSRF(self):
        data = Request(self.session, env["URL_API_TOKEN"])

        try:
            return data.json()["data"]["token"]
        except Exception as e:
            print("Error ->", e)
            return ""


    def GetAuth(self, body):
        data = Request(rq, env["URL_API_AUTH"], body=body)
        
        if not data:
            return ""
        
        return data.json()


    def Like(self, post_id:str):
        id = post_id

        t = int(datetime.datetime.now().timestamp())

        body = {
            "post_id":id,
            "timestamp":t
        }

        headers = self.Headers(body)
        # return
 
        
        # res = self.session.post(API_URL.LIKE, json=body, headers=headers)
        
        res = Request(self.session, API_URL.LIKE, "POST", body=body, headers=headers)
        # print(res.text)
        if not res:
            return False, res
        ok = "success" in res.text.lower()
        if not ok:
            print(res.text)
        return ok, res
    


    def Comment(self, post_id, comment):
        id = post_id

        t = int(datetime.datetime.now().timestamp())

        body = {
            "post_id":id,
            "comment_content":comment,
            "timestamp":t
        }

        headers = self.Headers(body)
        # return
        # res = self.session.post(API_URL.COMMENT, json=body, headers=headers)
        res = Request(self.session, API_URL.COMMENT, "POST", body=body, headers=headers)
        
        if not res:
            return
        # print(res.text)

        if("success" in res.text.lower()):
            return res.json()["data"]["replyid"]

    def Headers(self, body):

        return {
            "X-Xsrf-Token":self.GetTokenCSRF(), 
            "Authorization":self.GetAuth(body)
        }

    def Close(self):
        self.session.close()


