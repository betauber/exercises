import random


def roll_die(faces=6, seed=None):
    random.seed(seed)
    return random.randint(1,faces)


def roll_dice(count, faces=6, seed=None):
    return [roll_die(faces, seed) for x in range(count)]


def player_round(number=4):
    sum = 0


def multiplayer():
    for i in range(4):
        player_round(i)


def main_menu():
    while True:
        if x == 'n':
            multiplayer()
        elif x == 'q':
            break