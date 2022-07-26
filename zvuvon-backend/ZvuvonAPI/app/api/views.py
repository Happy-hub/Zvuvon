import dataclasses
from typing import Optional, Tuple

from django.http import QueryDict, HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

import ZvuvonAPI.app.api.zvuvon_calculator_service as zvuvon_service
import ZvuvonAPI.app.api.utils as utils


def parse_initial_parameters(params_dict: QueryDict) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    """
    Parses the data received from the request and
    extracts the required parameters
    :param params_dict: a dictionary containing the url parameters
    :return: returns a tuple containing all the initial values
    """
    initial_angle, initial_height, initial_velocity = (
        params_dict.get("initial_angle"),
        params_dict.get("initial_height"),
        params_dict.get("initial_velocity")
    )

    return initial_angle, initial_height, initial_velocity


@api_view(['GET'])
def calculate_motion(request: HttpRequest, *args, **kwargs):
    """
    Calculates the landing position,
    landing angle and landing velocity of an object
    from the given initial parameters
    :return: returns a ZvuvonResponse containing the results
    """

    # Retrieve initial parameters from request's body
    (initial_angle,
     initial_height,
     initial_velocity) = parse_initial_parameters(params_dict=request.GET)

    try:
        response = zvuvon_service.calculate_zvuvon_response(initial_angle=initial_angle,
                                                            initial_height=initial_height,
                                                            initial_velocity=initial_velocity)

    except Exception as ex:
        return utils.error(str(ex))

    return Response({"results": dataclasses.asdict(response)})