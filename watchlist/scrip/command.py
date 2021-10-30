import time
import click
from datetime import datetime
from watchlist import app, db
from watchlist.models import User, Movie , Ethusdt1m
from watchlist.scrip.binance import getstick
import socket
import struct
import win32api

def onlinetime():
    now = datetime.now()
    now = datetime.strftime(now,'%Y-%m-%d %H:%M:%S')
    print('现在时间是：',now)
    TimeServer = 'time.windows.com'  # 国家授时中心ip
    Port = 123
    def getTime():
        TIME_1970 = 2208988800
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = '\x1b' + 47 * '\0'
        data = bytes(data, 'utf-8')
        client.sendto(data, (TimeServer, Port))
        data, address = client.recvfrom(1024)
        data_result = struct.unpack('!12I', data)[10]
        data_result -= TIME_1970
        return data_result

    tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.gmtime(getTime())
    win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, 0)
    now = datetime.now()
    now = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    print('更新后的时间是：', now)

