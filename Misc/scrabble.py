#Given letters and points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4,
 8, 4, 10]

#Use a list comprehension and zip to create a dictionary that has elements of 
#  letters as the keys and the elements of points as the values
letter_to_points = {letter:point for letter, point in zip(letters, points)}

#Add blank tiles
letter_to_points.update({" ": 0})

#Define a fn that takes in a word and returns how many points it's worth
def score_word(word):
    """Returns number of points in a word."""
  
    #Format word to all uppercase
    word = word.upper()
  
    #Initialize point_total
    point_total = 0
  
    #For loop that iterates through word and adds point to point_total
    for c in word:
        point_total += letter_to_points.get(c,0)
    
    #Return point_total
    return point_total

#Test with variable called brownie_points and set it equal to the value 
#  returned by score_word() fn with an input of "BROWNIE"
brownie_points = score_word("BROWNIE")
print(brownie_points)

#Create a dictionary called player_to_words that maps players 
#to a list of the words they've played
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], 
"wordNerd": ["EARTH", "EYES", "MACHINE"], 
"Lexi Con": ["ERASER", "BELLY", "HUSKY"], 
"Prof Reader": ["ZAP", "COMA", "PERIOD"]}

#Create an empty dictionary called player_to_points
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)