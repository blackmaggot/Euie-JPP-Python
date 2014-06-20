__author__ = 'WiktorMarchewka'

# def arithmetic_mean():
#     numbers_list = (1, 4, 3, 6, 5, 3, 7, 5)
#     numbers_list_lenght = len(numbers_list)
#     arithmetic_mean =
class AritheticMean:
    numbers_list = (1, 4, 3, 6, 5, 3, 7, 5)

    def numbers_list_lenght(self):
        numbers_list_lenght = float(len(AritheticMean.numbers_list))
        return numbers_list_lenght
    def sum_of_numbers_list(self):
        sum_of_numbers_list = float(sum(AritheticMean.numbers_list))
        return sum_of_numbers_list


    def arithmetic_mean(self):
        instance_of_class = AritheticMean()
        arithmetic_mean = float((instance_of_class.sum_of_numbers_list())/(instance_of_class.numbers_list_lenght()))
        print(arithmetic_mean)
AR = AritheticMean()
AR.arithmetic_mean()