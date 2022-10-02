
from http.client import IncompleteRead
from random import choice
from pytube import YouTube
from Utils import Request
from YoutubeAPI import Search

import requests
import wget
import zipfile
import os
import xmltodict

#! REVISADO
#! REVISADO
#! REVISADO

def Video() -> str:
    folder = "./Videos"
    video_name = "VIID.mp4"
    # while True:
    for c in range(5):
        try:
            try:
                print("baixando vídeo")
                YouTube(link).streams.filter(res="720p", file_extension='mp4').first().download(output_path=folder, filename=video_name)
                if os.path.isfile(f"{folder}/{video_name}"):
                    break
            except IncompleteRead as IR:
                print("download incompleto")
            a=1/0 #! erro proposital
        except:
            print("pegando novo link")
            v_title = None
            try:
                r = Search(choice(["meme brasil", "gato fofinho", "cachorro engraçado"]))
                print(r.text)
                r = r.json()
                print(r)
                items = choice(r["items"])
                v_id = items["id"]["videoId"]
                v_title = items["snippet"]["title"]
                link = f"https://www.youtube.com/watch?v={v_id}"
            except Exception as e:
                print("erro na hora de pegar um link ->", str(e))
    
    if not v_title:
        print("vídeo não baixado")
        return 

    print("vídeo baixado")
    return str(v_title)


def Driver(version=None) -> None:

    # get the latest chrome driver version number
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    # url = 'https://chromedriver.storage.googleapis.com/'
    # response = requests.get(url)
    response = Request(requests, url)

    # print(xmltodict.parse(response))
    # exit()
    if not response:
        return

    version_number = response.text

    if version:
        url = 'https://chromedriver.storage.googleapis.com/'
        response = Request(requests, url)

        data = xmltodict.parse(response.text)

        # print(str(data["ListBucketResult"]["Contents"])[:1000])
        for c in data["ListBucketResult"]["Contents"]:
            if str(version) in c["Key"] and "chromedriver_win32.zip" in c["Key"]:
                version_number = c["Key"].split("/")[0]

    # download_url = "https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_win32.zip"
    # download the zip file using the url built above

    # build the donwload url
    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

    latest_driver_zip = wget.download(download_url,'chromedriver.zip')


    # extract the zip file
    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall() # you can specify the destination folder path here
    # delete the zip file downloaded above
    os.remove(latest_driver_zip)
