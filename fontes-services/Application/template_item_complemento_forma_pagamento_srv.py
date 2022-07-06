from requests import request
from template_item_complemento_forma_pagamento_dao import TemplateItemComplementoFormaPagamentoDAO
from flask_restful import Resource
from flask import request

class TemplateItemComplementoFormaPagamento(Resource):
    def get(self, template, chave=""):
        if chave == "":
            retorno = TemplateItemComplementoFormaPagamentoDAO().lista(template)
            return retorno["return"], retorno["http_state"]
        else:
            retorno = TemplateItemComplementoFormaPagamentoDAO().listaEspecifica(template, chave)
            return retorno["return"], retorno["http_state"]

    def post(self):
        templateItemComplementoFormaPagamento = request.get_json(force=True)
        template = str(templateItemComplementoFormaPagamento["template"])
        chave = str(templateItemComplementoFormaPagamento["chave"])
        inserido = TemplateItemComplementoFormaPagamentoDAO().insere(template, chave)
        return inserido["return"], inserido["http_state"]

    def delete(self,template, chave):
        print("Delete: ", template, chave)
        apagado = TemplateItemComplementoFormaPagamentoDAO().apaga(template, chave)
        return apagado["return"], apagado["http_state"]
