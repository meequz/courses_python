#! /usr/bin/env python3
# coding: utf-8


def rhombus(n):
    if n % 2 == 0:
        return 'n is not odd!'
    
    res = []
    for i in range(n//2 + 1):
        spaces = (n//2 + 1) - i
        stars = i*2 + 1
        res.append(' '*spaces + '*'*stars)
    
    rest = list(reversed(res[:n//2]))
    res.extend(rest)
    res = '\n'.join(res)
    
    return res


def simple_wrap(text, max_len):
    words = text.split()
    res = '\n'
    
    for word in words:
        last_n = len(res) - res[::-1].find('\n')
        
        if len(res[last_n:]) + len(word) + 1 > max_len:
            res += '\n'
        
        res += word + ' '
    
    return res[1:]
    


text = 'If you are going to get complicated with this (and it sounds like you are if you are writing a game), you should look into the "curses" module, which handles a lot of the complicated parts of this for you. The Python Curses HowTO is a good introduction.'

#~ text = rhombus(9)
text = simple_wrap(text, 29)
print(text)
