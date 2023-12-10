import pandas as pd
import os
from datasets import load_dataset

def my_decorator(func):

    def wrapper(*args, **kwargs):
        format = dict(**kwargs)
        form = format['format']
        if os.path.isfile('file.' + form):
            file = open('file.' + form, 'r')
            val = file.read()
            print(val)
            return val
        else:
            file = open('file.' + form, 'w')
            val = func(*args)
            print(val)
            file.write(str(val))
            return val
    return wrapper


@my_decorator
def calculate_correlation(data):
    return data['age'].corr(df['limit_bal'])

dataset = load_dataset("imodels/credit-card")
df = pd.DataFrame(dataset['train'])


calculate_correlation(df, format='csv')
