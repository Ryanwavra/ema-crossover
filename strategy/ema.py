import talib

"""
defines what an ema is and calculates it based off the list of candle closes, and timperiod specified
"""

def ema(closes, timeperiod):
    return talib.EMA(closes, timeperiod=timeperiod)
   
