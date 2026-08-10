
from ema import ema

fast_ema_value = 10
slow_ema_value = 200

def strategy(closes):
    #compute indicators
    fast_ema = ema(closes, fast_ema_value)
    slow_ema = ema(closes, slow_ema_value)

    signals = []

    #generate signals
    for i in range(len(closes)):
        if fast_ema[i] > slow_ema[i]:
            signals.append['buy']
        elif fast_ema[i] < slow_ema[i]:
            signals.append['sell']
        else:
            signals.append['hold']

    #return everything the orchestrator needs
    return {
        'fast_ema': fast_ema,
        'slow_ema': slow_ema,
        'signals': signals
    }