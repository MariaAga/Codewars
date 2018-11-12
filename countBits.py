def countBits(n):
    b =str(bin(n))[2:]
    return len([x for x in b if int(x)])