import numpy as np
from watchlist import app, db
from watchlist.models import User, Movie, Ethusdt1m, Order
from watchlist.scrip import binance,command
from datetime import datetime
import threading
import time

exitFlag = 0
acc = 0
pos = 0
arprday = 0
arprh = 0
class myThread1 (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print ("开启线程：" + self.name)
        while exitFlag == 0:
            binance.geteth1m()
            time.sleep(61)
        print ("退出线程：" + self.name)
class myThread2 (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print ("开启线程：" + self.name)
        while exitFlag == 0:
            runbinan()
            time.sleep(61)
        print ("退出线程：" + self.name)

def init():
    global acc,pos,arprday,arprh
    print('system time accurate: ')
    command.onlinetime()
    acc = binance.getacc()[5]
    pos = binance.getpostion()[0]
    days30 = binance.getstick(interval='1d')[0]
    arprday = round(np.average([a.close for a in days30]),2)
    h30 = binance.getstick(interval='1h')[0]
    arprh = round(np.average([a.close for a in h30]), 2)
    return
def runbinan(price):

    global acc, pos, arprday, arprh
    # eth1m = Ethusdt1m
    # ethmin = eth1m.query.filter(eth1m.id > (eth1m.query.count() - 30)).all()
    x = 0
    while True:
       markprice = round(binance.getprice().markPrice, 2)
       ran = (markprice - price) / markprice
       if abs(ran) >= 0.003:
           print('ran=',ran)
           acc = binance.getacc()[5]
           blana = acc.withdrawAvailable * pos.leverage
           if blana > 1000:
               quantity = round(blana / 50 / markprice, 4)
           quantity = round(7 / price, 3)
           if ran > 0:
               side = "SELL"
           else:
               side = "BUY"
           print('side =',side,'quantity=',quantity,'blana=',blana,'price=',markprice)

           order = binance.trade(ordertype='MARKET', price=None, side=side, quantity=quantity, timeInForce=None)
           if order.status == 'NEW':
               price = markprice
               ordered = binance.getordered(orderid=order.orderId)
               orders = Order(ordertime=ordered.updateTime, orderid=ordered.orderId, side=ordered.side,
                          price=ordered.avgPrice, time=ordered.updateTime, origqty=ordered.executedQty, status=ordered.status)
               db.session.add(orders)
               db.session.commit()
       x = x + 1
       if x == 10:
           x = 0
           print('price=',price,'markprice=',markprice, 'ran=',ran)
       time.sleep(10)


if __name__ == '__main__':
    init()
    markprice = round(binance.getprice().markPrice, 2)
    time.sleep(10)
    runbinan(markprice)



    print('test')
