import logging
import pyodbc
from config.properties import Properties

class TemplateComplementoFormaPagamentoDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB01").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def lista(self):
        retorno = []

        try:
            self.cursor.execute("SELECT identificador, descricao FROM app.vTemplateComplementoFormaPagamento ORDER BY descricao")
            row = self.cursor.fetchone()
            while row:
                retorno.append({"template":row[0], "descricao":row[1]})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}


    def listaEspecifica(self, template):
        retorno = {}

        try:
            self.cursor.execute("SELECT identificador, descricao FROM app.vTemplateComplementoFormaPagamento WHERE identificador = '" + template +"'")
            row = self.cursor.fetchone()
            if row:
                retorno = {"template":row[0], "descricao":row[1]}

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}


    def insere(self, descricao):
        retorno = {}

        try:
            self.cursor.execute("{call app.insereTemplateComplementoFormaPagamento('"+ descricao +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"template":row[0], "descricao":row[1], "mensagem":"Template de complemento de forma de pagamento criado com sucesso."}
                self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def apaga(self, template):
        retorno = {}

        try:
            self.cursor.execute("{call app.apagaTemplateComplementoFormaPagamento('"+ template +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"template":row[0], "descricao":row[1], "mensagem":"Template de complemento de forma de pagamento excluido com sucesso."}
                self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}

    
    