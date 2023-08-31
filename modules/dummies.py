import numpy as np
from read import read
import pandas as pd

"""Convert categorical variable into dummy/indicator variables."""

def dummies(data,feature,keep_first=True):

    data = pd.get_dummies(data, columns=feature)


    if keep_first == False:
        data = data.iloc[:,1:]

    return data
        
