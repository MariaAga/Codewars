def narcissistic( value ):
    sum=0
    real_num =value
    pow = len(str(value))
    while(value>0):
        sum+=(value%10)**pow
        value/=10
    return sum==real_num