import logging
import pyodbc
from config.properties import Properties

class TipoFormaPagamentoDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB01").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def listaTipoFormaPagamento(self):
        retorno = []

        try:
            self.cursor.execute("SELECT identificador, nome, aceitaComplemento FROM app.vTipoFormaPagamento ORDER BY nome")
            row = self.cursor.fetchone()
            while row:
                retorno.append({"identificador":row[0], "tipo":row[1], "aceitaComplemento":int(row[2])})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}


    def listaTipoFormaPagamentoEspecifica(self, identificador):
        retorno = {}

        try:
            self.cursor.execute("SELECT identificador, nome, aceitaComplemento FROM app.vTipoFormaPagamento WHERE identificador = '"+ identificador +"'")
            row = self.cursor.fetchone()
            if row:
                retorno = {"identificador":row[0], "tipo":row[1], "aceitaComplemento":int(row[2])}

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}


    def insereTipoFormaPagamento(self, nome, aceitaComplemento):
        retorno = {}

        try:
            self.cursor.execute("{call app.insereTipoFormaPagamento('"+ nome +"',"+ str(aceitaComplemento) +")}")
            row = self.cursor.fetchone()
            retorno = {"identificador":row[0], "tipo":nome, "aceitaComplemento":int(aceitaComplemento), "mensagem":"Tipo de forma de pagamento criado com sucesso."}
            self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def apagaTipoFormaPagamento(self, identificador):
        retorno = {}

        try:
            self.cursor.execute("{call app.apagaTipoFormaPagamento('"+ identificador +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"identificador":row[0], "tipo":row[1], "aceitaComplemento":int(row[2]), "mensagem":"Tipo de forma de pagamento excluído com sucesso."}
                self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}

    
    