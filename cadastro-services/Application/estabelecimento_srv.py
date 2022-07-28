from estabelecimento_dao import EstabelecimentoDAO
from flask_restful import Resource, request

class Estabelecimento(Resource):
    def get(self,categoria=None):
        if categoria == None:
            retorno = EstabelecimentoDAO().lista()
            return retorno["return"], retorno["http_state"]    

        retorno = EstabelecimentoDAO().listaByCategoria(categoria)
        return retorno["return"], retorno["http_state"]

    def post(self, estabelecimento=None):
        if estabelecimento == None:
            estabelecimento = request.get_json(force=True)
            inserido = EstabelecimentoDAO().insere(nome=estabelecimento["nome"], categoria=estabelecimento["categoria"])
            return inserido["return"], inserido["http_state"]

        endereco = request.get_json(force=True)
        inserido = EstabelecimentoDAO().insereEndereco(estabelecimento,endereco["cep"],endereco["numero"],endereco["complemento"], endereco["ponto_referencia"])
        return inserido["return"], inserido["http_state"]

    def delete(self, estabelecimento):
        apagado = EstabelecimentoDAO().apaga(estabelecimento)
        return apagado["return"], apagado["http_state"]