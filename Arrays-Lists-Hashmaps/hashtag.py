#Given a hashtag string and a list of all possible words in the hashtag, 
# return a list of all the words in the hashtag

hashtag = "#lovedogsandcats"
all_words = ["love","dogs","and","cats"]

def all_words_in_hashtag(hashtag, all_words):
    """Given a hashtag string and a list of all possible words in the hashtag, 
        return a list of all the words in the hashtag.

        eg.
            "#lovedogsandcats" ==> ["love","dogs","and","cats"]
    """

    #Turn all_words into a set
    all_words = set(all_words)

    #Remove the octothorp
    if hashtag[0] == "#":
        hashtag = hashtag[1:]

    #Initiate an answer list
    answer = []

    #Iterate through hashtag to tokenize each word
    for c in hashtag:
        token = ""
        if token in all_words:
            answer.append(token)
        else:
            token += c

    return answer

