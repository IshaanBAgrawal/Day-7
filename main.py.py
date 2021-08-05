#Step 5

import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
chosen_word_len = len(chosen_word)

lives = 6

print(hangman_art.logo)

#Create blanks
display = []
for blanks in range(0, chosen_word_len):
  display += "_"

# Making chosen_word a list
chosen_word_list = []
for word in range(chosen_word_len):
  chosen_word_list += chosen_word[word]

already_entered_letters = []

# Defining the Word Guesser Function
def word_guess():
  global lives
  global already_entered_letters
  print(f"You have {lives} lives.")
  guess = input("Guess a letter: ").lower()

  if guess in already_entered_letters:
    print(f"You have already entered {guess}")
  else:
    already_entered_letters += guess

  #Check guessed letter
  replacement = 0
  true_or_false = ""
  for letter in chosen_word:
    if letter == guess:
      true_or_false = True
      display[replacement] = chosen_word[replacement]
      replacement += 1
    else:
      true_or_false = False
      replacement += 1

  if not guess in chosen_word:
    print(f"'{guess}' is not in the word.")
  print(display)

  if not guess in chosen_word:
    lives -= 1

while display != chosen_word_list and lives != 0:
  word_guess()
  if lives == 6:
    print(hangman_art.stages[6])
  elif lives == 5:
    print(hangman_art.stages[5])
  elif lives == 4:
    print(hangman_art.stages[4])
  elif lives == 3:
    print(hangman_art.stages[3])
  elif lives == 2:
    print(hangman_art.stages[2])
  elif lives == 1:
    print(hangman_art.stages[1])
  else:
    print(hangman_art.stages[0])


if display == chosen_word_list:
  print("You Win.")
elif lives == 0:
  print(f"You Lose. The word was {chosen_word}.")
