from .projectile_motion import ProjectileMotion
from typing import List


def _validate_input(*args):
    """
    Checks if there are any empty arguments
    or non-float arguments
    """
    for arg in args:
        if arg is None:
            raise Exception("Input cannot be empty!")

        try:
            float(arg)

        except ValueError:
            raise ValueError("Input must be a number!")


class ZvuvonCalculator:
    def __init__(self, initial_angle: float, initial_height: float, initial_velocity: float):

        # Make sure the input received is valid
        try:
            _validate_input(initial_angle, initial_height, initial_velocity)

        except ValueError as ex:
            raise ex

        except OverflowError:
            raise Exception("One of the inputs is too large!")

        except Exception as ex:
            raise ex

        # Safe to parse to float here
        self.projectile_motion = ProjectileMotion(initial_angle=float(initial_angle),
                                                  initial_height=float(initial_height),
                                                  initial_velocity=float(initial_velocity))

    def calculate_landing_position(self) -> float:
        """
        Calculates the landing position of the object
        :return: returns the landing position
        """

        # Object can only hit the ground once, so two solutions are not possible
        # unless the object is launched from the ground.
        return max(self.projectile_motion.calculate_positions())

    def calculate_landing_angle(self) -> float:
        """
        Calculates the landing angle of the object
        :return: returns the landing angle
        """

        return min(self.projectile_motion.calculate_angles())

    def calculate_landing_velocity(self) -> float:
        """
        Calculates the landing velocity of the object
        :return: returns the landing velocity
        """

        return self.projectile_motion.get_velocities()[0].get_magnitude()
