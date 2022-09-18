from ast import Raise
import os
from constants import *
from Driver import *
import Notify
from Utils import *

#! REVISADO
#! REVISADO
#! REVISADO

lastVideoUploaded = {}
ACCOUNT_NAME = ""

def StartUploadVideo(title, bot):
    global lastVideoUploaded, ACCOUNT_NAME
    
    try:
        print("Publicando video")
        print(1)
        ACCOUNT_NAME = bot["usuario"]
        print(2)
        COOKIE = bot["cookie"]
        print(3)
        driver = CreateDriver()
        print(4)
        if(not Login(driver, COOKIE)):
            Raise("Não fez login")
        print(5)
        UpVideo(driver)
        print(6)
        SetTitle(driver, title)
        print(7)
        SetTags(driver)
        print(8)
        WaitProgress(driver)
        print(9)
        if(lastVideoUploaded["progress"] == 100):
            if(SetThumb(driver)):
                if(UploadButton(driver)):
                    GetLastVideoLink(driver)
                    idd = GetVideoID()
                    WaitApprove(driver)
                    return [idd, lastVideoUploaded['link']]
    except Exception as e:
        Notify.SendEmail("UPLOAD VIDEO ERROR", str(e))
        print("Erro na hora de publica o vídeo. Tentando de novo")

def WaitApprove(driver):
    print("WaitApprove >>>")
    while(True):
        try:
            LoadPage(URL.MY_VIDEOS, driver)
            WaitLoad(driver)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_ELEMENT.APPROVED)))
            Wait(10,20)
        except:
            print("---- Vídeo aprovado")
            print("WaitApprove <<<")
            return


def GetVideoID():  
    global lastVideoUploaded  
    return lastVideoUploaded["link"].split("/")[-1]


def GetLastVideoLink(driver):    
    global lastVideoUploaded  
    WaitLoad(driver)  
    print("GetLastVideoLink >>>")
    LoadPage(URL.MY_VIDEOS, driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_ELEMENT.LAST_VIDEO_THUMB))).click()
    WaitLoad(driver)
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    lastVideoUploaded["link"] = driver.current_url        
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("GetLastVideoLink <<<")


def UploadButton(driver):
    print("UploadButton >>>")
    global ACCOUNT_NAME
    Wait(1, 2.5)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_ELEMENT.SEND_VIDEO_BUTTON))).click()

    try:
        alert_text = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_ELEMENT.UPLOAD_SUCCESS))).text
        # print("------------->",("Envio concluído!" in str(alert_text)))
        # print("UploadButton <<<")
        Wait(4, 5)
        # return True
        return "upload completed" in str(alert_text).lower()
    except Exception as e: 
        Notify.SendEmail("NO RESISTENCE", f"{ACCOUNT_NAME} acabou de tentar postar um vídeo mas não conseguiu :(")
        print("---- Não conseguiu postar, provavelmente está sem energia")
        # print("Deu erro na hora de verificar o popup ->",str(e))
    print("UploadButton 2 <<<")
    return False


def WaitLoadThumbs(driver):
    print("WaitLoadThumbs >>>")
    Wait(3, 5)
    count = 0
    while(True):
        try:
            WebDriverWait(driver, 2.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_ELEMENT.THUMB_LOADING)))
            Wait(4, 5)
            count += 1
            if(count >= 20):
                print("---- Não carregou")
                print("WaitLoadThumbs <<<")
                return False
                
        except:
            Wait(1, 3)
            print("---- Thumbs carregadas")
            print("WaitLoadThumbs <<<")
            return True


def UpVideo(driver):
    print("UpVideo >>>")
    # Wait(1, 2)
    title = "VIID"
    # if(not title):
    #     print("---- Não baixou o vídeo, usando vídeo do backup")
    #     title = 'VIID'
    LoadPage(URL.SITE_UPLOAD, driver)
    Wait(0.5, 1)
    inp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_ELEMENT.UPLOAD_INPUT)))
    dir_path = os.path.dirname(os.path.realpath("Videos\VIID.mp4"))
    # print(dir_path)
    path = dir_path+"\\VIID.mp4"
    # print(path)
    print(os.path.isfile(path))
    inp.send_keys(path)
    print("UpVideo <<<")


def WaitProgress(driver):
    print("WaitProgress >>>")
    Wait(1, 2)
    global lastVideoUploaded
    prog = ""
    count = 0
    while(prog != "100%"):
        try:
            prog = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_ELEMENT.UPLOAD_PROGRESS))).text
            print("---- Progress ->",prog)
            if("%" in prog and len(prog) > 1):
                lastVideoUploaded["progress"] = int(prog[:-1])
            else:
                sleep(1)
                lastVideoUploaded["progress"] = 0
                count += 1
                if(count > 20):
                    break
        except:
            pass
    
    print("WaitProgress <<<")


def SetThumb(driver):
    print("SetThumb >>>")
    if(not WaitLoadThumbs(driver)):
        return False
    Wait(2, 3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_ELEMENT.VIDEO_THUMB))).click()
    print("SetThumb <<<")
    return True


def SetTitle(driver, title:str=None):
    print("SetTitle >>>")
    global lastVideoUploaded
    Wait(0.5, 1)
    lastVideoUploaded["title"] = title
    # print("---- Título do vídeo ->", title)
    Write(title, WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_ELEMENT.VIDEO_TITLE))))
    print("SetTitle <<<")


def SetTags(driver):
    print("SetTags >>>")
    Wait(1, 2)
    elems = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.tags > span.item")))
    # Wait(1, 2)
    for elem in reversed(elems[:3]):
        elem.click()
        Wait(0.5, 1.5)
    print("SetTags <<<")


