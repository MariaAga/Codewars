def printer_error(s):
    count = sum([ 1 for x in s if x> 'm'])
    return ("{0}/{1}".format( count,len(s)))