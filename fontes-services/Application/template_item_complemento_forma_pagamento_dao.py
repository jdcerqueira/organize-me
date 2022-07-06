import logging
import pyodbc
from config.properties import Properties

class TemplateItemComplementoFormaPagamentoDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB01").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def lista(self,template):
        retorno = []

        try:
            self.cursor.execute("SELECT chave FROM app.fTemplateItemComplementoFormaPagamento('"+ template +"') ORDER BY chave")
            row = self.cursor.fetchone()
            while row:
                retorno.append(row[0])
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":{"chaves":retorno}, "http_state": 200}
            
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


    def insere(self, template, chave):
        retorno = {}

        try:
            self.cursor.execute("{call app.insereTemplateItemComplementoFormaPagamento('"+ chave +"','"+ template +"')}")
            retorno = {"mensagem":"Chave associada ao template com sucesso."}
            self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def apaga(self, template, chave):
        retorno = {}

        try:
            self.cursor.execute("{call app.apagaTemplateItemComplementoFormaPagamento('"+ chave +"','"+ template +"')}")
            retorno = {"mensagem":"Chave desassociada ao template com sucesso."}
            self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}

    
    