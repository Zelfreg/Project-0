'''
lets make a deal: the minimum number allowed 1
                  the maximum one 100
'''
import numpy as np


def Vanga_foo(number: int) ->int:
    count = 0
    lower = 1           # as per deal above
    upper = 100         # as per deal above
    
    while True:
        count += 1
        predict = int((upper + lower) / 2) + 1
        if predict == number:   # got it!
            break
        elif number > predict:
            lower = predict     # adjusting boundaries
        else:
            upper = predict     # adjusting boundaries
    
    suffix_dictionary ={
        1: 'st',
        2: 'nd',
        3: 'rd'
    }
    suf = suffix_dictionary.get(count % 10, 'th')   # making result looks nicely
    return print(f"got {predict} on {count}{suf} attempt")


def num_gen() ->int:
    '''randomizing number as per dealed boundaries'''
    return int(np.random.randint(1, 101))


Vanga_foo(num_gen)
