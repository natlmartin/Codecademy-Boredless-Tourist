letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Inclue lowercase letters in letter list
letters += [
  letter.lower() for letter in letters
]
# Duplicate points to account for lowercase letters
points *= 2

# Combine letters and points lists into dict
letter_to_points = {key:value for key, value in zip(letters, points)}

# Account for blank tiles 
letter_to_points[" "] = 0

# Return point total for a word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")

print(brownie_points)

# Generate scores for game 
player_to_words = {"player1": ["BLUE", "TENNIS", "MACHINE"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

# Add another word as a value to a specified player key
def play_word(player, word):
  player_to_words[player].append(word)

play_word("player1", "CODE")
print(player_to_words)

# Generate total score for each player
# Calculate score for each word and add as a value to player key in player_to_points
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

update_point_totals()
print(player_to_points)