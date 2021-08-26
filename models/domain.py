from enum import Enum
from jsonclasses import jsonenum


@jsonenum
class Domain(Enum):
    ESHOP = 1
    EEDU = 2
