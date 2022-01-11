#market.py, account.py 등 필요없어진다.
import os
import pyupbit
import pandas as pd

access_key = os.environ['ACCESS_KEY']
secret_key = os.environ['SECRET_KEY']
upbit=pyupbit.Upbit(access_key, secret_key)

#전체잔고
BALANCE = upbit.get_balances()
#원화 잔고
KRW_BALANCE = upbit.get_balance('KRW')
#비트코인 잔고
BTC_BALANCE = upbit.get_balance('BTC')

#원화 마켓 티커
KRW_TICKERS = pyupbit.get_tickers("KRW")
DF_KRW_TICKERS = pd.DataFrame(KRW_TICKERS)
