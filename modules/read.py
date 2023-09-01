import os
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from prompt_toolkit import print_formatted_text, HTML

def read(data, header=None):

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
        
        else:
            # dataframe global variable
            data_frame = action(data)

            """
            if header:
            index starts from zero, so this condition maintains the column headers
            """
            if header:
                try:
                    # data_frame = action(data)
                    return pd.DataFrame(data_frame)

                except Exception as e:
                    error_msg = f'Error reading file: {str(e)}'
                    print_formatted_text(HTML(f'<b>{error_msg}</b>'))
                    return None
                
            # if an index argument for the column header is passed
            else:
                # not working yet
                data_frame.columns = data_frame.iloc[:, header:]
                data_frame = data_frame.iloc[header:]
                # .reset_index(drop=True)
                return (data_frame)
                        
    else:
        error_msg = f'ERROR => The File {data} You\'re trying to reference does not exist'
        print_formatted_text(HTML(f'<b>{error_msg}</b>'))
        # return None


# print(read("../testing/Human Resources.xlsx", header=1))
print(read("../testing/Human Resources.xlsx", header=2))