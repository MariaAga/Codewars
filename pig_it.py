def pig_it(text):
    words = text.split(" ")
    for i in range(len(words)):
        if (len(words[i])>1):
            words[i] = words[i][1:]+words[i][:1]+"ay"
        elif (words[i].isalpha()):
            words[i] = words[i]+"ay"
    return ' '.join(words)
