# Implement an algorithm to determine if a string has all unique characters.
# Assumptions:
# 1) Cannot use additional data structures
# 2) If length of string is 1, then return True
# 3) Can be any letter, int, float, or symbol

def is_unique(s):
    """Returns True if characters in s are unique. Returns false if not unique.
        eg.
            "a" ==> True
            "ba" ==> True
            "abb" ==> False
    """

    if len(s) == 1:
        return True
    else:
        #This results in TypeError: '>' not supported between instances of 'generator' and 'int'
        # if (s.count(c) for c in s) > 1:
        
        #This results in a false positive because it returns True if the first character is not followed by itself
        # for c in s:
        #     count = s.count(c)

        #Create a dictionary object where key is the count of each character in string and value is character
        d = {s.count(c): c for c in s}
        #If there are unique characters in the string, the length of set(d) is always 1
        if len(set(d)) > 1:
            return False
        else:
            return True

#The above function can be revised further.
#We know that the length of the string will always equal the length of the set of string

def is_unique2(s):
    """Returns True if characters in s are unique. Returns false if not unique.
        eg.
            "a" ==> True
            "ba" ==> True
            "abb" ==> False
    """

    if len(s) == len(set(s)):
        return True
    else:
        return False