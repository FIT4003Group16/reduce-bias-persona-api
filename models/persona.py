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
    gender: Gender = types.enum(Gender).writeonce
    goals: list[str] = types.listof(str).nonnull.required
