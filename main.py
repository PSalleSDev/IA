from __future__ import annotations

from enum import Enum
from math import sqrt

"""
Proposta do arquivo é englobar todos os conceitos de Python básico.
abordados pelo orientador em um arquivo em viés de aplicabilidade.

O código reposiciona x pontos de uma lista dentro de um polígono alvo. Foi usado algoritmo de Ray Casting e distância euclidiana.
"""

class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    @staticmethod
    def distance(p1: Point, p2: Point) -> float:
        return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

class Poligon:
    class Where(Enum):
        In = "In"
        Out = "Out"

    def __init__(self, vertexs: list[Point]):
        self.vertexs: list[Point] = vertexs

    def where(self, point: Point) -> Poligon.Where:
        intersections: int = 0

        for i in range(len(self.vertexs)):
            a: Point = self.vertexs[i]
            b: Point = self.vertexs[(i + 1) % len(self.vertexs)]

            if ((a.y > point.y) != (b.y > point.y) and a.x + (point.y - a.y) * (b.x - a.x) / (b.y - a.y) > point.x):
                intersections += 1

        if intersections % 2:
            return self.Where.In

        return self.Where.Out

area: list[Point] = [
    Point(2, 1),
    Point(2, 4),
    Point(5, 4),
    Point(5, 1)
]

points: dict[str, Point] = {
    "A": Point(3, 3),
    "B": Point(1, 2)
}

poligon: Poligon = Poligon(area)

for name, point in points.items():
    print(f"Point {name}:{point.x, point.y} is {poligon.where(point).name} of poligon area")

    if poligon.where(point) == Poligon.Where.Out:
        target: tuple[Point, float] | None = None

        for i in range(len(area)):
            a: Point = area[i]
            b: Point = area[(i + 1) % len(area)]

            dx: float = b.x - a.x
            dy: float = b.y - a.y

            t: float = ((point.x - a.x) * dx + (point.y - a.y) * dy) / (dx**2 + dy**2)

            cpoint: Point = Point(
                a.x + t * dx,
                a.y + t * dy
            )

            candidate: tuple[Point, float] = (cpoint, Point.distance(point, cpoint))

            if target is None or candidate[1] < target[1]:
                target = candidate

        point.x = target[0].x
        point.y = target[0].y

        print(f"Point {name}:{point.x, point.y} is {poligon.where(point).name} of poligon area")
