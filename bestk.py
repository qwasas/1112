from typing import DefaultDict
import pyupbit
import numpy as np


def get_ror(k=0.5):
    #open 시가  high 고가 low 저가 close 종가 volume 거래량
    df = pyupbit.get_ohlcv("KRW-BTC", count=60)
    #변동폭
    df['range'] = (df['high'] - df['low']) * k
    #매수가
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    #수익율
    df['ror'] = np.where(df['high'] > df['target']*1.02,
                         df['close'] / df['target'] - fee,
                         1)
   


    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))
