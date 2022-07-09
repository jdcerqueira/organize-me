from flask import Flask
from flask_restful import Api
from genero_srv import Generos
from responsavel_srv import Responsaveis
from categoria_srv import Categoria


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

if __name__ == "__main__":
    app.run(debug=True, port=8081)