from rest_framework.response import Response
from rest_framework import status


def error(msg: str) -> Response:
    """
    Returns an error response with status code of 400 Bad Request.
    :param msg: error message to be displayed as a response.
    :return: returns a response object containing the error message.
    """
    return Response({"ERROR": msg}, status=status.HTTP_400_BAD_REQUEST)
