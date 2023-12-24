import random


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
    while True:
        try:
            string = input(text)
            points = []
            for point_str in string.split():
                x, y = map(float, point_str.split(','))
                points.append((x, y))
            return points
        except ValueError:
            print('Ошибка ввода. Попробуйте снова.')


def output_points(points):
    """
    Функция вывода точек на экран
    :param points: список точек
    """
    for point in points:
        print(f"({point[0]}, {point[1]})")


def start_task9():
    pass





