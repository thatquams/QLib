LIBRARY FUNCTIONALITIES


1. This Library is built on top of the pandas library, and also to enable user to implement their code with few lines of code. you can install the package using the pip command. "pip install quelib"

2. Import Qlib as ql.

3. This Library automatically detects your data extension type and then reads it.

4. This library supports files from EXCEL, CSV, JSON, SQL, HTML, PICKLE. to read your data, use the "read(data)".

5. Data from multiple sources should be read separately before merging or concatenating using the PANDAS's methods.

6. To set column header (Data.columns = data.iloc[columns_index_loc]).

7. If more than one redundant values is to be filled and filled with, the values should be represented in a list, 
separated with a comma.     (fill_redunds(data, [redunds to be replaced], [replace_with])).....In case of replacing values
in multiple columns,  you have to loop through them before calling the "fill_redunds" method.

8. User can fill null values in their data using the Fillnull(data, threshold, method). If the null values in a each
column is less than threshold, the column will be filled with the specified method, User can then "data.dropna(axis=1,inplace=True)" afterwards. 
Note : method parameter should be in a quote "" . The fillnull only supports(mean, median and mode) methods. And In case
of filling nan values in multiple columns, you have to loop through them before calling the "impute" module.

9. User can drop duplicate values in their data using the "drop_duplicates(data)" module, with the DATAFRAME passed 
as parameter.

10. User can encode their categorical features using the ".encode(data, [feature])".
NOTE:
It also has a default parameter "keep_first" whose default value is True, so
                                                                if keep_first == False:
                                                                        data=data.iloc[:,1:].

11. Scale your data using the "scale(data)" method before fitting them into a machine learning model.
The scale function takes in your data as an argument, and performs : (data-data.mean()) / data.std() on the imputed data, and then outputs a scaled data.







GENERAL NOTE : THE FORMAT OF THE OUTPUT GENERATED AFTER PERFORMING MULTIPLE ACTIVITIES ON YOUR DATA USING THIS PACKAGE IS
STILL IN DATAFRAME, SO YOU CAN PERFORM PANDAS METHODS ON YOUR DATA ALSO.
