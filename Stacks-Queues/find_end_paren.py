def find_end_paren(s,position):
    """Given a string and index of open paren, return index of closing paren."""

    #>=1 means true, 0 means no
    in_paren = 0

    for i in range(s[position], len(s)+1):
        if i == '(':
            in_paren += 1
        elif i == ')':
            in_paren -= 0
            if in_paren == 0:
                return i
        else:
            return("No accompanying parenthesis. Please review.")
                