import string
from codecs import encode as _dont_use_this_

def rot13(message):
    abc='nopqrstuvwxyzabcdefghijklm'
    aBC='NOPQRSTUVWXYZABCDEFGHIJKLM'
    s = []
    for a in message:
        if a.isupper():
            s.append(aBC[ord(a)-ord('A')])
        elif a.islower():
            s.append(abc[ord(a)-ord('a')])
        else:
            s.append(a)
    return ''.join(s)

