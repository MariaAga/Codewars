def solution(string, markers):
    s = ""
    flag = True
    for i in range(len(string)):
        if string[i] in markers:
            if s and s[-1] == ' ':
                s = s[:-1]
            flag = False
        elif (not flag) and (string[i]) == ('\n'):
            flag = True
            
            s += (string[i])
        elif flag:
            s += (string[i])
    return s
