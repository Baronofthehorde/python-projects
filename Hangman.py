#Python program to illistrate a hangman game
import random
from collections import Counter

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
# Randomly chooese a secrete word from our "someWords" list.
word = random.choice(someWords)

if __name__ == '__main__':
    print("Guess the word! HINT: word is a name of a fruit")

    for i in word:
        #For printing the empty spaces for Letters of the word
        print('_', end=' ')
    print()

    playing = True
    # List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances!= 0) and flag == 0: #flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            #validation of the guess
            if not guess.isalpha():
                print('enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # if the letter is guessed correctly
            if guess in word:
                #k stores the number of times the guessed letter occures in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess # The guessed letter is added as many times as it occurs
            
            #print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed)) != Counter(word):
                    print(char, end=' ')
                    correct += 1
                #if user has guessed all the letters / once the correct word is guessed fully
                elif (Counter(letterGuessed) == Counter(word)):
                    #the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(word)
                    flag=1
                    print('Congraatulations, You Win!')
                    break # To Break out of the For Loop
                    break # To break out of the while loop
                else:
                    print('_', end=' ')

        # IF user has used all of their chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try Again...')
            print('The word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')    