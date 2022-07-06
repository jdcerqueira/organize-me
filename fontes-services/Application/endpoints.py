from flask import Flask
from flask_restful import Api, Resource
from banco_srv import Bancos, BancosGerais
from tipo_pagamento_srv import TipoFormaPagamento
from item_complemento_forma_pagamento_srv import ItemComplementoFormaPagamento
from template_complemento_forma_pagamento_srv import TemplateComplementoFormaPagamento
from template_item_complemento_forma_pagamento_srv import TemplateItemComplementoFormaPagamento
from forma_pagamento_srv import FormaPagamento
from complemento_forma_pagamento_srv import ComplementoFormaPagamento
#from responsaveis_srv import Responsaveis


app = Flask(__name__)
api = Api(app)

#api.add_resource(Responsaveis, "/responsavel/lista", endpoint="responsaveis_busca")
#api.add_resource(Responsaveis, "/responsavel/<string:identificador>", endpoint="responsavel_busca")
#api.add_resource(Responsaveis, "/responsavel/insere", endpoint="responsavel_insere")

api.add_resource(Bancos, "/fontes/bancos/vinculados", endpoint="lista_vinculos_bancos")
api.add_resource(Bancos, "/fontes/bancos/vinculados/<string:numero>", endpoint="lista_vinculos_bancos_espec")
api.add_resource(Bancos, "/fontes/bancos/insere", endpoint="insere_bancos")
api.add_resource(Bancos, "/fontes/bancos/apaga/<string:codigo>", endpoint="apaga_bancos")

api.add_resource(BancosGerais, "/fontes/bancos/geral", endpoint="lista_geral_bancos")
api.add_resource(BancosGerais, "/fontes/bancos/geral/<string:codigo>", endpoint="lista_geral_bancos_espec")

api.add_resource(TipoFormaPagamento, "/fontes/tipoformapagamento/lista", endpoint="lista_tipoformapagamento")
api.add_resource(TipoFormaPagamento, "/fontes/tipoformapagamento/lista/<string:identificador>", endpoint="lista_tipoformapagamento_espec")
api.add_resource(TipoFormaPagamento, "/fontes/tipoformapagamento/insere", endpoint="insere_tipoformapagamento")
api.add_resource(TipoFormaPagamento, "/fontes/tipoformapagamento/apaga/<string:identificador>", endpoint="apaga_tipoformapagamento")

api.add_resource(ItemComplementoFormaPagamento, "/fontes/complementoformapagamento/item/lista", endpoint="lista_itemcomplementoformapagamento")
api.add_resource(ItemComplementoFormaPagamento, "/fontes/complementoformapagamento/item/lista/<string:chave>", endpoint="lista_itemcomplementoformapagamento_espec")
api.add_resource(ItemComplementoFormaPagamento, "/fontes/complementoformapagamento/item/insere", endpoint="insere_itemcomplementoformapagamento")
api.add_resource(ItemComplementoFormaPagamento, "/fontes/complementoformapagamento/item/apaga/<string:chave>", endpoint="apaga_itemcomplementoformapagamento")

api.add_resource(TemplateComplementoFormaPagamento, "/fontes/complementoformapagamento/template/lista", endpoint="lista_templatecomplementoformapagamento")
api.add_resource(TemplateComplementoFormaPagamento, "/fontes/complementoformapagamento/template/lista/<string:template>", endpoint="lista_templatecomplementoformapagamento_espec")
api.add_resource(TemplateComplementoFormaPagamento, "/fontes/complementoformapagamento/template/insere", endpoint="insere_templatecomplementoformapagamento")
api.add_resource(TemplateComplementoFormaPagamento, "/fontes/complementoformapagamento/template/apaga/<string:template>", endpoint="apaga_templatecomplementoformapagamento")

api.add_resource(TemplateItemComplementoFormaPagamento, "/fontes/complementoformapagamento/template/item/lista/<string:template>", endpoint="lista_templateitemcomplementoformapagamento")
api.add_resource(TemplateItemComplementoFormaPagamento, "/fontes/complementoformapagamento/template/item/lista/<string:template>/<string:chave>", endpoint="lista_templateitemcomplementoformapagamento_espec")
api.add_resource(TemplateItemComplementoFormaPagamento, "/fontes/complementoformapagamento/template/item/insere", endpoint="insere_templateitemcomplementoformapagamento")
api.add_resource(TemplateItemComplementoFormaPagamento, "/fontes/complementoformapagamento/template/item/apaga/<string:template>/<string:chave>", endpoint="apaga_templateitemcomplementoformapagamento")

api.add_resource(FormaPagamento, "/fontes/formapagamento/lista", endpoint="lista_formapagamento")
api.add_resource(FormaPagamento, "/fontes/formapagamento/insere", endpoint="insere_formapagamento")
api.add_resource(FormaPagamento, "/fontes/formapagamento/apaga/<string:formaPagamento>", endpoint="apaga_formapagamento")

api.add_resource(ComplementoFormaPagamento, "/fontes/formapagamento/complemento/lista/<string:formaPagamento>", endpoint="lista_complementoformapagamento")
api.add_resource(ComplementoFormaPagamento, "/fontes/formapagamento/complemento/insere", endpoint="insere_complementoformapagamento")
api.add_resource(ComplementoFormaPagamento, "/fontes/formapagamento/complemento/apaga/<string:formaPagamento>/<string:chave>", endpoint="apaga_complementoformapagamento")


#api.add_resource(FormaPagamento, "/formapagamento/lista", endpoint="formapagamentos_busca")
#api.add_resource(FormaPagamento, "/formapagamento/<string:identificador>", endpoint="formapagamentos_busca_espec")

if __name__ == "__main__":
    app.run(debug=True, port=8080)