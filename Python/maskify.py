# return masked string
def maskify(cc):
    part1 = cc[:-4]
    part2 = cc[-4:]
    part1 =''.join( ['#' for i in range(len(part1))])
    return part1+part2