from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    """
    Harold is a kidnapper who wrote a ransom note, but now he is worried it
    will be traced back to him through his handwriting. He found a magazine
    and wants to know if he can cut out whole words from it and use them to
    create an untraceable replica of his ransom note. The words in his note
    are case-sensitive and he must use only whole words available in the
    magazine. He cannot use substrings or concatenation to create the words 
    he needs.

    Given the words in the magazine and the words in the ransom note, 
    print Yes if he can replicate his ransom note exactly using whole words 
    from the magazine; otherwise, print No.

    For example, the note is "Attack at dawn". The magazine contains only 
    "attack at dawn". The magazine has all the right words, but there's a 
    case mismatch. The answer is "No".

    Example 1:
        magazine = 'give me one grand today night'
        note = 'give one grand today'

        returns 'Yes'

    Example 2:
        magazine = 'two times three is not four'
        note = 'two times two is four'

        returns 'No'
    """

    #Initialize an empty dictionary to hold possible words
    wordbank = defaultdict(int)

    #Iterate through magazine (list)
    for m in magazine:
        #Check if m in wordbank doesn't exist
        if m not in wordbank:
            #Add m to the wordbank
            wordbank[m] = 0
        #Increase count of m in wordbank by 1
        wordbank[m] += 1

    #Iterate through note (list)
    for n in note:
        #Check if n is not in wordbank
        if not n in wordbank or wordbank[n] == 0:
            #If not, print "No" and return out of function
            print("No")
            return
        #Decrease wordbank by 1 - this will account for multiple n in notes
        wordbank[n] -= 1

    #Prints yes if can create note from magazine
    print("Yes")