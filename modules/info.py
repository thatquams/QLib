import pandas as pd
from prompt_toolkit import print_formatted_text, HTML
import warnings
warnings.filterwarnings('ignore')
from read import read

def info(df):

    # if type(data) == DataFrame, output dataframe's info.
    if isinstance(df, pd.DataFrame):
        yield f'DATA SHAPE : {df.shape} \n '
        yield f'DATA DESCRIPTIONS : \n {df.describe()} \n'
        yield f'SUM OF NULL VALUES : \n {df.isna().sum()} \n'
        yield f'SUM OF DUPLICATED VALUES : \n {df.duplicated().sum()} \n'

    # if type(data) == Series, output series data info also.
    elif isinstance(df, pd.Series):
        yield f'DATA SHAPE : {df.shape} \n'
        yield f'DATA DESCRIPTIONS : \n {df.describe()} \n'
        yield f'SUM OF NULL VALUES : \n {df.isna().sum()} \n'

    # Throws error if data isn't in DataFrame/Series Format
    else:
        yield f'DATA NOT IN PANDAS DATAFRAME FORMAT : {type(df)}'
    
    return df.sample(3)



        
