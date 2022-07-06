from requests import request
from complemento_forma_pagamento_dao import ComplementoFormaPagamentoDAO
from flask_restful import Resource
from flask import request

class ComplementoFormaPagamento(Resource):
    def get(self,formaPagamento):
        retorno = ComplementoFormaPagamentoDAO().lista(formaPagamento)
        return retorno["return"], retorno["http_state"]

    def post(self):
        not_keys = ["forma_pagamento"]
        retorno = []
        erro = {}

        complementoFormaPagamento = request.get_json(force=True)
        formaPagamento = complementoFormaPagamento["forma_pagamento"]
        for key in complementoFormaPagamento:
            if key not in not_keys:
                (inserido, executado) = ComplementoFormaPagamentoDAO().insere(formaPagamento = formaPagamento, chave=key, valor=complementoFormaPagamento[key])
                if not bool(executado):
                    erro = {"return":inserido["return"], "http_state":inserido["http_state"]}
                    break
                
                retorno.append({"chave":key, "valor": complementoFormaPagamento[key], "return":inserido["return"], "http_state":inserido["http_state"]})

        if len(erro):
            for key in retorno:
                self.delete(formaPagamento,key["chave"])

            return erro["return"], erro["http_state"]

        return [doc["return"] for doc in retorno],201

    def delete(self,formaPagamento,chave):
        apagado = ComplementoFormaPagamentoDAO().apaga(formaPagamento,chave)
        return apagado["return"], apagado["http_state"]
