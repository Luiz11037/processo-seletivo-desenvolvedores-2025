from app import db

class Produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)


class Carrinho(db.Model):
    __tablename__ = "carrinho"

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, default=1, nullable=False)

    # relacionamento com o produto
    produto = db.relationship('Produto')

    def __repr__(self):
        return f"<Carrinho {self.produto.nome} x {self.quantidade}>"

'''
{
			"descricao": "Bacana ",
			"id": 1,
			"marca": "Android",
			"nome": "Motorola",
			"preco": 1500
		},
		{
			"descricao": "i5 12450h, 16gb ram, tela tn ",
			"id": 2,
			"marca": "Acer",
			"nome": "Notebook Acer aspire 5",
			"preco": 2750
		},
		{
			"descricao": "Bluetooth 5.1",
			"id": 3,
			"marca": "QYC",
			"nome": "Fone Bluetooth",
			"preco": 150
}
'''