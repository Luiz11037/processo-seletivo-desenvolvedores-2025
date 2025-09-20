from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Instanciando app.
app = Flask(__name__)

# Dados de configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USUARIO:SENHA@localhost/carrinho'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # sem warning

# Instanciando o SQLAlchemy
db = SQLAlchemy(app)

#importando as rotas(GET, POST, DELETE, PUT)
from routes_produto import *
from routes_carrinho import *

#Isso precisa estar no final.
if __name__ == "__main__":
    app.run(debug=True)