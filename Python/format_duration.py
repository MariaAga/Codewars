def format_duration(seconds):
    if(seconds==0):
        return 'now'
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)
    time = [y, d, h, m, s]
    name = ['year', 'day', 'hour', 'minute', 'second']
    for i in range(5):
        if time[i] > 0 and time[i] > 1:
            time[i] = "{} {}s".format(time[i], name[i])
        elif time[i] > 0:
            time[i] = "{} {}".format(time[i], name[i])
    time = list(filter(lambda x: type(x) != int, time))
    if len(time) == 1:
        return time[0]
    time[-2] = "{} and {}".format(time[-2],time[-1])
    time.pop()
    if len(time) == 1:
        return time[0]
    return ', '.join(time)
    