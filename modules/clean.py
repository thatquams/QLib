import pandas as pd
from prompt_toolkit import print_formatted_text, HTML
import os
import warnings
warnings.filterwarnings('ignore')


class DataCleaning(object):

    def __init__(self):
        pass
        
    def read(self, data):

        # Readable file formats
        actions = {'csv':pd.read_csv, 'xlsx':pd.read_excel,
                'json':pd.read_json, 'sql':pd.read_sql,
                'html':pd.read_html, 'pkl':pd.read_pickle}

        # check if file path's exist
        try:
            if os.path.exists(data):
                action = actions.get(data.split('.')[-1].lower(), f'Invalid File : ({data}')
                return (pd.DataFrame(action(data)))

                # If file format isn't valid
                    
            else:
                print_formatted_text(HTML(f'<b>ERROR => The File "{data}" You\'re trying to reference does not exist</b>'))

        except TypeError:
            if actions.get(data.split('.')[-1].lower()) not in actions.keys():
                print_formatted_text(HTML(f'<b> Invalid File Format {data} </b>'))

        return data


# from read import DataCleaning

wra = DataCleaning()
print(wra.read("5.fhf"))