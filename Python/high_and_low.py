def high_and_low(numbers):
    numbers=sorted([int(x) for x in (numbers.split())])
    
    return ('{0} {1}'.format(numbers[-1],numbers[0]))