"""
Your team is scrambling to decipher a recent message, worried it's a plot to 
break into a major European National Cake Vault. The message has been mostly 
deciphered, but all the words are backward! Your colleagues have handed off the 
last step to you.

Write a function reverse_words() that takes a message as a list of characters 
and reverses the order of the words in place. ↴
"""

def reverse_words(lst):
    """Returns a string that reverses the order of words in a list of chars."""

    #Create empty string
    temp_str = ""

    #Iterate through lst, pop off the first item and add to temp_str
    while len(lst) != 0:
        temp_str += lst.pop(0)
        
    #Split temp_str, reverse it, then join as one string
    return " ".join(temp_str.split()[::-1])


