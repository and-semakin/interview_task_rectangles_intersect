"""Решение задачи с собеседования про пересечение двух прямоугольников.

Формулировка задачи:
Имеются два прямоугольника, стороны которых параллельны координатным осям X и Y.
Нужно найти пересечение двух прямоугольников, если оно существует.
"""

from typing import Optional, Tuple, NamedTuple


class Rectangle(NamedTuple):
    """Прямоугольник со сторонами, параллельными координатным осям.

    Такой прямоугольник можно задать двумя координатами двух точек,
    например, левой нижней (x1, y1) и правой верхей (x2, y2).
    """
    x1: float
    y1: float
    x2: float
    y2: float

    @property
    def is_correct(self):
        """Проверить, задают ли указанные точки правильный прямоугольник.

        Точку тоже считаем правильным прямоугольником.
        """
        return self.x1 <= self.x2 and self.y1 <= self.y2


def intersect_section(a1: float, a2: float, b1: float, b2: float) -> Optional[Tuple[float, float]]:
    """Пересечь два отрезка: A (a1, a2) и B (b1, b2)."""
    if not (a1 <= a2 and b1 <= b2):
        raise ValueError('Переданные отрезки не являются правильными, невозможно вычислить пересечение.')

    if a2 < b1 or b2 < a1:
        return None

    sorted_coords = list(sorted([a1, a2, b1, b2]))
    return sorted_coords[1], sorted_coords[2]


def intersect_rectangles(a: Rectangle, b: Rectangle) -> Optional[Rectangle]:
    """Пересечь два прямоугольника."""
    if not (a.is_correct and b.is_correct):
        raise ValueError('Переданные прямоугольники не являются правильными, невозможно вычислить пересечение.')

    x_intersection = intersect_section(a.x1, a.x2, b.x1, b.x2)
    y_intersection = intersect_section(a.y1, a.y2, b.y1, b.y2)

    if not (x_intersection and y_intersection):
        return None

    return Rectangle(
        x_intersection[0],
        y_intersection[0],
        x_intersection[1],
        y_intersection[1]
    )
