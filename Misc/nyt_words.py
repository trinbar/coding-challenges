def find_number_of_words(wordlist, puzzles):
     """ 
     Returns a list of word matches between wordlist and puzzles. 
     Based on NYT Spelling Bee game.

     Args:
          wordlist (lst): 
               - First parameter; a list of words in which to check against 
                    second parameter, puzzles. 
               - Must be at least 5 characters in length.
               - All capital letters.

          puzzles (lst):
               - Second parameter; a list of letters by which to check wordlist.
               - Seven characters in length.
               - Key is the first character of each puzzle, and must be included
                    in the word being checked against.
               - All capital letters.

     Returns:
          A list of integers indicating how many words in the wordlist can a
               puzzle in puzzles spell.

     """

     # create a new list variable from wordlist
     # such that each word is a set of letters
     wordset = [''.join(set(word)) for word in wordlist]

     # create an empty list in which to capture word counts
     answer_list = []

     for p in puzzles:
          # initialize a count, break up each puzzle into its key and remaining letters
          count = 0
          key = p[0]
          value = p[1:]
          for word in wordset:
               # key must exist in word
               # if the key exists in word, remove key from word to make a subword
               if key in word:
                    subword = ''.join(sorted(word.replace(key,'')))
                    value = ''.join(sorted(value))
                    if subword in value:
                         count += 1

          # return a count for each puzzle, therefore append to answer_list
          #  outside of inner for loop
          answer_list.append(count)

     return answer_list