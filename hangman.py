import random

def hangman():
    words = ['python', 'hangman', 'programming', 'computer', 'science', 'code']
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while True:
        print('\n')
        display_word = ''
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += '_ '

        print(display_word)
        if display_word == word:
            print('Congratulations! You guessed the word correctly.')
            break

        if attempts == 0:
            print('Game Over. The word was:', word)
            break

        print('Attempts Left:', attempts)
        guess = input('Enter a letter: ').lower()

        if len(guess) != 1:
            print('Please enter a single letter.')
            continue

        if guess in guessed_letters:
            print('You have already guessed that letter.')
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print('Wrong guess!')

hangman()
