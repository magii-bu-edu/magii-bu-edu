import random

def get_random_word():
    with open("words.txt") as file:
        return random.choice(list(file))[:-1].lower()

def play_unscramble():

    while True:
        summer_word = get_random_word()
        print(summer_word)
        break


#introduction()
play_unscramble()