import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 557932710 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    t = 65
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)


#пока примерно что-то:
import scipy.stats as st
z1 = st.gamma.ppf(1-alpha/2, a = n, scale = 1)
z2 = st.gamma.ppf(alpha/2, a = n, scale = 1)
loc/(t*t) + 1/(2*t*t) + z1/(t*t), \
loc/(t*t) + 1/(2*t*t) + z2/(t*t)
