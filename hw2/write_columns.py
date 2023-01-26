def write_columns(data, fname):
    '''
        data: list of integer or float
        fname: string of file name
        
        write data_value, data_value**2, (data_value + data_value**2)/3 to
        3 columns to a commma-separated file
        
        written floating-point values must be to the hundreths place
    '''
    assert isinstance(data, list)
    assert isinstance(fname, str)

    for i in range(len(data)):
        assert isinstance(data[i], int) or isinstance(data[i], float)

    with open(fname, "w") as of:
        for i in range(len(data)):
            data_value = float(data[i])
            of.write("{:.2f},{:.2f},{:.2f}\n".format(data_value, \
            data_value ** 2, \
            (data_value + data_value ** 2) / 3))
