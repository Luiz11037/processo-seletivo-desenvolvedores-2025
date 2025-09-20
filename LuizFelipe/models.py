from app import db

#Criando table Produto
class Produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)

#Criando table Carrinho
class Carrinho(db.Model):
    __tablename__ = "carrinho"

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, default=1, nullable=False)

    produto = db.relationship('Produto')

    def __repr__(self):
        return f"<Carrinho {self.produto.nome} x {self.quantidade}>"