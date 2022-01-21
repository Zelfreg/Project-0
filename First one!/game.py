import numpy as np


def random_predict(number: int=1) ->int:
    count = 0
    
    while True:
        count += 1
        predict = np.random.randint(1, 101)
        if number == predict:
            return count
        

def check(random_predict) ->int:
    count_list =[]
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=(1000))
    
    for x in random_array:
        count_list.append(random_predict(x))
        
    mean_attempt = int(np.mean(count_list))

    return print(mean_attempt)


if __name__ == '__main__':
    check(random_predict)
