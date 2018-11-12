def rgb(r, g, b):
    rgb = [r,g,b]
    for i in range(3):
        if rgb[i]<0:
            rgb[i]='00'
        elif rgb[i]>255:
            rgb[i]='FF'
        else:
            rgb[i]=format(rgb[i], '02X')

    return ''.join(rgb)