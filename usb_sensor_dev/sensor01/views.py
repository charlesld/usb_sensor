from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
from seri import fetData

def renToWeb(request):
    rawData = fetData()
    print rawData
    if rawData:
        TEMP=float(rawData[0])
        HUMI=float(rawData[1])
        PM2d5=float(rawData[3])
        HCHO= float(rawData[14])
        TVOC= float(rawData[15])
        ret = {"temp":TEMP,"humi":HUMI,"pm2d5":PM2d5,"hcho":HCHO,"tvoc":TVOC}
        return HttpResponse(json.dumps(ret))

def index(request):
    return render(request, 'index.html')
