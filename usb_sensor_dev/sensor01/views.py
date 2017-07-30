from django.shortcuts import render
from django.http import HttpResponse
import json
from models import rawDatas
# Create your views here.
from seri import fetData
import time

def save_to_sql():
    rawData = fetData()
    # print rawData
    if len(rawData) == 16:
        TEMP = float(rawData[0])
        HUMI = float(rawData[1])
        PM2d5 = float(rawData[3])
        HCHO = float(rawData[14])
        TVOC = float(rawData[15])
        savedate = rawDatas.objects.create(
            PM25=PM2d5,
            TVOC=TVOC,
            HCOC=HCHO,
            TEMP=TEMP,
            WEIG=HUMI,
        )
        print savedate
        savedate.save()



def renToWeb(request):

    sqldata = rawDatas.objects.all().order_by("-id")[:1]
    print sqldata[0].PM25,sqldata[0].TVOC,sqldata[0].HCOC,sqldata[0].WEIG,sqldata[0].TEMP
    if sqldata:

        # ret = {"temp":TEMP,"humi":HUMI,"pm2d5":PM2d5,"hcho":HCHO,"tvoc":TVOC}
        ret = {"hcho": sqldata[0].HCOC, "pm2d5": sqldata[0].PM25, "humi": sqldata[0].WEIG, "tvoc": sqldata[0].TVOC,
               "temp": sqldata[0].TEMP}
        return HttpResponse(json.dumps(ret))
    else:
        print "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFCCCCCCCCCCCCCCCCCCCCKKKKK"
        time.sleep(2)
        return HttpResponse(json.dumps({"hcho": 0.0, "pm2d5": 0.0, "humi": 0.0, "tvoc": 0.0, "temp": 0.0}))

def index(request):
    return render(request, 'index.html')
