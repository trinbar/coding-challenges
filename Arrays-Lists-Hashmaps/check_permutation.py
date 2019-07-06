# Given two strings, write a method to decide if one is a permutation of the other
# Assumptions:
# If both empty strings, return True
# Any letter, symbol, int

def is_permutation(s1,s2):
    """Returns True if s1 is a permuation of s2.
        eg.
            "cat", "act" ==> True
            "dog", "pig" ==> False
            "","" ==> True
    """

    dict1 = {c:s1.count(c) for c in s1}
    dict2 = {d:s2.count(d) for d in s2}

    if dict1 == dict2:
        return True
    else:
        return False

# RT is O(N) because of for loops through strings s1 and s2 
