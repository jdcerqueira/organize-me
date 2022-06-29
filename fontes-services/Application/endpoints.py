from flask import Flask
from flask_restful import Api, Resource
from banco_srv import Bancos, BancosGerais
#from tipo_pagamento_srv import TipoPagamento
#from responsaveis_srv import Responsaveis
#from forma_pagamento_srv import FormaPagamento

app = Flask(__name__)
api = Api(app)

#api.add_resource(Responsaveis, "/responsavel/lista", endpoint="responsaveis_busca")
#api.add_resource(Responsaveis, "/responsavel/<string:identificador>", endpoint="responsavel_busca")
#api.add_resource(Responsaveis, "/responsavel/insere", endpoint="responsavel_insere")
#api.add_resource(Bancos, "/banco/lista", endpoint="bancos_busca")
#api.add_resource(Bancos, "/banco/<string:numero>", endpoint="banco_busca")
#api.add_resource(Bancos, "/banco/insere", endpoint="banco_insere")
api.add_resource(BancosGerais, "/fontes/bancos/geral", endpoint="lista_geral_bancos")
api.add_resource(BancosGerais, "/fontes/bancos/geral/<string:codigo>", endpoint="lista_geral_bancos_espec")
#api.add_resource(TipoPagamento, "/tipopagamento", endpoint="tipopagamento_busca")
#api.add_resource(FormaPagamento, "/formapagamento/lista", endpoint="formapagamentos_busca")
#api.add_resource(FormaPagamento, "/formapagamento/<string:identificador>", endpoint="formapagamentos_busca_espec")

if __name__ == "__main__":
    app.run(debug=True, port=8080)