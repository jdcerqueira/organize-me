from flask import Flask
from flask_restful import Api
from genero_srv import Generos
from responsavel_srv import Responsaveis
from categoria_srv import Categoria
from endereco_srv import Endereco
from estabelecimento_srv import Estabelecimento


app = Flask(__name__)
api = Api(app)

api.add_resource(Generos, "/cadastro/generos/lista", endpoint="lista_genero")
api.add_resource(Generos, "/cadastro/generos/insere/<string:nome>", endpoint="insere_genero")
api.add_resource(Generos, "/cadastro/generos/apaga/<string:genero>", endpoint="apaga_genero")

api.add_resource(Responsaveis, "/cadastro/responsaveis/lista", endpoint="lista_responsavel")
api.add_resource(Responsaveis, "/cadastro/responsaveis/insere", endpoint="insere_responsavel")
api.add_resource(Responsaveis, "/cadastro/responsaveis/apaga/<string:responsavel>", endpoint="apaga_responsavel")

api.add_resource(Categoria, "/cadastro/categorias/lista", endpoint="lista_categoria")
api.add_resource(Categoria, "/cadastro/categorias/insere/<string:nome>", endpoint="insere_categoria")
api.add_resource(Categoria, "/cadastro/categorias/apaga/<string:categoria>", endpoint="apaga_categoria")

api.add_resource(Endereco, "/cadastro/enderecos/lista", endpoint="lista_endereco")
api.add_resource(Endereco, "/cadastro/enderecos/vincula/<string:cep>", endpoint="insere_endereco")

api.add_resource(Estabelecimento, "/cadastro/estabelecimentos/lista", endpoint="lista_estabelecimento")
api.add_resource(Estabelecimento, "/cadastro/estabelecimentos/insere", endpoint="insere_estabelecimento")
api.add_resource(Estabelecimento, "/cadastro/estabelecimentos/apaga/<string:estabelecimento>", endpoint="apaga_estabelecimento")
api.add_resource(Estabelecimento, "/cadastro/estabelecimentos/lista/<string:categoria>", endpoint="lista_estabelecimento_categoria")
api.add_resource(Estabelecimento, "/cadastro/estabelecimentos/endereco/insere/<string:estabelecimento>", endpoint="insere_endereco_estabelecimento")

if __name__ == "__main__":
    app.run(debug=True, port=8081)