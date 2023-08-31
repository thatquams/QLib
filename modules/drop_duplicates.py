import warnings
warnings.filterwarnings('ignore')
import pandas as pd 


def drop_duplicates(data):

    # Drop DUplicate values in the data
    if data.duplicated().sum() > 0:
        data.drop_duplicates(inplace=True, keep='first')
        print(f'SUM OF DUPLICATED VALUES : {data.duplicated().sum()}')
    
    return (data)