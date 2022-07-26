from typing import List
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from scipy import constants

from .vector import Vector2D


def _valid_time_value(time: float) -> bool:
    """
    Checks whether the given time is a valid physical value
    :param time: time to check
    :return: returns True if valid and False otherwise
    """
    return (not np.iscomplex(time)) and (time > 0)


class ProjectileMotion:
    def __init__(self, initial_angle: float,
                 initial_height: float,
                 initial_velocity: float,
                 target_height: float = 0):

        self.initial_angle = initial_angle
        self.initial_height = initial_height
        self.initial_velocity = self._get_velocity_vector(velocity=initial_velocity)
        self.target_height = target_height

    def _get_velocity_vector(self, velocity: float) -> Vector2D:
        """
        Splits the given velocity to its X and Y components
        :param velocity: velocity magnitude
        :return: a Vector2D object representing the velocity
        """
        angle_in_radians = np.deg2rad(self.initial_angle)
        velocity_x = round(velocity * np.cos(angle_in_radians), 10)
        velocity_y = round(velocity * np.sin(angle_in_radians), 10)

        return Vector2D(x=velocity_x, y=velocity_y)

    def _get_time_in_air(self) -> List[float]:
        """
        Calculates the time an object was in the air until a given height
        :return list of all the possible time values
        """
        a = self.initial_height - self.target_height
        b = self.initial_velocity.y
        c = -(constants.g / 2)
        equation_roots = Polynomial([a, b, c]).roots()

        # Filter all non-physical values
        time_in_air = list(filter(_valid_time_value, equation_roots))
        if not time_in_air:
            raise Exception("No solutions")

        return time_in_air

    def calculate_positions(self) -> List[float]:
        """
        Calculates the possible positions of the object
        at a given height (Y value).
        It multiplies the time the object was in the air by its X axis velocity
        :return: returns a list of X axis positions in which the object was at
        the desired height
        """
        time_in_air = self._get_time_in_air()
        return [self.initial_velocity.x * time for time in time_in_air]

    def get_velocities(self) -> List[Vector2D]:
        """
        Calculates the velocities in which the object was in the desired height
        :return: a list of all the velocities
        """
        velocities = []
        for time in self._get_time_in_air():

            # The Y velocity at the given height
            y_velocity = self.initial_velocity.y - (constants.g * time)

            # The X velocity does not change throughout the flight
            velocities.append(Vector2D(x=self.initial_velocity.x, y=y_velocity))

        return velocities

    def calculate_angles(self) -> List[float]:
        """
        Calculates the angles at which the object was in the given height
        :return: returns a list of the angles
        """
        angles = []

        for velocity in self.get_velocities():
            if velocity.x == 0 or velocity.y == 0:
                angles.append(90)
            else:
                # tan(a) = Vy / Vx
                angle_radians = np.arctan(velocity.y / velocity.x)
                angles.append(np.rad2deg(angle_radians))

        return angles

