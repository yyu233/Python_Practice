def get_average_word_length(words):
    '''
        Compute the average length of the words
        words: list of strings
        return: float
    '''
    count = 0
    tot = 0.0

    assert isinstance(words, list)
    for w in words:
        assert isinstance(w, str)
        count = count + 1
        tot = tot + len(w)

    return tot / count

def get_longest_word(words):
    '''
        What is the longest word
        words: list of strings
        return: string
    '''
    maxlen = 0
    res = ""

    assert isinstance(words, list)
    for w in words:
        assert isinstance(w, str)
        if len(w) > maxlen:
            res = w
            maxlen = len(w)

    return res

def get_longest_words_startswith(words,start):
    '''
        What is the longest word that starts with a single letter
        words: list of strings
        start: string
        return: string
    '''
    res = ""
    maxlen = 0

    assert isinstance(words, list)
    assert isinstance(start, str)
    assert len(start) == 1
    for w in words:
        assert isinstance(w, str)
        if w[0] == start and len(w) > maxlen:
            res = w
            maxlen = len(w)

    return res

def get_most_common_start(words):
    '''
        What is the most common starting letter
        words: list of strings
        return: char
    '''
    lut = {}
    res = ""
    maxcnt = 0

    assert isinstance(words, list)
    for w in words:
        assert isinstance(w, str)
        firstchar = w[0]
        if firstchar in lut:
            lut[firstchar] = lut[firstchar] + 1
        else:
            lut[firstchar] = 1
        if lut[firstchar] > maxcnt:
            res = firstchar
            maxcnt = lut[firstchar]

    return res

def get_most_common_end(words):
    '''
        What is the most common ending letter
        words: list of strings
        return: char
    '''
    lut = {}
    res = ""
    maxcnt = 0

    assert isinstance(words, list)
    for w in words:
        assert isinstance(w, str)
        lastchar = w[-1]
        if lastchar in lut:
            lut[lastchar] = lut[lastchar] + 1
        else:
            lut[lastchar] = 1
        if lut[lastchar] > maxcnt:
            res = lastchar
            maxcnt = lut[lastchar]

    return res
