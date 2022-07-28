import logging
import pyodbc
import requests
from config.properties import Properties
import json

class EstabelecimentoDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB02").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def lista(self):
        retorno = []

        try:
            self.cursor.execute("SELECT estabelecimento, nome, categoria, nome_categoria FROM app.vEstabelecimentos ORDER BY nome")
            row = self.cursor.fetchone()
            while row:
                retorno.append({"estabelecimento":row[0], "nome":row[1], "categoria":{"id":row[2], "nome":row[3]}})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":retorno, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def listaByCategoria(self,categoria):
        retorno = []

        try:
            self.cursor.execute("SELECT estabelecimento, nome FROM app.fEstabelecimentos('"+ categoria +"') ORDER BY nome")
            row = self.cursor.fetchone()
            while row:
                retorno.append({"estabelecimento":row[0], "nome":row[1]})
                row = self.cursor.fetchone()

            if len(retorno):
                return {"return":retorno, "http_state": 200}
            
            return {"return":retorno, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def insere(self, nome, categoria):
        retorno = {}
        try:
            self.cursor.execute("{call app.insereEstabelecimento('"+ nome +"','"+ categoria +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"estabelecimento":row[0], "nome": row[1], "retorno":"Estabelecimento criado com sucesso."}
                self.connection.commit()
            return {"return":retorno, "http_state":201}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def apaga(self, estabelecimento):
        retorno = {}
        try:
            self.cursor.execute("{call app.apagaEstabelecimento('"+ estabelecimento +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"estabelecimento":row[0], "nome": row[1], "retorno":"Estabelecimento excluído com sucesso."}
                self.connection.commit()
            else:
                return {"return":retorno, "http_state":204}

            return {"return":retorno, "http_state":200}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def insereEndereco(self, estabelecimento, cep, numero, complemento, ponto_referencia):
        cria_cep = requests.post(f"http://localhost:8081/cadastro/enderecos/vincula/{cep}")

        retorno = {}
        try:
            self.cursor.execute("{call app.insereEnderecoEstabelecimento('"+ cep +"','"+ estabelecimento +"','"+ str(numero) +"','"+ complemento +"','"+ ponto_referencia +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {
                    "id":row[0], 
                    "cep": row[1], 
                    "logradouro":cria_cep.json()[0]["logradouro"],
                    "numero":row[2], 
                    "complemento":row[3], 
                    "bairro":cria_cep.json()[0]["bairro"],
                    "cidade":cria_cep.json()[0]["cidade"],
                    "estado":cria_cep.json()[0]["estado"],
                    "uf":cria_cep.json()[0]["uf"],
                    "pais":cria_cep.json()[0]["pais"],
                    "retorno":"Endereço vinculado ao estabelecimento com sucesso."}
                self.connection.commit()
            return {"return":retorno, "http_state":201}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}
    

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}