import os
import pyupbit
import pandas as pd
import numpy as np

access_key = os.environ['ACCESS_KEY']
secret_key = os.environ['SECRET_KEY']
upbit=pyupbit.Upbit(access_key, secret_key)

#
def GET_ROR(K):
    
    df = pyupbit.get_ohlcv("KRW-BTC", count=30)

    
    df['range'] = (df['high']-df['low']) * K
    df['target'] = df['open'] + df['range'].shift(1)

    tax=0.05
    df['ror'] = np.where(df['high'] > df['target'],
                        ( df['close']*(1-tax) ) / ( df['target']*(1+tax) ),
                        1
                        )

    df['hpr'] = df['ror'].cumprod()
    df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
    
    # print(df)
    return(df['hpr'][-1])


for i in np.arange(0.3, 0.9, 0.05):
    ROR=GET_ROR(i)
    print(i, ROR)    
# print("MDD(%): ", df['dd'].max())