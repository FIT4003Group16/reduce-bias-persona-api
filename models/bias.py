from __future__ import annotations
from typing import Optional,TYPE_CHECKING
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject
if TYPE_CHECKING:
    from models.persona import Persona

@pymongo
@jsonclass
class Bias(BaseObject):
    name: str = types.str.required
    description: str = types.str
    personas: list[Persona] = types.nonnull.listof('Persona').linkedby('bias')
