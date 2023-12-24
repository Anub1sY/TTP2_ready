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
    return 0


def generate_points(num_points):
    return 0


def output_points(points):
    pass


def start_task7():
    pass
