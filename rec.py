def rec(a,s,left,i):
    nS=s[:]
    if len(left)==1:
        nS.append(left[0])
        a.append(''.join(nS))
        return 
    
    for j in range(len(left)):
        nS.append(left[j])
        nLeft = left[:]
        nLeft.remove(left[j])
        rec(a,nS,nLeft,i)
        nS= nS[:-1]
        
        
def permutations(string):
    a = []
    
    rec(a,[],list(string),0)    
    return set(a)