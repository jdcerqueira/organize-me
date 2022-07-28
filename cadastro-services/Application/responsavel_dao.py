import logging
import pyodbc
from config.properties import Properties

class ResponsavelDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB02").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def lista(self):
        retorno = []

        try:
            self.cursor.execute("SELECT identificador, nome, data_nascimento, genero, nomeGenero FROM app.vResponsaveis ORDER BY nome")
            row = self.cursor.fetchone()
            while row:
                retorno.append({"responsavel":row[0], "nome":row[1], "data_nascimento":str(row[2]), "genero":{"id":row[3], "nome":row[4]}})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":retorno, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def insere(self, genero, nome , data_nascimento):
        print (genero, nome, data_nascimento)
        retorno = {}
        try:
            self.cursor.execute("{call app.insereResponsavel('"+ genero +"','"+ nome +"','"+ data_nascimento +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"responsavel":row[0], "nome": row[1], "data_nascimento":str(row[2]), "retorno":"Responsável criado com sucesso."}
                self.connection.commit()
            return {"return":retorno, "http_state":201}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def apaga(self, responsavel):
        retorno = {}
        try:
            self.cursor.execute("{call app.apagaResponsavel('"+ responsavel +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"responsavel":row[0], "nome": row[1], "data_nascimento":str(row[2]), "retorno":"Responsável excluído com sucesso."}
                self.connection.commit()
            else:
                return {"return":retorno, "http_state":204}

            return {"return":retorno, "http_state":200}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}