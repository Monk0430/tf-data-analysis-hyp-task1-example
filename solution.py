import pandas as pd
import numpy as np


chat_id = 408092552 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    significance=0.09
    mean_control = x_success / x_cnt
    mean_test = y_success / y_cnt
    
    # Вычисляем стандартное отклонение для каждой группы
    std_control = (x_success * (1 - x_cnt) + x_cnt * (1 - x_success)) / (x_cnt ** 2)
    std_test = (y_success * (1 - y_cnt) + y_cnt * (1 - y_success)) / (y_cnt ** 2)
    
    # Вычисляем статистику z
    z = (mean_control - mean_test) / np.sqrt(std_control / x_cnt + std_test / y_cnt)
    return z>significance
