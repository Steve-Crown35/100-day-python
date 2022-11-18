import random
from hangman_art import hangman, art
from Hangman_words import words
hangman_design = art
print("WELCOME TO HANGMAN WORD GAME!")
print(hangman_design)
stages = hangman
word_list = words
underscore = []
random_number = random.randint(0, len(word_list)-1)
random_word = word_list[random_number]
life = 6
letter = []
#print(random_word)
for i in random_word:
    underscore.append("_")
place_holder = underscore
while "_" in place_holder and life != 0:
     guess_letter = input("Guess a letter:  ").lower()
     while guess_letter in letter:  
          print(f"{guess_letter} already guessed. please guess again.")
          print(place_holder)
          guess_letter = input("Guess a letter:  ").lower()
     if guess_letter in random_word:
          letter.append(guess_letter)

     for i in range(len(random_word)):
          if guess_letter == random_word[i]:
               place_holder[i] = guess_letter        
               print(place_holder)
     if guess_letter not in random_word: 
        life -= 1
        stage = stages[life]
        print(f"You guessed the letter {guess_letter}. {guess_letter} is not in the word. You lose a life")
        print(stage)  
if "_" not in place_holder:
    print("Congratulations! You won.") 
else:
    print(f"You lose. The word is {random_word}")     
    




    









