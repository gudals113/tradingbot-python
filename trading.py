import os
import pyupbit
import time, datetime
import pandas as pd
import numpy as np

# from main import BALANCE

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']
upbit=pyupbit.Upbit(ACCESS_KEY, SECRET_KEY)


#K 30일마다 갱신해주자
def GET_TARGET_PRICE(K):
    df = pyupbit.get_ohlcv("KRW-BTC", count=2)
    gap = df['high'][0] - df['low'][0] #전날 고점 저점의 변동폭
    target = df['open'][-1] + gap*K
    return target

def SET_START_TIME():
    df = pyupbit.get_ohlcv("KRW-BTC",count=1)
    start = df.index[0]
    return start

def GET_BALANCE(ticker):
    balances = upbit.get_balances()
    for balance in balances:
        if balance['currency'] == ticker and balance['balance'] != None:
            return float(balance['balance'])
        else:
            return 0            
        
def GET_CURRENT_PRICE_LIST():
    current = pyupbit.get_orderbook(ticker="KRW-BTC")
    df = pd.DataFrame(current)
    return df

def GET_CURRENT_PRICE():
    price = pyupbit.get_orderbook(ticker="KRW-BTC")["orderbook_units"][0]["ask_price"]
    return price


while True:
    try:
        NOW = datetime.datetime.now()
        START_TIME=SET_START_TIME()
        END_TIME = START_TIME + datetime.timedelta(days=1)
        KRW_BALANCE=GET_BALANCE("KRW")
        BTC_BALANCE=GET_BALANCE("BTC")
        
        #매매 시간일 때 (하루 중)
        if START_TIME <= NOW < END_TIME :
            TARGET_PRICE=GET_TARGET_PRICE(0.5)
            CURRENT_PRICE = GET_CURRENT_PRICE()
            
            if TARGET_PRICE < CURRENT_PRICE and KRW_BALANCE >5000:
                upbit.buy_market_order("KRW-BTC", KRW_BALANCE*0.9995)
        else:
            if BTC_BALANCE > 0 :
                upbit.sell_market_order("KRW-BTC", BTC_BALANCE)
                    
        time.sleep(1)
            
    except Exception as e:
        print(e)
        time.sleep(1)