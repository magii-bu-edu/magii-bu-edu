import random

def get_random_word():
    with open("words.txt") as file:
        return random.choice(list(file))[:-1].lower()
    
print(get_random_word())