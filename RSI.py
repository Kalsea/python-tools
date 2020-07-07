import pandas as pd
import numpy as np

def RSIfun(price, n):

    delta = price.diff()
    
    dUp = delta.copy()
    dDown = delta.copy()
    dUp[dUp < 0] = 0
    dDown[dDown > 0] = 0
    
    RolUp = dUp.rolling(window=n).mean()
    RolDown = dDown.rolling(window=n).mean().abs()
    
    RS = RolUp / RolDown
    
    rsi = 100.0 - ( 100.0 / (1 + RS))
    
    return rsi

