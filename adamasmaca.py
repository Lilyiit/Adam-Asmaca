import os
clear=lambda: os.system('cls')
import random
from art import stages
end_of_game = False
from words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives=6
from art import logo
print(logo)



#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    
    for position in range(word_length): 
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("you lose")

    print(f"{''.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(stages[lives])       