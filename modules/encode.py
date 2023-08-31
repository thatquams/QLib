import pandas as pd
from read import read
from sklearn.preprocessing import LabelEncoder

df = read('data.csv')

"""Encode target labels with value between 0 and n_classes-1.

This transformer should be used to encode target values, *i.e.* y, and not the input X"""

def encode(data, keep_first=True):
    
    encoder = LabelEncoder()
    data = encoder.fit_transform(data)


    if keep_first == False:
        data=data.iloc[:,1:]

    return pd.DataFrame(data)


