"""
File: hangman.py
Name: Chance
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Define turns and play a guess word game
    If guess is not in answer, turns -1
    Turns = 0 or guess success -> Game Over
    (case-insensitive)
    """
    ans = random_word()
    guess_times = N_TURNS
    old_word = ''
    print('The word looks like ', end='')
    # old/new_word is dashed and print
    for i in range(len(ans)):
        old_word += '-'
    print(old_word)
    num_not_guess = len(ans)
    while True:
        # if no guess chance -> game over
        if guess_times == 0:
            print('You are completely hung')
            print('The word was: ' + ans)
            break
        # if guess all alphabet -> game over
        elif num_not_guess == 0:
            print('You are correct')
            print('You win!!')
            print('The word was: ' + ans)
            break
        new_word = ''
        print('You have ' + str(guess_times) + ' wrong guesses left.')
        # check whether guess alphabet is in ans.
        # Yes -> replace - from old_word to new_word
        while True:
            guess_word = input('Your guess: ')
            # Input format
            if len(guess_word) == 1 and guess_word.isalpha():
                break
            else:
                print('Illegal format.')
        # skip means after check whether guess alphabet is in ans
        skip = 1
        for i in range(len(ans)):
            if ans[i] == guess_word.upper():
                new_word += ans[i]
                skip = 0
                # origin is alphabet -> num_not_guess keep
                if old_word[i] == '-':
                    num_not_guess -= 1
            else:
                new_word += old_word[i]
        if skip == 1:
            guess_times -= 1
            print('There is no ' + guess_word.upper() + "'s in the world.")
        old_word = new_word
        # Give problem if game is not over
        if guess_times != 0 and num_not_guess != 0:
            print('The word looks like ' + str(new_word))


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
