import pandas as pd
import numpy as np
import scipy.stats as st 
from statsmodels.stats.weightstats import ztest as ztest

chat_id = 881258336 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: 
    p_value=ztest(x, value=500, alternative = 'larger')[1]
    if (p_value<0.06): 
        return True 
    else: 
        return False
