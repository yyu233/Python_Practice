def write_chunks_of_five(words, fname):
    '''
        words: a list of string
        fname: string name for the output file

        create a new file that consists of each consecutive non-overlapping
        sequence of five lines merged into one line
    '''
    assert isinstance(words, list)
    
    for i in range(len(words)):
        assert isinstance(words[i], str)

    with open(fname, "w") as of:
        for i in range(0, len(words), 5):
            end = min(len(words), i + 5)
            for j in range(i, end):
               if j + 1 == end:
                of.write(words[j] + "\n")
               else:
                of.write(words[j] + " ")
