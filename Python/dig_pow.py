def dig_pow(n, p):
    l= len(str(n))
    number=n
    sum1=0
    for i in range(p,l+p):
        sum1+=pow(n%10,(l+2*p-i-1))
        n=int(n/10)
    if (sum1%number==0):
        return sum1/number
    return -1
