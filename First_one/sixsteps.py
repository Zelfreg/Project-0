"""some code"""
import numpy as np


def vanga_foo(number: int) -> int:
    """number searching

    Args:
        number (int): 1 <= number <= 100

    Returns:
        int: number of attempts
    """
    upper, lower, count = 100, 1, 0          
        
    while True:
        count += 1
        predict = int((upper + lower) / 2)
        if predict == number:  # got it!
            break
        elif number > predict and upper - lower > 1:
            lower = predict                        
        elif number < predict and upper - lower > 1:
            upper = predict                        
        else:
            count += 1 if number == lower else 2  # if number is equal to lower limit then plus one attempt, if no then
            break                                 # plus another one (ie 2)
            
    return count


def num_gen() -> np.array:
    """[summary]

    Returns:
        np.array: [description]
    """
    np.random.seed(1)  # set initial point for pseudo randomisation    
    return np.random.randint(1, 101, size=1000)


def get_av_attempt(ar: np.array) -> int:
    result = []
    
    for number in ar:    
        result.append(vanga_foo(number))
    
    return round(np.mean(result))


if __name__ == '__main__':
    print(get_av_attempt(num_gen()))
