import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from read import read

"""Replace Redundant values"""
def fill_redunds(data, to_replace, replace_with):
    
    if isinstance(data, pd.Series) | isinstance(data, pd.DataFrame):
        data.replace(to_replace, replace_with, inplace=True)

    return data, to_replace, replace_with


