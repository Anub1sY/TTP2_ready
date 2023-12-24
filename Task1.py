import random
from os import system


def sum_sorted_arrays(array1, array2):
    """
    Функция реализующая сортировку первого входного массива по убыванию,
    второго входного массива по возрастанию. Далее два массива суммируются
    между собой, при этом если их элементы совпадают будет сумма будет
    равна 0.
    :param arr1: Первый массив
    :param arr2: Второй массив
    :return: Возвращает результат работы функции
    """

    sorted_arr1 = sorted(array1, reverse=True)
    sorted_arr2 = sorted(array2)

    print('Первый массив, отсортирован по убыванию:', sorted_arr1,
          '\nВторой массив, отсортирован по возрастанию:', sorted_arr2)

    sum_result = []
    for x, y in zip(sorted_arr1, sorted_arr2):
        if x == y:
            sum_result.append(0)
        else:
            sum_result.append(x + y)

    sum_result.sort()

    return sum_result


def input_array(size):
    """
    Функция ввода списка с проверкой на вход, только
    целые значения.
    :param size: Количество элементов списка
    :return: Возвращает готовый список или выводит ошибку ввода
    и ничего не возвращает
    """

    try:
        array = []
        for _ in range(size):
            num = int(input('Введите число: '))
            array.append(num)
        return array
    except ValueError:
        print('Ошибка ввода. Попробуйте снова')
        return None


def generate_array(size):
    """
        Функция заполнения массива случайными значениями,
        в диапозоне который выбираете сами.
        :param size: Размер массива
        :return: Возвращает готовый список или выводит ошибку ввода
        и ничего не возвращает
        """

    while True:
        try:
            a = int(input('Введите минимальное значение чисел в массиве: '))
            b = int(input('Введите максимальное значение чисел в массиве: '))
        except ValueError:
            print('Ошибка ввода. Попробуйте снова')
            system('pause')
            system('cls')
            continue
        return [random.randint(a, b) for _ in range(size)]


def start_task1():
    pass
