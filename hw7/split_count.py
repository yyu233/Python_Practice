import pandas as pd

def split_count(x):
    '''
        Split out column entries

        x: pd.Series
        return: pd.DataFrame
    '''
    assert isinstance(x, pd.Series)

    wordSE = x.str.split(', ')
    wordSE = wordSE.explode()
    wcSE = wordSE.value_counts(ascending=True)

    return wcSE.to_frame(name='count')
