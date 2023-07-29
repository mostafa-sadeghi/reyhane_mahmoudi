from rock_utils import get_user_choice, get_system_choice, find_winner


def play():
    result = {
        'user': 0,
        'system': 0
    }
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)
        # TODO