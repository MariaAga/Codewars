def alphabet_position(text):
    s=""
    for x in text:
        if (ord(x) >= ord('a') and ord(x) <= ord('z')):
            s+= (str(ord(x)-ord('a')+1)+" ")
        if (ord(x) >= ord('A') and ord(x) <= ord('Z')):
            s+= (str(ord(x)-ord('A')+1)+" ")  
    return s[:-1]