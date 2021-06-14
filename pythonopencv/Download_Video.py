import youtube_dl
import requests
import os
y={}
path ="C:\\Users\\PC\\PycharmProjects\\pythonopencv"
os.chdir(path)

url="https://youtu.be/rUWxSEwctFU"
with youtube_dl.YoutubeDL(y) as u:
    print("Downloading..."+url)
    u.download([url])
print("Done")
