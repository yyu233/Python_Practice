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

def fix_categorical(x):
    '''
        Convert the month-yr column dtype to a Pandas CategoricalDtype with the correct order

        x: pd.DataFrame
        returns: pd.DataFrame
    '''
    assert isinstance(x, pd.DataFrame)

    x['month-yr'] = x['month-yr'].astype(pd.CategoricalDtype(categories=['Sep-2017', 'Jan-2018', 'Feb-2018', 'Mar-2018','Apr-2018','Sep-2018','Oct-2018','Jan-2019'],ordered=True))

    return x
