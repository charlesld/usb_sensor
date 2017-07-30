# usb_sensor
利用传感器测量甲醛，TVOC，PM2.5，温度，湿度

#### 实时绘制的图片效果如下
![gif](https://github.com/charlesld/usb_sensor/blob/master/GIF.gif)

#### 天气一热，空气质量就爆表。。。
![爆表指数](hcho.gif)

#### 读取的数值走向显示
![走向](https://github.com/charlesld/usb_sensor/blob/master/图形显示.png)

#### 17-7-31 更新：
1. 将数据存入mysql，一来解决传感器黏包问题，二来为建设平台数据做准备
1. 真的不黏包了，sql.jpg 可以看，连续取800多数据，正常的很，图就不贴了
1. 前端传感器的数据读取频率，通过url文件里面的（代码见下）修改，默认设置60
> @sched.scheduled_job("interval",seconds=60)
