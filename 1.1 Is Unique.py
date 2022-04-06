'''1.1 Is Unique: Implement an algorithm to determine 
if a string has all unique characters. What if you cannot 
use additional data structures?'''

def Is_unique(val): 
    unq = True 
    for i in range(len(val)): 
        if val[i] in val[i+1:]:
            unq = False
            break
        else:
            unq = True
    return unq
