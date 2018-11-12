import itertools
def permutations(string):
    a = []
    for e in  itertools.permutations(string):
        a.append(''.join(e))
    return set(a)