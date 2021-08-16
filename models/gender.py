from enum import Enum
from jsonclasses import jsonenum


@jsonenum
class Gender(Enum):
    MALE = 1
    FEMALE = 2
