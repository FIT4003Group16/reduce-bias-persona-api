from __future__ import annotations
from flask import Flask, Response, request
from jsonclasses_pymongo import Connection
from jsonclasses_flask import jsonclasses_integrate, data, empty, encode_jwt_token
from models.persona import Persona
from models.gender import Gender
from models.bias import Bias
from utils.jsjson_encoder import JSJSONEncoder
from utils.data import data
from utils.empty import empty


app = Flask(__name__)

app.json_encoder = JSJSONEncoder

app.url_map.strict_slashes = False

jsonclasses_integrate(app, cors={
    'allow_headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
}, operator={
    'operator_cls': Bias,
    'encode_key': 'SECRET_VERY_SECRET'
})

@app.get('/personas')
async def personas() -> Response:
    return data(await Persona.find().include('bias'))


@app.get('/personas/<id>')
async def persona(id: str) -> Response:
    return data(await Persona.id(id).include('bias'))


@app.post('/personas')
async def create_persona() -> Response:
    return data(Persona(**request.json).save())


@app.patch('/personas/<id>')
async def update_persona(id: str) -> Response:
    return data((await Persona.id(id)).set(**request.json).save())


@app.delete('/personas/<id>')
async def delete_persona(id: str) -> Response:
    return empty((await Persona.id(id)).delete())

@app.get('/biases')
async def biases() -> Response:
    return data(await Bias.find())


@app.get('/biases/<id>')
async def bias(id: str) -> Response:
    return data(await Bias.id(id))


@app.post('/biases')
async def create_bias() -> Response:
    return data(Bias(**request.json).save())


@app.patch('/biases/<id>')
async def update_bias(id: str) -> Response:
    return data((await Bias.id(id)).set(**request.json).save())


@app.delete('/biases/<id>')
async def delete_bias(id: str) -> Response:
    return empty((await Bias.id(id)).delete())