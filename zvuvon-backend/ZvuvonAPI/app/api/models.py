import dataclasses
from typing import List


@dataclasses.dataclass
class ZvuvonResponse:
    landing_position: float
    landing_velocity: float
    landing_angle: float
