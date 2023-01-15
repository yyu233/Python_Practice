def compute_average_word_length(instring, unique=False):
    '''
        instring: input string
        unique: if True, exclude duplicated words
        return the average length of the words in the input string
    '''
    assert instring is not None
    assert unique is not None
    assert isinstance(instring, str)
    assert isinstance(unique, bool)
    
    if len(instring) == 0:
        return 0.0

    count = 0.0
    length = 0.0
    i = 0
    n = len(instring)

    visited = set()

    for j in range(n + 1):
        if j != n and instring[j].isalpha():
            length = length + 1
            if not instring[i].isalpha():
                i = j
        else:
            if instring[i].isalpha():
                word = instring[i:j]
                if unique:
                    if word not in visited:
                        count = count + 1
                        visited.add(word)
                else:
                    count = count + 1
            i = j

    if count == 0:
        return 0.0

    return length / count

x="123"
print(compute_average_word_length(x, False))

