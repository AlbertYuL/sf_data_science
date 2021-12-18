    #"""Игра 'Угадай число'
#
    #Returns:
    #    за сколько раз в среднем за 1000 подходов угадывает число алгоритм
    #"""
#
import numpy


def predict(number):#алгоритм угадывания
    count = 0#количество попыток угадывания
    supposed_number = 50
    max_sup_num = 100
    min_sup_num = 2
    while True:
        count += 1
        if number == 1:
            break
        elif supposed_number == number:
            break
        elif supposed_number > number:
            max_sup_num = supposed_number
            supposed_number = round((max_sup_num + min_sup_num) / 2)
        elif supposed_number < number:
            min_sup_num = supposed_number
            supposed_number = round((max_sup_num + min_sup_num) / 2)
    return count

def score_game(predict):
    numpy.random.seed(1)
    random_array = numpy.random.randint(1, 101, size = (1000))
    count_list = []
    for number in random_array:
        count_list.append(predict(number))
    score = int(numpy.mean(count_list))
    print(f"Мой алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == '__main__':
    score_game(predict)



