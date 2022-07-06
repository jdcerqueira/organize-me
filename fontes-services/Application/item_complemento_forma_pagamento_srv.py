from requests import request
from item_complemento_forma_pagamento_dao import ItemComplementoFormaPagamentoDAO
from flask_restful import Resource
from flask import request

class ItemComplementoFormaPagamento(Resource):
    def get(self, chave=""):
        if chave == "":
            retorno = ItemComplementoFormaPagamentoDAO().lista()
            return retorno["return"], retorno["http_state"]
        else:
            retorno = ItemComplementoFormaPagamentoDAO().listaEspecifica(chave)
            return retorno["return"], retorno["http_state"]

    def post(self):
        itemComplementoFormaPagamento = request.get_json(force=True)
        chave = str(itemComplementoFormaPagamento["chave"])
        tipagem = str(itemComplementoFormaPagamento["tipagem"])
        infoConversao = str(itemComplementoFormaPagamento["info_conversao"])

        inserido = ItemComplementoFormaPagamentoDAO().insere(chave, tipagem, infoConversao)
        return inserido["return"], inserido["http_state"]

    def delete(self,chave):
        apagado = ItemComplementoFormaPagamentoDAO().apaga(chave)
        return apagado["return"], apagado["http_state"]
