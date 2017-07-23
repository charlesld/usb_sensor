#!/usr/bin/env python
#coding:utf-8
import serial
import time

se = serial.Serial('COM3')
# TEMP = []
# HUMI = []
# PM2d5 = []
# HCHO = []
# TVOC = []
def fetData():
    xdata = ''  #不初始化，出现黏包情况后无法自动恢复
    stdout = ''
    time.sleep(0.5)
    xdata = se.readline()
    if xdata:
        stdout = xdata.strip()
        usb_data = stdout.split()
        # TEMP.append(float(usb_data[0]))
        # HUMI.append(float(usb_data[1]))
        # PM2d5.append(float(usb_data[3]))
        # HCHO.append(float(usb_data[14]))
        # TVOC.append(float(usb_data[15]))
        print (len(usb_data))
        print usb_data
        if len(usb_data) ==16:
            return usb_data
        # TEMP,HUMI ,PM2d5,HCHO ,TVOC

if __name__ == '__main__':
    n = 0
    while n<2000:
        fetData()
        n += 1