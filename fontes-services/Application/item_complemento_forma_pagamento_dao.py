import logging
import pyodbc
from config.properties import Properties

class ItemComplementoFormaPagamentoDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB01").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def lista(self):
        retorno = []

        try:
            self.cursor.execute("SELECT chave, RTRIM(tipagem), infoConversao FROM app.vItemComplementoFormaPagamento ORDER BY chave")
            row = self.cursor.fetchone()
            while row:
                retorno.append({"chave":row[0], "tipagem":row[1], "info_conversao":row[2]})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}


    def listaEspecifica(self, chave):
        retorno = {}

        try:
            self.cursor.execute("SELECT chave, RTRIM(tipagem), infoConversao FROM app.vItemComplementoFormaPagamento WHERE chave = '"+ chave +"'")
            row = self.cursor.fetchone()
            if row:
                retorno = {"chave":row[0], "tipagem":row[1], "info_conversao":row[2]}

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}


    def insere(self, chave, tipagem, infoConversao):
        retorno = {}

        try:
            self.cursor.execute("{call app.insereItemComplementoFormaPagamento('"+ chave +"','"+ tipagem +"','"+ infoConversao +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"chave":row[0], "tipagem":row[1], "info_conversao":row[2], "mensagem":"Item de tipo de forma de pagamento criado com sucesso."}
                self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def apaga(self, chave):
        retorno = {}

        try:
            self.cursor.execute("{call app.apagaItemComplementoFormaPagamento('"+ chave +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"chave":row[0], "tipagem":row[1], "info_conversao":row[2], "mensagem":"Item de tipo de forma de pagamento excluído com sucesso."}
                self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}

    
    