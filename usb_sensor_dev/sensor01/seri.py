#!/usr/bin/env python
#coding:utf-8
import serial
import time


se = serial.Serial('COM4')

def fetData():

    time.sleep(0.5)
    xdata = se.readline()
    # print "xdata:",xdata
    if xdata:
        stdout = xdata.strip()
        usb_data = stdout.split()
        # print (len(usb_data))
        # print usb_data
        if usb_data and len(usb_data) ==16:
            return usb_data
        else:
            xdata = " "
            time.sleep(2)
            # return ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
            return [0]


if __name__ == '__main__':
    n = 0
    while n<2000:
        fetData()
        n += 1