from django.contrib.sites import requests
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile, SimpleUploadedFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from zeep import Client

from untitled.Forms.dateform import dateForm

def get_videos(from_, to):
    url = 'http://localhost:4567/rest/videosRange/'

    date1= from_.split("/")
    date2= to.split("/")
    params = {'dia1': date1[0], 'mes1': date1[1],'year1': date1[2],'dia2': date2[0], 'mes2': date2[1],'year2': date2[2]}
    r = requests.get('http://localhost:4567/rest/videosRange/', params=params)
    videos = r.json()
    videos_list = {'videos':videos['results']}
    return videos_list