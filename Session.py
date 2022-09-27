import requests as rq
import json
import datetime
from constants import API_URL
from os import environ as env

#! REVISADO
#! REVISADO
#! REVISADO

class BotSession():

    def __init__(self, id) -> None:
        self.id = id
        self.session = rq.Session()
        self.Login()


    def Login(self):
        
        res = self.session.get(f"{env['MY_API_URL']}/{self.id}")
        
        if(res.status_code != 200):
            return False

        for cok in json.loads(res.json()["cookie"]):
            self.session.cookies.set(cok["name"], cok["value"], domain=env["DOMINIO"])
        
        # é bom implementar uma verificação de login bem sucedido
        

    # necessário fazer login antes
    def GetTokenCSRF(self):
        try:
            return self.session.get(env["URL_API_TOKEN"]).json()["data"]["token"]
        except:
            return ""


    def GetAuth(self, body):
        return rq.get(env["URL_API_AUTH"], json=body).json()


    def Like(self, post_id:str):
        id = post_id

        t = int(datetime.datetime.now().timestamp())

        body = {
            "post_id":id,
            "timestamp":t
        }

        headers = self.Headers(body)
        # return
 
        
        res = self.session.post(API_URL.LIKE, json=body, headers=headers)
        
        # print(res.text)
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
        res = self.session.post(API_URL.COMMENT, json=body, headers=headers)
        
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

