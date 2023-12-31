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
    """
    Меню задания 1 с условиями его выполнения, а также
    пунктами с которыми можно работать.
    :return: Меню для работы, с кнопкой выхода из него.
    """

    while True:
        system('cls')
        print('Меню задания 1:'
              '\n1. Условие задачи'
              '\n2. Ввести массивы вручную'
              '\n3. Заполнить массивы случайными числами'
              '\n4. Вывод результата'
              '\n5. Выход')

        menu_point = input('\nВведите пункт меню:')

        if menu_point == '1':
            print('Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму\n'
                  'чисел из массивов, первый массив должен быть отсортирован в порядке убывания,\n'
                  'второй в порядке возрастания. Если числа в массивах совпадают, их сумма будет равна\n'
                  'нулю. Конечный массив нужно отсортировать в порядке возрастания.\n')
            system('pause')
            system('cls')

        elif menu_point == '2':
            system('cls')
            size = int(input("Введите размер массива: "))
            print('Первый массив:')
            arr1 = input_array(size)
            print('Второй массив:')
            arr2 = input_array(size)
            if arr1 is not None and arr2 is not None and len(arr1) == len(arr2):
                print('Первый массив до сортировки:', arr1,
                      '\nВторой массив до сортировки:', arr2)
                system('pause')

        elif menu_point == '3':
            system('cls')
            size = int(input("Введите размер массива: "))
            arr1 = generate_array(size)
            arr2 = generate_array(size)
            print('Массивы заполнены автоматически,'
                  '\nПервый массив до сортировки:', arr1,
                  '\nВторой массив до сортировки:', arr2)
            system('pause')

        elif menu_point == '4':
            system('cls')
            if 'arr1' not in locals() and 'arr2' not in locals():
                print('Ошибка: Сначала введите или сгенерируйте массивы.')
                system('pause')
                continue
            result = sum_sorted_arrays(arr1, arr2)
            print(f'Результат работы, отсортированный по возростанию {result}')
            system('pause')

        elif menu_point == '5':
            system('cls')
            break

        else:
            print('Ошибка ввода. Попробуйте ещё раз.')
            system('pause')
