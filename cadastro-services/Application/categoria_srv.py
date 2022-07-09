from categoria_dao import CategoriaDAO
from flask_restful import Resource, request

class Categoria(Resource):
    def get(self):
        retorno = CategoriaDAO().lista()
        return retorno["return"], retorno["http_state"]

    def post(self, nome):
        inserido = CategoriaDAO().insere(nome)
        return inserido["return"], inserido["http_state"]

    def delete(self, categoria):
        apagado = CategoriaDAO().apaga(categoria)
        return apagado["return"], apagado["http_state"]