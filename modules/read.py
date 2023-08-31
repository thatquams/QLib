import os
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from prompt_toolkit import print_formatted_text, HTML

def read(data):

    # Readable file formats
    actions = {'csv': pd.read_csv, 'xlsx': pd.read_excel,
               'xls': pd.read_excel, 'json': pd.read_json, 
               'sql': pd.read_sql, 'html': pd.read_html, 
               'pkl': pd.read_pickle}

    # check if file path exists
    if os.path.exists(data):
        file_extension = data.split('.')[-1].lower()
        action = actions.get(file_extension)

        if action is None:
            error_msg = f'Invalid File Format: {file_extension}'
            print_formatted_text(HTML(f'<b>{error_msg}</b>'))
            return None

        try:
            data_frame = action(data)
            return pd.DataFrame(data_frame)

        except Exception as e:
            error_msg = f'Error reading file: {str(e)}'
            print_formatted_text(HTML(f'<b>{error_msg}</b>'))
            return None

    else:
        error_msg = f'ERROR => The File {data} You\'re trying to reference does not exist'
        print_formatted_text(HTML(f'<b>{error_msg}</b>'))
        # return None


# cle = DataCleaning("customer.das")
# print(cle.read())

print(read("../testing/Human Resources.xlsx"))