ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def compute_slug(key):
    key = key.lower() # makes key lower
    """
    Given a key string, compute and return the len-26 slug list for it.
    >>> compute_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> compute_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> compute_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> compute_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """
    tmp = []
    result = []
    new_alpha = ALPHABET
    for i in key:  # loops through all the characters in key
        tmp.append(i)      # adds the characters to empty list
    for i in tmp: #goes through temp
        if i in new_alpha: #if a character is in new_alpha
            new_alpha.remove(i) #remove said character
    tmp.append(new_alpha) #append our new_alpha to tmp
    # right now tmp is a list inside of a list so we must flatten it out
    for element in tmp: #goes through tmp
        if type(element) is list: # if our elemen in tmp is a list
            for item in element: # go through said list
                result.append(item) # append list to result
        else:
            result.append(element) #else append it
    return result
print(compute_slug("zasdf")) # test
