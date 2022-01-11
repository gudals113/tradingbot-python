import os
import pyupbit
import time, datetime
import pandas as pd
import numpy as np

from main import BALANCE

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']
upbit=pyupbit.Upbit(ACCESS_KEY, SECRET_KEY)


#K 30일마다 갱신해주자
def GET_TARGET(K):
    df = pyupbit.get_ohlcv("KRW-BTC", count=2)
    gap = df['high'][0] - df['low'][0]
    target = df['open'][-1] + gap*K
    
    return target

TARGET=GET_TARGET(0.5)

def SET_START_TIME():
    df = pyupbit.get_ohlcv("KRW-BTC",count=1)
    start = df.index[0]
    return start

START=SET_START_TIME()

def GET_BALANCE(ticker):
    balances = upbit.get_balances()
    for balance in balances:
        if balance['currency'] == ticker and balance['balance'] != None:
            return float(balance['balance'])
        else:
            return 0            
        
KRW_BALANCE=GET_BALANCE("KRW")
BTC_BALANCE=GET_BALANCE("BTC")
    
def GET_CURRENT_PRICE():
    current = pyupbit.get_orderbook(ticker="KRW-BTC")
    df = pd.DataFrame(current)
    return df
CURRENT_PRICE=GET_CURRENT_PRICE()
print(CURRENT_PRICE)