import logging
import pyodbc
from config.properties import Properties

class GeneroDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB02").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def lista(self):
        retorno = []

        try:
            self.cursor.execute("SELECT identificador, nome FROM app.vGeneros ORDER BY nome")
            row = self.cursor.fetchone()
            while row:
                retorno.append({"genero":row[0], "nome":row[1]})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":retorno, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def insere(self, nome):
        retorno = {}
        try:
            self.cursor.execute("{call app.insereGenero('"+ nome +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"genero":row[0], "nome": row[1], "retorno":"Gênero criado com sucesso."}
                self.connection.commit()
            return {"return":retorno, "http_state":201}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def apaga(self, genero):
        retorno = {}
        try:
            self.cursor.execute("{call app.apagaGenero('"+ genero +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"genero":row[0], "nome": row[1], "retorno":"Gênero excluído com sucesso."}
                self.connection.commit()
            else:
                return {"return":retorno, "http_state":204}

            return {"return":retorno, "http_state":200}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}