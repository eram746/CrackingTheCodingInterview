'''1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
other.'''

def Is_prem(string1, string2):

    if len(string1) != len(string2): 
        return False
    else: 
        return sorted(string1) == sorted(string2)
        #return sorted(string1.lower()) == sorted(string2.lower())


