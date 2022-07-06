from requests import request
from template_complemento_forma_pagamento_dao import TemplateComplementoFormaPagamentoDAO
from flask_restful import Resource
from flask import request

class TemplateComplementoFormaPagamento(Resource):
    def get(self, template=""):
        if template == "":
            retorno = TemplateComplementoFormaPagamentoDAO().lista()
            return retorno["return"], retorno["http_state"]
        else:
            retorno = TemplateComplementoFormaPagamentoDAO().listaEspecifica(template)
            return retorno["return"], retorno["http_state"]

    def post(self):
        templateComplementoFormaPagamento = request.get_json(force=True)
        descricao = str(templateComplementoFormaPagamento["descricao"])
        inserido = TemplateComplementoFormaPagamentoDAO().insere(descricao)
        return inserido["return"], inserido["http_state"]

    def delete(self,template):
        apagado = TemplateComplementoFormaPagamentoDAO().apaga(template)
        return apagado["return"], apagado["http_state"]
