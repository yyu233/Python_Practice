import math
import os

def split_by_n(fname, n=3):
    '''
        Split files into sub files of near same size
        fname: Input file name
        n is the number of segments
    '''
    assert isinstance(fname, str)
    assert isinstance(n, int)
    assert len(fname) > 0
    assert n > 0

    fs = 0
    with open(fname, 'r') as fp:
        fp.seek(0, os.SEEK_END)
        fs = fp.tell()

    avgfs = math.ceil(fs / n)
    offset = 0
    size = 0
    with open(fname, 'r') as src:
        for i in range(0, n):
            ofname = '{0}_00{1}.txt'.format(fname, i) 
            with open(ofname, 'wt') as dst:
                if i == n - 1:
                   content = src.read()
                else:
                    content = src.read(avgfs)
                if content[-1] != '\n':
                    j = -2
                    while True:
                        if content[j] == '\n':
                            offset = src.seek(offset + avgfs + j + 1, 0)
                            break
                        else:
                            j = j - 1
                if i == n - 1:
                    dst.write(content)
                else:
                    dst.write(content[:j+1])
