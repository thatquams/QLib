import pandas as pd


def dropna(data, axis=1):
    data.dropna(axis=1, inplace=True)

    if axis == 0:
        data.dropna(axis=0, inplace=True)

    return data