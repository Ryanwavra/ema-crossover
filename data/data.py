import pandas as pd

"""
creates dataframe (df) from .csv file, converts timestamp from timestamp
to datetime, sets 'timestamp' as the inex, returns df
"""

def loader():
    df = pd.read_csv('data/Data_sets/nq_1min_2022-25_1.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    return df


