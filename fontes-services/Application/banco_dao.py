import logging
import pyodbc
from config.properties import Properties

class BancoDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB01").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def listaBancos(self):
        retorno = []

        try:
            self.cursor.execute("SELECT codigo, nome FROM app.vBancos ORDER BY nome")
            row = self.cursor.fetchone()
            while row:
                retorno.append({"banco":row[0], "nome":row[1]})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":retorno, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def listaBanco(self, numero):
        retorno = []

        try:
            self.cursor.execute("SELECT codigo, nome FROM app.vBancos WHERE (ISNUMERIC('"+ str(numero) +"')=1 AND codigo = '"+ str(numero) +"') OR LOWER(nome) LIKE '%"+ str(numero).lower() +"%'")
            row = self.cursor.fetchone()
            while row:
                retorno.append({"banco":row[0], "nome":row[1]})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state":200}

            return {"return":retorno, "http_state":204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def insereBanco(self, codigo, nome):
        retorno = {}
        try:
            self.cursor.execute("{call app.insereBanco("+ ("null" if codigo == None else codigo) +",'"+ nome +"')}")
            row = self.cursor.fetchone()
            retorno = {"banco":row[0], "nome": nome, "retorno":"Banco vinculado com sucesso."}
            self.connection.commit()
            return {"return":retorno, "http_state":201}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def apagaBanco(self, codigo):
        retorno = {}
        try:
            self.cursor.execute("{call app.apagaBanco("+ codigo +")}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"banco":row[0], "nome": row[1], "retorno":"Banco excluído com sucesso."}
                self.connection.commit()
            else:
                return {"return":retorno, "http_state":204}

            return {"return":retorno, "http_state":200}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}