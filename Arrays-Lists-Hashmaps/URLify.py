# Write a method to replace all spaces in a string with '%20'.
# Assumptions:
# - String has sufficient space at the end to hold the additional chars
# - You're given the 'true' length of the string

def URLify(s):
    """Replaces all spaces in a string with '%20'. Does not count insignificant spaces.
        eg.
            'Mr John Smith   ' ==> 'Mr%20John%20Smith'
    """

    result = []

    #When splitting on a space, " ", comes back as an empty list
    for c in s.split(" "):
        if len(c) > 1:
            result.append(c)

    return '%20'.join(result)