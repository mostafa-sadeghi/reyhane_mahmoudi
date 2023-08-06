import string
from random import shuffle

MAXGUSSES = 10


def create_secret_phrase(phrase, num_of_digits=3):
    digits = list(phrase)
    shuffle(digits)
    return "".join(digits[:num_of_digits])


def compare_digits(sec, g):
    res = ""
    if sec == g:
        return "You Won!!"
    for i in range(len(g)):
        if g[i] == sec[i]:
            res += "CC, "
        elif g[i] in sec:
            res += "CN, "
    if len(res):
        return res
    return "NN"


while True:
    secret_number = create_secret_phrase(string.digits)
    print("secret number is generated!")
    user_times = 0
    while user_times < MAXGUSSES:
        print(f"Guess #{user_times + 1}")
        user_input = ""
        while (not user_input.isdecimal()) or len(user_input) != 3:
            user_input = input("Enter your guess: ")
        result = compare_digits(secret_number, user_input)
        print(result)
        if user_input == secret_number:
            break

        user_times += 1
    if user_input != secret_number:
        print("Sorry, you losed!!!")
    print("Do you want To continue ('y|n') ? ")
    user_choice = input("> ")
    if user_choice.lower().startswith("y"):
        continue
    else:
        print("Bye...")
        break
