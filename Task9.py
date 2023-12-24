import random
from os import system


def check_distance(point1, point2):
    """
    функция для вычисления расстояния между точками
    :param point1: Первая точка
    :param point2: Вторая точка
    :return: Возвращает расстояние между двумя точками
    """
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def is_points_distance(array1, array2, distance):
    """
    Функция для находения точек, расстояние между которыми больше заданного числа
    :param array1: Первая точка
    :param array2: Вторая точка
    :param distance: Расстояние между точками
    :return: возвращает список точек
    """
    result_points = []
    for point1, point2 in zip(array1, array2):
        if check_distance(point1, point2) > distance:
            result_points.append((point1, point2))
    return result_points


def input_points(text):
    """
    Функция ввода массива точек
    :param text: Текст для рекомендации ввода
    :return: Возвращает список точек
    """
    num = int(input(text))
    points = []
    while True:
        for i in range(num):
            try:
                x = int(input(f'Введите x-координату точки {i + 1}: '))
                y = int(input(f'Введите y-координату точки {i + 1}: '))
                points.append((x, y))
            except ValueError:
                print('Ошибка ввода. Попробуйте снова')
                return None
        return points


def generate_array(size):
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


def generate_random_points(minv, maxv, size):
    return [(random.randint(minv, maxv), random.randint(minv, maxv)) for _ in range(size)]


def start_task9():
    array1 = []
    array2 = []
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
            system('cls')
            print('\nВходные данные: 2 массива с точками и число. Требуется вывести точки из первого и' 
                  '\nвторого массивов, расстояния между которыми больше заданного числа. Расстояния' 
                  '\nсчитаются только для соответствующих чисел.')
            system('pause')

        elif menu_point == '2':
            array1 = input_points('Введите количество точек первого массива: ')
            array2 = input_points('Введите количество точек второго массива: ')
            system('cls')

            print('Первый список: ', array1)
            print('Второй список: ', array2)
            system('pause')
            system('cls')

        elif menu_point == '3':
            system('cls')
            size = int(input('Введите размер массивов точек: '))
            min_value = int(input('Введите минимальное значение координат точек: '))
            max_value = int(input('Введите максимальное значение координат точек: '))

            array1 = generate_random_points(min_value, max_value, size)
            array2 = generate_random_points(min_value, max_value, size)

            print('Первый список: ', array1)
            print('Второй список: ', array2)
            system('pause')
            system('cls')

        elif menu_point == '4':
            system('cls')
            if 'array1' not in locals() and 'array2' not in locals():
                print('Ошибка. Сначала введите или сгенерируйте массивы.')
                system('pause')
                continue
            else:
                distance = float(input('Введите число, расстония между точками: '))
                result = is_points_distance(array1, array2, distance)
                print(f'Числа, подходящие под условие: {result}')
                system('pause')

        elif menu_point == '5':
            system('cls')
            break

        else:
            print('Ошибка ввода. Попробуйте ещё раз.')
            system('pause')

start_task9()