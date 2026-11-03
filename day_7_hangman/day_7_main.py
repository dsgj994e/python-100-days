#word generated -> split into a list -> for each letter in letters: print("_")
# player input = user_guess -> for each letter in letters: if user_guess == letter: 
# print letter, elif/else: print("_")
#   ____
#  |    |
#  |    0
#  |   /|\
#  |   / \
#__|______
import random
guesses = []
tries = 0
blank = "_"
word_bank = ["airplane","golfball","picnic","bedtime","pencil","smelly","elephant","vehicle","chicago","storage"]
random_word = random.choice(word_bank)
word_list = []
blanks_list = []
word_len = len(random_word)
for num in range(1,word_len+1):
    blanks_list.append("_")
blanks = " ".join(blanks_list)
print(blanks)
still_blanks = blank in blanks_list
stages = ['''   ____
  |    |
  |    
  |    
  |    
__|______''','''   ____
  |    |
  |    0
  |    
  |    
__|______''','''   ____
  |    |
  |    0
  |    |
  |    
__|______''','''   ____
  |    |
  |    0
  |   /|
  |    
__|______''',r'''   ____
  |    |
  |    0
  |   /|\
  |    
__|______''',r'''   ____
  |    |
  |    0
  |   /|\
  |   / 
__|______
    ''',r'''   ____
  |    |
  |    0
  |   /|\
  |   / \
__|______''']
while still_blanks == True and tries <6:
    
    n = 0
    print(stages[tries])
    user_input = input("Guess a letter\n: ").lower()
    if user_input in guesses:
        print("You already guessed that")
        print(blanks)
    else:

        for char in blanks_list:
        
            if user_input == random_word[n]:
                blanks_list[n] = user_input
                n+=1
                still_blanks = blank in blanks_list
         
            else:
                n+=1
        guesses.append(user_input)
        if user_input not in blanks_list:
            tries += 1
        blanks = " ".join(blanks_list)
        print(blanks)
if still_blanks == True:
    print(stages[tries])
    print(f"The word was: {random_word}")
    print("YOU LOSE")
else:
    print("YOU WIN")