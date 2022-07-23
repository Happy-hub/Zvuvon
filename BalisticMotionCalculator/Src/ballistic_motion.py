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


class BallisticMotion:
    def __init__(self, initial_angle: float, initial_height: float, initial_velocity: float):
        self.initial_angle = initial_angle
        self.initial_height = initial_height
        self.initial_velocity = self._get_velocity_vector(velocity=initial_velocity)

    def _get_velocity_vector(self, velocity: float) -> Vector2D:
        """
        Splits the given velocity to it's X and Y components
        :param velocity: velocity magnitude
        :return: a Vector2D object representing the velocity
        """
        angle_in_radians = np.deg2rad(self.initial_angle)
        velocity_x = round(velocity * np.cos(angle_in_radians), 10)
        velocity_y = round(velocity * np.sin(angle_in_radians), 10)
        return Vector2D(x=velocity_x, y=velocity_y)

    def _get_time_in_air(self) -> List[float]:
        """
        Returns the total time the object was in the air i.e. time until impact
        :return list of all the possible time values
        """
        # 0 = h + v0.y * t - 0.5 * g * t^2
        a = self.initial_height
        b = self.initial_velocity.y
        c = -(constants.g / 2)
        equation_roots = Polynomial([a, b, c]).roots()
        # Filter all non-physical values
        time_in_air = list(filter(_valid_time_value, equation_roots))
        if not time_in_air:
            raise Exception("No solutions")
        return time_in_air

    def calculate_landing_position(self) -> List[float]:
        time_in_air = self._get_time_in_air()
        return [self.initial_velocity.x * time for time in time_in_air]

    def _get_landing_velocities(self) -> List[Vector2D]:
        landing_velocities = []
        for time in self._get_time_in_air():
            final_y_velocity = self.initial_velocity.y - (constants.g * time)
            landing_velocities.append(Vector2D(x=self.initial_velocity.x, y=final_y_velocity))

        return landing_velocities

    def calculate_landing_velocity(self):
        return [landing_velocity.get_magnitude() for landing_velocity in self._get_landing_velocities()]

    def calculate_landing_angle(self) -> List[float]:
        landing_angles = []

        for landing_velocity in self._get_landing_velocities():
            if landing_velocity.x == 0 or landing_velocity.y == 0:
                landing_angles.append(90)
            else:
                # tan(a) = Vy / Vx
                landing_angle_radians = np.arctan(landing_velocity.y / landing_velocity.x)
                landing_angles.append(np.rad2deg(landing_angle_radians))

        return landing_angles



