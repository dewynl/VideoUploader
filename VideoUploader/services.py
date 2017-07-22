import requests
import json

def get_videos(from_, to):
    url = 'http://localhost:4567/rest/videosRange/'

    date1= from_.split("/")
    date2= to.split("/")
    path = "http://localhost:4567/rest/videosRange/"+ date1[0] + '/' + date1[1] + '/' + date1[2] + '/' + date2[0] + '/' + date2[1] + '/' + date2[2]
    print(path)
    r = requests.get(path)
    print(r)
    videos = r.json()
    print(videos[0])
    return videos