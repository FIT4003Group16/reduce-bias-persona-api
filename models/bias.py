from __future__ import annotations
from typing import Optional
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject


@pymongo
@jsonclass
class Bias(BaseObject):
    name: str = types.str.required
    description: str = types.str
