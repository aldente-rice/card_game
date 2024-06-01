import random
import tkinter

MAX_HAND = 5
red_repeat = False
wildcard = False
used_w_cards = set()  # tracks the white cards used


# create a nested collection of all the players and cards (so like players, then the hands)
# to check if white cards has been used
# or just create a global hashset and check if it has been there or not

#
#################################################################
# a player that keeps track of their username, points, and hand #
#################################################################
class Player:
    def __init__(self, user_name, points):
        self.user_name = user_name
        self.points = points
        self.hand = []

    def play_card(self, play_white):
        self.hand.remove(play_white)

    def draw_white(self, hand):
        white_file = open('white_cards.txt', 'r', encoding='utf-8')
        read_white = white_file.readlines()

        curr_white = read_white[random.randint(0, 311)]
        while curr_white in used_w_cards:
            curr_white = read_white[random.randint(0, 311)]

        used_w_cards.add(curr_white)
        self.hand.append(curr_white)

        white_file.close()


###################################
# deal a red card                 #
# used at the start of each round #
###################################
def deal_red():
    used_cards = {}  # dictionary to track red card usage
    # if you want statistics at end of game, then can do hashmap (key, value)

    red_file = open('red_cards.txt', 'r', encoding='utf-8')
    read_red = red_file.readlines()  # reads all red cards
    curr_red = read_red[random.randint(0, 100)]  # selects a random red card

    # keep track of repeated cards
    if (curr_red in used_cards) and red_repeat:
        used_cards[curr_red] += 1  # if red already used, increment

        red_file.close()
        return curr_red
    else:
        while curr_red in used_cards:
            curr_red = read_red[random.randint(0, 100)]  # keep choosing until unique red card

        used_cards[curr_red] = 1

        red_file.close()
        return curr_red


# deals a user a hand of white cards (MAX_HAND # of cards)
def deal_full_white(player):
    white_file = open('white_cards.txt', 'r', encoding='utf-8')
    read_white = white_file.readlines()

    card_num = 0
    while card_num < MAX_HAND:  # picks a unique white card
        curr_card = read_white[random.randint(0, 311)]
        if curr_card not in used_w_cards:
            player.hand.append(curr_card+'[' + f"{(card_num + 1)}" + ']')
            used_w_cards.add(curr_card)
            card_num += 1

    white_file.close()


def play():
    game = tkinter.Tk()






