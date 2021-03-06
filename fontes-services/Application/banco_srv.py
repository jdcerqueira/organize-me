from banco_dao import BancoDAO
from flask_restful import Resource, request
from flask import jsonify
from config.properties import Bancos as ListaBancosGerais


class Bancos(Resource):
    def get(self, numero=""):
        if numero == "":
            retorno = BancoDAO().listaBancos()
        else:
            retorno = BancoDAO().listaBanco(numero)
    
        return retorno["return"], retorno["http_state"]

    def post(self):
        banco = request.get_json(force=True)
        codigo = None if "banco" not in banco else banco["banco"]
        nome = banco["nome"]
        inserido = BancoDAO().insereBanco(codigo, nome)
        return inserido["return"], inserido["http_state"]

    def delete(self, codigo):
        apagado = BancoDAO().apagaBanco(codigo)
        return apagado["return"], apagado["http_state"]
        

class BancosGerais(Resource):
    def get(self, codigo = ""):
        retorno = []
        if codigo == "":
            return ListaBancosGerais().listaBancos
        else:
            for item in ListaBancosGerais().listaBancos:
                if (item["banco"] == codigo) or (codigo.lower() in item["nome"].lower()):
                    retorno.append(item)

        if not len(retorno):
            return [], 204

        return retorno
        