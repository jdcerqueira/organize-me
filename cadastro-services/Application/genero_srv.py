from genero_dao import GeneroDAO
from flask_restful import Resource, request

class Generos(Resource):
    def get(self):
        retorno = GeneroDAO().lista()
        return retorno["return"], retorno["http_state"]

    def post(self, nome):
        inserido = GeneroDAO().insere(nome)
        return inserido["return"], inserido["http_state"]

    def delete(self, genero):
        apagado = GeneroDAO().apaga(genero)
        return apagado["return"], apagado["http_state"]