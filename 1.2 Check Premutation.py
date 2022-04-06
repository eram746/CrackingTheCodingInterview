'''1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
other.'''

def Check_Prem(string1, string2):
    result = 'Is not a premuation'
    for char in string1:
        if char not in string2:
            break
        else:
            result = 'Is a premuation'
    return result
            
