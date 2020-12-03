import string
import random

def gen_url():
    url = ''
    for i in range(4):
        url += random.choice(string.ascii_letters)
    return url
