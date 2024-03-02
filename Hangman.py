import random

words = ['python','java','javascript','hacking','html','css']
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]#creates a list of '_'

attempts = 8 #number of allowed attempts

print("Welcome to Hangman")

while attempts>0 and '_' in word_display:
    print('\n'+' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):#returns index,item pairs of chosen word
            if letter == guess:
                word_display[index] = guess

    else:
        print("That letter doesn't appear in the word...idiot!!")
        attempts -=1

if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print('You ran out of attempts .. the word was : '+chosen_word)
    print('you lost!!')
