from random import choice
from config import RULES, score_board, GAME_CHOICES


def get_user_choice() -> str:
    """
    get the user choice between rock, paper and scissors
    :return:user_input
    """
    user_input = input("Enter your choice please (r, p, s): ")
    if user_input not in GAME_CHOICES:
        print("Some thing wrong!!!")
        return get_user_choice()

    return user_input


def get_system_choice():
    return choice(GAME_CHOICES)


def find_winner(user_hand, system_hand):
    match = {user_hand, system_hand}
    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]
