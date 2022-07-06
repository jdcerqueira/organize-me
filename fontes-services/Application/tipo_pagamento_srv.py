from requests import request
from tipo_pagamento_dao import TipoFormaPagamentoDAO
from flask_restful import Resource
from flask import request

class TipoFormaPagamento(Resource):
    def get(self, identificador=""):
        if identificador == "":
            retorno = TipoFormaPagamentoDAO().listaTipoFormaPagamento()
            return retorno["return"], retorno["http_state"]
        else:
            retorno = TipoFormaPagamentoDAO().listaTipoFormaPagamentoEspecifica(identificador)
            return retorno["return"], retorno["http_state"]

    def post(self):
        tipoFormaPagamento = request.get_json(force=True)
        nome = str(tipoFormaPagamento["nome"])
        aceitaComplemento = int(tipoFormaPagamento["aceitaComplemento"])
        inserido = TipoFormaPagamentoDAO().insereTipoFormaPagamento(nome, aceitaComplemento)
        return inserido["return"], inserido["http_state"]

    def delete(self,identificador):
        apagado = TipoFormaPagamentoDAO().apagaTipoFormaPagamento(identificador)
        return apagado["return"], apagado["http_state"]
