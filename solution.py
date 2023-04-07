import pandas as pd
import numpy as np

import scipy.stats as st

chat_id = 557932710 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    t = 65
    loc = sum(x)/n

    
    z1 = st.gamma.ppf((1+p)/2, a = n, scale = 1/n)
    z2 = st.gamma.ppf((1-p)/2, a = n, scale = 1/n)
    
    return 2*loc/(t*t) - 2/(2*t*t) + 2*z2/(t*t), \
           2*loc/(t*t) - 2/(2*t*t) + 2*z1/(t*t)
