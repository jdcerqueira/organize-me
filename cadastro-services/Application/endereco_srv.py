from endereco_dao import EnderecoDAO
from flask_restful import Resource, request

class Endereco(Resource):
    def get(self):
        retorno = EnderecoDAO().lista()
        return retorno["return"], retorno["http_state"]

    def post(self, cep):
        inserido = EnderecoDAO(cep).listaEspec(cep)
        return inserido["return"], inserido["http_state"]

    #def delete(self, responsavel):
    #    apagado = ResponsavelDAO().apaga(responsavel)
    #    return apagado["return"], apagado["http_state"]