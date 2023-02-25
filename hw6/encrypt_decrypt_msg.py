import random

def build_word_dict(fname):
    '''
        Build word dictionary from source file
        fname: string name of source file
        return: dictionary of key: word, value: size 2 tuple (linenumber, word number)
    '''
    wdict = {}
    with open(fname, 'r') as fh:
        for lnum, line in enumerate(fh, 1):
          wlist = "".join((ch if ch.isalpha() else " ") for ch in line).split()
          for wnum, w in enumerate(wlist, 1):
              wtuple = (lnum, wnum)
              w = w.lower()
              wdict.setdefault(w, []).append(wtuple)

    return wdict

def encrypt_message(message, fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.

    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message, str)
    assert isinstance(fname, str)
    assert len(message) > 0
    assert len(fname) > 0
    
    res = []
    wdict = build_word_dict(fname)
    repeatdict = {}
    for w in message.split():
        wlisttuple = wdict[w]
        while True:
            rndindx = random.randint(0,len(wlisttuple) - 1)
            enctuple = wlisttuple[rndindx]
            if w in repeatdict:
                if enctuple not in repeatdict[w]:
                    repeatdict[w].add(enctuple)
                    break
            else:
                repeatdict[w] = {enctuple}
                break
        res.append(enctuple)

    return res

def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message.

    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert isinstance(inlist, list)
    for tup in inlist:
        assert isinstance(tup, tuple)
        assert len(tup) == 2
        assert isinstance(tup[0], int)
        assert isinstance(tup[1], int)
        assert tup[0] > 0
        assert tup[1] > 0

    assert isinstance(fname, str)
    assert len(fname) > 0

    msgsize = len(inlist)
    res = [None] * msgsize
    encdict = {}
    for i, tup in enumerate(inlist):
        encdict.setdefault(tup[0], []).append((i, tup[1]))

    with open(fname, 'r') as fh:
        for lno, line in enumerate(fh,1):
            if msgsize == 0:
                break
            if lno in encdict:
                wlist = "".join((ch if ch.isalpha() else " ") for ch in line).split()
                for ele in encdict[lno]:
                    resindx = ele[0]
                    wno = ele[1]
                    word = wlist[wno - 1].lower()
                    res[resindx] = word
                    msgsize = msgsize - 1

    return " ".join(res)
