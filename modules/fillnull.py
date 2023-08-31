import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from read import read



def fillnull(data, thresh, method):
    mean = data.mean()
    median = data.median()
    mode = data.mode()[0]

    if (isinstance(data, pd.DataFrame)) :
        if (data.isna().sum()*100 / len(data) < thresh) & (method == 'mean'):
            if (data.dtype == int) | (data.dtype == float):
                data.fillna(mean, inplace=True)

        elif (data.isna().sum()*100 / len(data) < thresh) & (method == 'median'):
            if (data.dtype == int) | (data.dtype == float):
                data.fillna(median, inplace=True)

        elif (data.isna().sum()*100 / len(data) < thresh) & (method == 'mode'):
            if (data.dtype == int) | (data.dtype == float):
                data.fillna(mode, inplace=True)       

        elif (data.isna().sum()*100 / len(data) < thresh) & (method == 'median'):
            if (data.dtype == object):
                data.fillna(median, inplace=True)

        elif (data.isna().sum()*100 / len(data) < thresh) & (method == 'mode'):
            if (data.dtype == object):
                data.fillna(mode, inplace=True)

        else:
            data.dropna(axis=1, inplace=True)

    return data, thresh, method







































