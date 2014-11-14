#! /usr/bin/env python3
# coding: utf-8
import random


def triangle(n):
    for i in range(n):
        print((i+1) * '*')


def color_text(text):
    colors = ['\033[95m', '\033[94m', '\033[92m', '\033[93m', '\033[91m']
    ENDC = '\033[0m'
    
    words = text.split()
    res = ''
    
    for word in words:
        word = random.choice(colors) + word + ENDC + ' '
        res += word
    
    return res


def freq(text):
    res = {}
    for word in text.split():
        try:
            res[word] += 1
        except KeyError:
            res[word] = 1
    
    return res


def hello(code):
    if code == 'be':
        return 'Вітаю!'
    elif code == 'en':
        return 'Hello!'
    elif code == 'ru':
        return 'Привет!'
    elif code == 'de':
        return 'Hallo!'


text = 'If you are going to get complicated with this (and it sounds like you are if you are writing a game), you should look into the "curses" module, which handles a lot of the complicated parts of this for you. The Python Curses HowTO is a good introduction.'


#~ triangle(5)
#~ text = color_text(text)
#~ text = freq(text)
text = hello('be')
print(text)
