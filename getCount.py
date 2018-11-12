
import re
def getCount(inputStr):
    num_vowels = 0
    num_vowels = len(re.findall("[aeiou]",inputStr))
    
    return num_vowels