from ZvuvonCalculator.Src.zvuvon_calculator import ZvuvonCalculator
from .models import ZvuvonResponse


def calculate_zvuvon_response(initial_angle: float, initial_height: float, initial_velocity: float) -> ZvuvonResponse:
    """
    Assembles a Zvuvon response out of the initial parameters
    :return: object representing the response
    """

    try:

        zvuvon = ZvuvonCalculator(initial_angle=initial_angle,
                                  initial_height=initial_height,
                                  initial_velocity=initial_velocity)

        # Prepare the results object
        results = ZvuvonResponse(landing_position=zvuvon.calculate_landing_position(),
                                 landing_angle=zvuvon.calculate_landing_angle(),
                                 landing_velocity=zvuvon.calculate_landing_velocity())

    except ValueError:
        raise ValueError("Request fields must be numbers!")

    except Exception as ex:
        raise ex
    
    return results
