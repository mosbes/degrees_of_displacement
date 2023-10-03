"""Module for calculate degrees of displacement."""
from math import pi

degree_all_circ = 360


def get_degree(time: float, acceleration: float, radius: float, speed: float | None = 0) -> int:
    """Get the degree of a given distance.

    Args:
        time (float): The time in seconds to travel that distance.
        acceleration (float): Acceleration in meters/(seconds in square) this distance.
        radius (float): The radius in meters of the circle.
        speed (float, optional): The speed in meters/seconds for distance. Defaults to 0.

    Returns:
        Degree of displacement
    """
    circ_len = 2 * pi * radius
    distance = speed * time + acceleration * (time ** 2) / 2
    degree = 0 if circ_len == 0 else distance % circ_len / circ_len * degree_all_circ

    return round(degree, 2)
