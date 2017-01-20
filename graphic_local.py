#!/usr/bin/env python
#coding:utf-8
###############################################
#甲醛检测传感数据收集绘图
#单机版V1.0
#传感器购买：淘宝{微创联合}
#任何运行问题，联系我邮箱pppoe@139.com
#需要模块：
#1、serial :  pip install PySerial
#2、bokeh  :  pip install bokeh
#3、pandas ： pip install pandas   (ubuntu 可以使用apt-get install python-pandas安装）
#运行版本 python 2.7
##############################################
import serial
import os

from bokeh.charts import Area, show, output_file, defaults
from bokeh.layouts import row
from bokeh.layouts import gridplot
import time
import sys

def progess(percent):  #采集进程，不需要实时显示数据时调用该进度条
    if percent <= 100:
        time.sleep(.01)
        sys.stdout.write("\r[%s] %d%%" % (('%%-%ds' % 50) % (50 * percent / 100 * '#'), percent))
        sys.stdout.flush()


def showgraphic(TEMP,HUMI,PM2d5,HCHO,TVOC):
    defaults.width = 600
    defaults.height = 300

    tempdata = dict(
        temperature = TEMP,
    )
    #print (tempdata)
    humidata = dict(
        humidity = HUMI
    )
    pm2d5data = dict(
        pm2dot5 = PM2d5
    )
    hchodata = dict(
        formaldehyde = HCHO
    )
    tvocdata = dict(
        smell = TVOC
    )

    area1 = Area(tempdata, title="温度显示", legend="top_left",xlabel='时间', ylabel='温度',color='#A6CEE3')
    area2 = Area(humidata, title="湿度显示", legend="top_left",xlabel='时间', ylabel='湿度',color='#B2DF8A')
    area3 = Area(pm2d5data,title="PM2.5显示", legend="top_left",xlabel='时间', ylabel='PM2.5浓度',color='#33A02C')
    area4 = Area(hchodata,title="甲醛显示", legend="top_left",xlabel='时间', ylabel='甲醛浓度',color='#FB9A99')
    area5 = Area(tvocdata,title="有机挥发物显示", legend="top_left",xlabel='时间', ylabel='TVOC浓度')
    filename = 'usb_sensor.html'
    if os.path.isfile(filename):   #bokeh好像无法支持动态绘图方式，采用动态更迭方式生成绘图结果
        os.remove(filename)
    output_file("usb_sensor.html", title="usb_sensor_data")
    area_charts = [area1,area2,area4,area5,area3]
    show(gridplot(area_charts,ncols=2))
    return 'Done'

countn = 0
se = serial.Serial('COM3')  #电脑com口，自行定义，linux加载CH340驱动，改成对应文件
TEMP = []
HUMI = []
PM2d5 = []
HCHO = []
TVOC = []
print ('温度   |  湿度  |  PM2.5  |  甲醛  |  TVOC')  #初始标题栏
while True:
    xdata = se.readline()
    if xdata:
        countn += 1
        stdout = xdata.strip()
        usb_data = stdout.split()
#        sock.send(('%s   |  %s  |  %s     | %s  | %s  ')%(usb_data[0],usb_data[1],usb_data[3],usb_data[14],usb_data[15])) #使用服务端发送时使用
        print (('%s   |  %s  |  %s     | %s  | %s  ')%(usb_data[0],usb_data[1],usb_data[3],usb_data[14],usb_data[15]))
        TEMP.append(float(usb_data[0]))
        HUMI.append(float(usb_data[1]))
        PM2d5.append(float(usb_data[3]))
        HCHO.append(float(usb_data[14]))
        TVOC.append(float(usb_data[15]))
#        progess(countn/10)    #进度条显示，输出数值该方法不可用
        if countn == 600:  #采集600个数据，如果数据量大需要自行添加求平均值出图，否则数据量会比较小
            break
        elif countn%150 == 0: #每150个数据出图
            showgraphic(TEMP,HUMI,PM2d5,HCHO,TVOC)
    else:
        continue

showgraphic(TEMP,HUMI,PM2d5,HCHO,TVOC) #数据采集完最终出图
