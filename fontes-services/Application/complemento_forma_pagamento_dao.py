import logging
import pyodbc
from config.properties import Properties

class ComplementoFormaPagamentoDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB01").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def lista(self, formaPagamento):
        retorno = []

        try:
            self.cursor.execute("SELECT chave, valor FROM app.fComplementoFormaPagamento('"+ formaPagamento +"')")
            row = self.cursor.fetchone()
            while row:
                retorno.append({row[0]:row[1]})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}


    def listaEspecifica(self, template, chave):
        retorno = {}

        try:
            self.cursor.execute("SELECT chave FROM app.fTemplateItemComplementoFormaPagamento('"+ template +"') where chave = '"+ chave +"'")
            row = self.cursor.fetchone()
            if row:
                retorno = {"chave":row[0]}

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}


    def insere(self, formaPagamento, chave, valor):
        retorno = {}

        try:
            self.cursor.execute("{call app.insereComplementoFormaPagamento('"+ formaPagamento +"','"+ chave +"', '"+ str(valor) +"')}")
            retorno = {"forma_pagamento":formaPagamento, "chave":chave, "valor":valor, "mensagem":"Complemento de forma de pagamento criado com sucesso."}
            self.connection.commit()

            if len(retorno):
                return ({"return":retorno, "http_state": 201}, True)
            
            return ({"return":retorno, "http_state": 204}, True)
        except pyodbc.Error as ex:
            return ({"return":self.exceptions(ex), "http_state":500}, False)

    def apaga(self, formaPagamento,chave):
        retorno = {}

        try:
            self.cursor.execute("{call app.apagaComplementoFormaPagamento('"+ formaPagamento +"','"+ chave +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"forma_pagamento":formaPagamento, "chave":chave, "valor": row[0], "mensagem":"Complemento de forma de pagamento excluído com sucesso."}
                self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}

    
    