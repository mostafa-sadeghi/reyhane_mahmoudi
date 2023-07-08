import string
import random

import argparse


def create_password(length=8, upper=False, lower=False, digit=False, pun=False):
    pool = ''
    if upper:
        pool += string.ascii_uppercase  # pool = pool + string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits

    if pun:
        pool += string.punctuation

    if pool == '':
        pool = string.ascii_letters

    # password = ''
    # for char in random.choices(pool, k=length):
    #     password += char
    # return password

    return ''.join(random.choices(pool, k=length))


parser = argparse.ArgumentParser(description="Password creator")
parser.add_argument('length', type=int, help="Length of password")

args = parser.parse_args()