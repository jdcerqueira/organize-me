from responsavel_dao import ResponsavelDAO
from flask_restful import Resource, request

class Responsaveis(Resource):
    def get(self):
        retorno = ResponsavelDAO().lista()
        return retorno["return"], retorno["http_state"]

    def post(self):
        responsavel = request.get_json(force=True)
        inserido = ResponsavelDAO().insere(
            genero=responsavel["genero"],
            nome=responsavel["nome"],
            data_nascimento=responsavel["data_nascimento"]
            )
        return inserido["return"], inserido["http_state"]

    def delete(self, responsavel):
        apagado = ResponsavelDAO().apaga(responsavel)
        return apagado["return"], apagado["http_state"]