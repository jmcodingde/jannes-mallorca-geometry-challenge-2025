import math
from dataclasses import dataclass
from typing import Self


@dataclass
class Point:
    x: float
    y: float

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def distance(self, Point):
        return math.sqrt((self.x - Point.x) ** 2 + (self.y - Point.y) ** 2)


@dataclass
class Circle:
    c: Point
    r: float

    def intersect(self, k: float, b: float) -> list[Point]:
        """Intersection with a non-trivial line"""
        # We are basically solving the quadratic equation with pre-calculated coefficients (A*x^2 + B*x + C = 0)
        A = 1 + k ** 2
        B = 2 * k * (b - self.c.y) - 2 * self.c.x
        C = self.c.x ** 2 + (b - self.c.y) ** 2 - self.r ** 2
        D = B ** 2 - 4 * A * C

        if D < 0:
            raise ValueError("No solutions for given parameters #1")
        elif D == 0:
            x = -B / (2 * A)
            y = k * x + b
            return [Point(x, y)]
        else:
            x1 = (-B + math.sqrt(D)) / (2 * A)
            y1 = k * x1 + b
            x2 = (-B - math.sqrt(D)) / (2 * A)
            y2 = k * x2 + b
            return [Point(x1, y1), Point(x2, y2)]

    def intersect_vertical(self, x: float) -> list[Point]:
        """Intersection with a vertical line"""
        y = math.sqrt(self.r ** 2 - (x - self.c.x) ** 2) + self.c.y
        return [Point(x, y)]


def calculate_length_r(alpha_degrees: float, n: float, g: float, i: float, j: float, k: float, s: float) -> float:
    """
    Calculate the length of side r based on the given angle alpha and constants.

    Args:
        alpha_degrees (float): The angle alpha in degrees
        n (float): Constant n from the construction
        g (float): Constant g from the construction
        i (float): Constant i from the construction
        j (float): Constant j from the construction
        k (float): Constant k from the construction
        s (float): Constant s from the construction

    Returns:
        float: The calculated length of side r

    Note: This is a placeholder implementation that doesn't solve the actual problem.
    Participants need to implement the correct formula.
    """

    G = Point(0, i)
    E = Point(-j, k)

    cos = math.cos(math.radians(alpha_degrees - 90))
    sin = math.sin(math.radians(alpha_degrees - 90))

    # Step 1: find H and I coordinates based on alpha
    H = G + Point(-g * cos, g * sin)
    I = H + Point(-sin, -cos)

    # Step 2: make a formula for a circle with E as the center
    circle_E = Circle(E, s)

    # Step 3: find the intersection of the circle with the line passing through I and our target point L
    # Note: the choice of the threshold here is very much debatable
    if abs(cos) >= 1e-5:
        # Line params for R-line
        k_coef = - sin / cos
        b_coef = I.y - k_coef * I.x

        points = circle_E.intersect(k_coef, b_coef)
    else:
        # vertical line
        points = circle_E.intersect_vertical(I.x)

    # Step 4: find the distance from I to the intersection point L - it is our desired r value
    # Note: when there are two intersection points, we take the one that is closer to I - that is by the problem design
    r = min([p.distance(I) for p in points])

    return r

def calculate_alpha_degrees(r: float, n: float, g: float, i: float, j: float, k: float, s: float) -> float:
    """
    Calculate the angle alpha in degrees based on the given length r and constants.

    Args:
        r (float): The length of side r
        n (float): Constant n from the construction
        g (float): Constant g from the construction
        i (float): Constant i from the construction
        j (float): Constant j from the construction
        k (float): Constant k from the construction
        s (float): Constant s from the construction

    Returns:
        float: The calculated angle alpha in degrees

    Note: This is a placeholder implementation that doesn't solve the actual problem.
    Participants need to implement the correct formula.
    """
    # This is a placeholder formula that will fail the tests
    return 90  # This is intentionally incorrect
