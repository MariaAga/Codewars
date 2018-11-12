def move_zeros(array):
    new = list(filter(lambda a: (type(a)==bool or a != 0), array))
    z = [0] * (len(array) - len(new))
    new.extend(z)
    return new