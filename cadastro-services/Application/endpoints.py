from flask import Flask
from flask_restful import Api
from genero_srv import Generos


app = Flask(__name__)
api = Api(app)

api.add_resource(Generos, "/cadastro/generos/lista", endpoint="lista_genero")
api.add_resource(Generos, "/cadastro/generos/insere/<string:nome>", endpoint="insere_genero")
api.add_resource(Generos, "/cadastro/generos/apaga/<string:genero>", endpoint="apaga_genero")

if __name__ == "__main__":
    app.run(debug=True, port=8081)