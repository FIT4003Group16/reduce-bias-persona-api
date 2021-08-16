from __future__ import annotations
from typing import Optional
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject
from models.gender import Gender

@pymongo
@jsonclass
class Persona(BaseObject):
    name: str = types.str.required
    age: int = types.int.min(0).required
    gender: Optional[Gender] = types.enum(Gender).required
    goals: list[str] = types.listof(str).nonnull.required
    to_do_list: list[str] = types.listof(str).nonnull.required
