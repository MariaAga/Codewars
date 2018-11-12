import re
def order(sentence):
  if not sentence:
    return sentence
  words=sentence.split(" ")
  ordered  = [None] * len(words)  
  for i in range(len(words)):    
    m = re.search('[0-9]',words[i])
    j = int(m.group(0))-1  
    ordered[j]=words[i]

  return " ".join(ordered)