# import pandas as pd
# from read import read
# from sklearn.preprocessing import StandardScaler, QuantileTransformer, MinMaxScaler

"""Standardize features by removing the mean and scaling to unit variance.
The standard score of a sample x is calculated as:

    z = (x - u) / s

where u is the mean of the training samples or zero if with_mean=False, and s is the standard deviation of the training
samples or one if with_std=False.
Centering and scaling happen independently on each feature by computing the relevant statistics on the samples
in the training set. Mean and standard deviation are then stored to be used on later data using transform."""

def scale(data, method=''):
    try:
        # data mean
        data_avg = data.mean()
        # data std
        data_std = data.std()

        if (type(data) == pd.DataFrame ) | (type(data) == pd.Series):
                data = (data-data_avg) / data_std

        else:
            print(AttributeError)
    except:

        # return scaled data
        return data


df = pd.read_csv('Test.csv')
print(df.isna().sum())


year_dist = df[['Distance', 'Year']]
year_dist['Year'] = year_dist['Year'].str.replace(',','')
year_dist['Year'] = pd.to_numeric(year_dist['Year'])

for col in year_dist:
    year_dist[col].fillna(year_dist[col].mode()[0], inplace=True)

year_dist['Year'] = year_dist['Year'].astype(int)

# Before scaling
# print(year_dist)

# year_dist = scale(year_dist, 'quantile_transformer')
# After Scaling
# print(year_dist)
