def one_edit_away(s1, s2):
    """Returns True if s2 is one edit (modify, remove, add) away from s1."""

    #Reassign lists such that s_long is the longer, s_short is the shorter string
    if len(s1) >= len(s2):
        s_long = s1
        s_short = s2
    else:
        s_long = s2
        s_short = s1

    #Determine if absolute diff between length of lists is > 1
    if len(s_long) - len(s_short) > 1:
        return False
    else:
        if len(s_long) - len(s_short) == 1:
            #Check that s_short in s_long
            if s_short in s_long:
                return True
        elif len(s_long) == len(s_short):
            new_string = ''
            s_short = set(s_short)
            for c in s_long:
                if c in s_short:
                    new_string += c

    if len(s1) - len(new_string) == 1:
        return True
    else:
        return False