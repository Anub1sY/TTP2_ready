import random
import math
from os import system


def distance(point1, point2):
    """
    Функция рассчёта расстояния между точками
    :param point1: Первая точка
    :param point2: Вторая точка
    :return: Расстояние между точками
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def add_nearest_points(points):
    """
    Функция принимает список точек в качестве аргумента,
    в котором каждая точка будет добавлена к координатам ближайшей другой точки
    :param points: Список точек
    :return: Возвращает новый список точек
    """
    return [(point[0] + min((p for p in points if p != point),
            key=lambda p: distance(point, p))[0],
            point[1] + min((p for p in points if p != point),
            key=lambda p: distance(point, p))[1]) for point in points]


def input_points():
    """
    Функция ввода точек на двумерной плоскости
    :return: Возвращает список точек
    """
    num_points = int(input('Введите количество точек: '))
    points = []
    while True:
        for i in range(num_points):
            try:
                x = int(input(f'Введите x-координату точки {i + 1}: '))
                y = int(input(f'Введите y-координату точки {i + 1}: '))
                points.append((x, y))
            except ValueError:
                print('Ошибка ввода. Попробуйте снова')
                return None
        return points


def generate_points(num_points):
    """
    Функция генерирует случайные точки на двумерной плоскости
    :param num_points: Принимает на вход число точек, которые нужно сгенерировать
    :return: Возвращает сгенерированный список точек
    """
    while True:
        try:
            a = int(input('Введите минимальное значение чисел: '))
            b = int(input('Введите максимальное значение чисел: '))
        except ValueError:
            print('Ошибка ввода. Попробуйте снова')
            return None
        return [(random.randint(a, b), random.randint(a, b)) for _ in range(num_points)]


def output_points(points):
    """
    Функция вывода двумерного списка
    :param points: Принимает список значений вида (x, y)
    """
    for n, point in enumerate(points):
        print(f'Точка {n + 1}: ({point[0]}, {point[1]})')


def start_task7():
    points = []

    while True:
        print('Меню задания 1:'
              '\n1. Условие задачи'
              '\n2. Ввести массивы вручную'
              '\n3. Заполнить массивы случайными числами'
              '\n4. Вывод результата'
              '\n5. Выход')

        menu_point = input('\nВведите пункт меню: ')

        if menu_point == '1':
            system('cls')
            print('Входные данные: массив из точек с двумя координатами ((1, 2), (2, 3) …). '
                  'Требуется вернуть массив, в котором к каждой точке будет прибавлена другая, ближайшая точка.')
            system('pause')

        if menu_point == '2':
            system('cls')
            points = input_points()

            if points is not None:
                print(f'Точки введены:')
                output_points(points)
                system('pause')

        if menu_point == '3':
            system('cls')
            num_points = int(input('Введите количество точек: '))
            points = generate_points(num_points)

            print(f'Точки сгенрированы:')
            output_points(points)
            system('pause')

        if menu_point == '4':
            system('cls')
            if not points:
                print('Ошибка: Сначала введите или сгенерируйте массив.')
                system('pause')
            else:
                points = add_nearest_points(points)
                print('Результат:')
                output_points(points)
                system('pause')
                system('cls')

        if menu_point == '5':
            break
