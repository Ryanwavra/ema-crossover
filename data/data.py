import pandas as pd

def loader():
    df = pd.read_csv('data/Data_sets/nq_1min_2022-25_1.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    return df


