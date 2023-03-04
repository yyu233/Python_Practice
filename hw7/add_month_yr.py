import pandas as pd

def add_month_yr(x):
    '''
        Create a dataframe column month-yr with ID as row-index

        x: pd.DataFrame
        return: pd.DataFrame with the new column

    '''
    assert isinstance(x, pd.DataFrame)

    x['Timestamp'] = pd.to_datetime(x['Timestamp'])
    x['month-yr'] = x['Timestamp'].dt.strftime('%b-%Y')

    return x
