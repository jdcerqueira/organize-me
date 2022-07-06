import logging
import pyodbc
from config.properties import Properties
from complemento_forma_pagamento_srv import ComplementoFormaPagamento

class FormaPagamentoDAO():
    def __init__(self):
        cfg = Properties("ORGANIZEDB01").properties
        self.connection = pyodbc.connect(cfg["datasource"])
        self.cursor = self.connection.cursor()
        
    def lista(self):
        retorno = []

        try:
            self.cursor.execute("SELECT identificador,nome,codBanco,nomeBanco,idTipoPagamento,nomeTipoPagamento,aceitaComplemento FROM app.vFormaPagamento ORDER BY nome")
            row = self.cursor.fetchone()
            while row:
                formaPagamento = {
                        "forma_pagamento":row[0],
                        "nome":row[1],
                        "banco":{"codigo":row[2],"nome":row[3]},
                        "tipo_pagamento":{"codigo":row[4], "nome":row[5], "aceita_complemento":int(row[6])},
                        "complemento": ComplementoFormaPagamento().get(formaPagamento = row[0])[0] if ComplementoFormaPagamento().get(formaPagamento = row[0])[0] != {} else []
                    }
                retorno.append(formaPagamento)
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


    def insere(self, nome, banco, tipoPagamento):
        retorno = {}

        try:
            self.cursor.execute("{call app.insereFormaPagamento("+ str(banco) +",'"+ tipoPagamento +"', '"+ nome +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"forma_pagamento":row[0], "nome":row[1], "mensagem":"Forma de pagamento criada com sucesso."}
                self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def apaga(self, formaPagamento):
        retorno = {}

        try:
            self.cursor.execute("{call app.apagaFormaPagamento('"+ formaPagamento +"')}")
            row = self.cursor.fetchone()
            if row:
                retorno = {"forma_pagamento":row[0], "nome":row[1], "mensagem":"Forma de pagamento excluída com sucesso."}
                self.connection.commit()

            if len(retorno):
                return {"return":retorno, "http_state": 201}
            
            return {"return":{}, "http_state": 204}
        except pyodbc.Error as ex:
            return {"return":self.exceptions(ex), "http_state":500}

    def exceptions(self, ex):
        logging.error(ex.args[1])
        return {"erro":"Ocorreu um erro na execução do serviço. Verifique detalhes no log da aplicação."}

    
    