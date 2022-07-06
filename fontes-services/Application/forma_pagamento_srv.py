from requests import request
from forma_pagamento_dao import FormaPagamentoDAO
from flask_restful import Resource
from flask import request

class FormaPagamento(Resource):
    def get(self):
        retorno = FormaPagamentoDAO().lista()
        return retorno["return"], retorno["http_state"]
        

    def post(self):
        formaPagamento = request.get_json(force=True)
        banco = formaPagamento["banco"]
        tipoPagamento = formaPagamento["tipo_pagamento"]
        nome = formaPagamento["nome"]
        inserido = FormaPagamentoDAO().insere(nome, banco, tipoPagamento)
        return inserido["return"], inserido["http_state"]

    def delete(self,formaPagamento):
        apagado = FormaPagamentoDAO().apaga(formaPagamento)
        return apagado["return"], apagado["http_state"]
