#!/usr/bin/python3
def weight_average(my_list=[]):
    numerador = 0
    denominador = 0
    if my_list:
        for i in range(len(my_list)):
            numerador += my_list[i][0] * my_list[i][1]
            denominador += my_list[i][1]
        return (numerador / denominador)
    else:
        return 0
