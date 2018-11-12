def sum_two_smallest_numbers(numbers):
    if (numbers[0] > numbers[1]):
        min1 = numbers[1]
        min2 = numbers[0]
    else:
        min1 = numbers[0]
        min2 = numbers[1]
    for i in range(2,len(numbers)):
        if numbers[i] < min2:
            if numbers[i] < min1:
                min1,min2= numbers[i],min1
            else:
                min2 = numbers[i]
    return min1+min2