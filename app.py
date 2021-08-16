from __future__ import annotations
from flask import Flask, Response, request
from jsonclasses_pymongo import Connection
from jsonclasses_flask import jsonclasses_integrate, data, empty, encode_jwt_token
from models.persona import Persona

app = Flask(__name__)

@app.get('/personas')
async def personas() -> Response:
    return data(await Persona.find())


@app.get('/personas/<id>')
async def persona(id: str) -> Response:
    return data(await Persona.id(id))


@app.post('/personas')
async def create_persona() -> Response:
    return data(Persona(**request.json).save())


@app.patch('/personas/<id>')
async def update_persona(id: str) -> Response:
    return data((await Persona.id(id)).set(**request.json).save())


@app.delete('/personas/<id>')
async def delete_persona(id: str) -> Response:
    return empty((await Persona.id(id)).delete())