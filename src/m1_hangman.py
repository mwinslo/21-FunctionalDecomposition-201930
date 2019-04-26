"""
Hangman.

Authors: Montgomery Winslow and Micah Fletcher.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
import random


def min_length():
    min = int(input('What MINIMUM length do you want for the secret word? '))
    return min

def random_word(min):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        while True:
            r = random.randrange(0, len(words))
            if len(words[r]) >= min:
                break
        chosen = words[r]
        list = []
        for k in range(len(chosen)):
           list = list + [chosen[k]]
        return list


def secret_word(word):
    secret = word
    shown = []
    for k in range(len(secret)):
        shown = shown + ['-']
    return shown


def user_guess():
    guess = input('What letter do you want to try? ')
    return guess


def compare_guess(secret_word):
    total = []
    guess = user_guess()
    for k in range(len(secret_word)):
        if guess == secret_word[k]:
            total = total + [k]
    if total == []:
        return guess
    return total


def replace_dash(word, list, shown):
    for k in range(len(list)):
        shown[list[k]] = word[list[k]]

    return shown


def list_to_string(list):
    string = ''
    for k in range(len(list)):
        string = string + list[k]
    return string


def check_win(shown):
    for k in range(len(shown)):
        if shown[k] == '-':
            return False
    print('win')
    return True


def choose_lost():
    lost = input('How many unsuccessful choices do you want to allow yourself? ')
    lost = int(lost)
    return lost


def check_lost(lose, lost, word):
    if lose > lost:
        print()
        print('You lose! The secret word was:  {}'.format(list_to_string(word)))
        return True

def endgame():
    print()
    replay = input('Play another game? (y/n) ')
    print()
    if replay == 'y':
        main()
    if replay == 'n':
        print('Thanks for playing Hangman!')

def main():
    print("I will choose a random secret word from a dictionary.")
    print("You set the MINIMUM length of that word.")
    print()
    min = min_length()
    print()
    word = random_word(min)
    shown = secret_word(word)
    print('You set the DIFFICULTY of the game by setting the')
    print('number of UNSUCCESSFUL choices you can make before you')
    print('LOSE the game.  The traditional form of Hangman sets this')
    print('number to 5.')
    print()
    lose = 0
    lost = choose_lost()
    while True:
        print()
        print('Here is what you know about the secret word:')
        print(list_to_string(shown))
        print()
        compared = compare_guess(word)
        if type(compared) != list:
            lose = lose + 1
            if check_lost(lose, lost, word):
                break
            print()
            print('Sorry!  There are no  {}  letters in the secret word.'.format(compared))
            print('You still have  {}  unsuccessful guesses left before you LOSE'.format(lost - lose))
            print('the game!')
        else:
            print()
            print('Good guess!  You still have  {}  unsuccessful guesses'.format(lost - lose))
            print('left before you LOSE the game!')
            shown = replace_dash(word, compared, shown)
            if check_win(shown):
                break
    endgame()



####### Do NOT attempt this assignment before class! #######


# def test_random_word():
    # print(random_word()[0])
    # print(random_word())
    # print(random_word())
    # print(random_word())


def test_secret_word():
    print('test secret word')
    # word = random_word()
    # print(word)
    # print(secret_word(word))

#compare_guess('aaad')

# test
def test_replace_dash():
    print(replace_dash(['a', 'd', 'a', 'd', 'a', 'd'], [0, 2, 4], ['-', '-', '-', '-', '-', '-']))


def test_list_to_string():
    print(list_to_string(['a', 'd', 'a', 'd', 'a', 'd']))

# test_random_word()
# test_secret_word()
# test_replace_dash()
# test_list_to_string()


main()

