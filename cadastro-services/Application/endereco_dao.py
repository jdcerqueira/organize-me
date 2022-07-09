import logging
import pyodbc
from config.properties import Properties
import requests

class EnderecoDAO():
    def __init__(self, cep):
        cfg = Properties("ORGANIZEDB02").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()

        self.cep = cep
        if self.validateStreetByCep() == None:
            cep_request = requests.get(f"http://viacep.com.br/ws/{self.cep}/json")
            if "erro" in cep_request.json():
                print("erro: " + cep_request.json()["erro"])
            else:
                self.nome = str(cep_request.json()["logradouro"]).upper()
                self.complemento = str(cep_request.json()["complemento"]).upper()
                self.bairro = str(cep_request.json()["bairro"]).upper()
                self.cidade = str(cep_request.json()["localidade"]).upper()
                self.uf = str(cep_request.json()["uf"]).upper()
                self.pais = "BRASIL"
                self.validateStreetByDistrict(self.validateDistrict(self.validateCity(self.validateState(self.validateCountry()))))

    def validateCountry(self):
        try:
            self.cursor.execute("SELECT identificador FROM [app].[vPaises] WHERE nome = '"+ self.pais +"'")
            row = self.cursor.fetchone()
            if row:
                return row[0]

            self.cursor.execute("{call [app].[inserePais]('"+ self.pais +"')}")
            row = self.cursor.fetchone()
            if row:
                self.connection.commit()
                return row[0]
        except pyodbc.Error as ex:
            print(self.exceptions(ex))
            return None

    def validateState(self, pais):
        try:
            self.cursor.execute("SELECT uf FROM [app].[fEstados]('"+ pais +"') WHERE uf = '"+ self.uf +"'")
            row = self.cursor.fetchone()
            if row:
                return row[0]

            uf_request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{self.uf}")
            self.cursor.execute("{call [app].[insereEstado]('"+ str(uf_request.json()["nome"]).upper() +"','"+ self.uf.upper() +"','"+ pais +"')}")
            row = self.cursor.fetchone()
            if row:
                self.connection.commit()
                return row[0]
        except pyodbc.Error as ex:
            print(self.exceptions(ex))
            return None

    def validateCity(self, uf):
        try:
            self.cursor.execute("SELECT identificador FROM [app].[fCidades]('"+ uf +"') WHERE nome = '"+ self.cidade +"'")
            row = self.cursor.fetchone()
            if row:
                return row[0]

            self.cursor.execute("{call [app].[insereCidade]('"+ self.cidade +"','"+ uf +"')}")
            row = self.cursor.fetchone()
            if row:
                self.connection.commit()
                return row[0]
        except pyodbc.Error as ex:
            print(self.exceptions(ex))
            return None

    def validateDistrict(self, cidade):
        try:
            self.cursor.execute("SELECT identificador FROM [app].[fBairros]('"+ cidade +"') WHERE nome = '"+ self.bairro +"'")
            row = self.cursor.fetchone()
            if row:
                return row[0]

            self.cursor.execute("{call [app].[insereBairro]('"+ self.bairro +"','"+ cidade +"')}")
            row = self.cursor.fetchone()
            if row:
                self.connection.commit()
                return row[0]
        except pyodbc.Error as ex:
            print(self.exceptions(ex))
            return None

    def validateStreetByDistrict(self, bairro):
        try:
            self.cursor.execute("SELECT cep FROM [app].[fLogradouros]('"+ bairro +"') WHERE cep = '"+ self.cep +"'")
            row = self.cursor.fetchone()
            if row:
                return row[0]

            self.cursor.execute("{call [app].[insereLogradouro]('"+ self.cep +"','"+ self.nome +"','"+ self.complemento +"', '"+ bairro +"')}")
            row = self.cursor.fetchone()
            if row:
                self.connection.commit()
                return row[0]
        except pyodbc.Error as ex:
            print(self.exceptions(ex))
            return None

    def validateStreetByCep(self):
        try:
            self.cursor.execute("SELECT cep FROM [app].[vLogradouros] WHERE cep = '"+ self.cep +"'")
            row = self.cursor.fetchone()
            if row:
                return row[0]
            return None
        except pyodbc.Error as ex:
            print(self.exceptions(ex))
            return None
        
    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}