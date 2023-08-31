from xml.etree.ElementInclude import include
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from read import read


def impute(data, thresh, method):

    # method's 
    mean = data.mean()
    median = data.median()
    mode = data.mode()[0]

    # Conditional statements on the data, null values will be filled according to the data, threshold
    # and method specified by the user,

    if (data.isna().sum()*100 / len(data) < thresh) & (method == 'mean'):
        if (data.dtype == int) | (data.dtype == float):
            data.fillna(mean, inplace=True)

    elif (data.isna().sum()*100 / len(data) < thresh) & (method == 'median'):
        if (data.dtype == int) | (data.dtype == float):
            data.fillna(median, inplace=True)

    elif (data.isna().sum()*100 / len(data) < thresh) & (method == 'mode'):
        if (data.dtype == int) | (data.dtype == float):
            data.fillna(mode, inplace=True)       

    elif (data.isna().sum()*100 / len(data) < thresh) & (method == 'mode'):
        if (data.dtype == object):
            data.fillna(mode, inplace=True)


    return data, thresh, method

