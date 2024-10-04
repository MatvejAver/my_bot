import random

alf = []

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>1234567890`qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBN|"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def gen_word():
    return random.choice(alf)

def new_word(message):
    alf.append(message)
