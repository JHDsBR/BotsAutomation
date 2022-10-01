
from http.client import IncompleteRead
from random import choice
from pytube import YouTube
from YoutubeAPI import Search

import requests
import wget
import zipfile
import os

#! REVISADO
#! REVISADO
#! REVISADO

def Video() -> str:
    folder = "./Videos"
    video_name = "VIID.mp4"
    while True:
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
            try:
                r = Search(choice(["meme brasil", "gato fofinho", "cachorro engraçado"]))
                r = r.json()
                items = choice(r["items"])
                v_id = items["id"]["videoId"]
                v_title = items["snippet"]["title"]
                link = f"https://www.youtube.com/watch?v={v_id}"
            except:
                print("erro na hora de pegar um link")
                
    print("vídeo baixado")
    return str(v_title)


def Driver() -> None:
    # get the latest chrome driver version number
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    # build the donwload url
    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"
    download_url = "https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/"
    # download the zip file using the url built above
    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    # extract the zip file
    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall() # you can specify the destination folder path here
    # delete the zip file downloaded above
    os.remove(latest_driver_zip)
