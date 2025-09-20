from flask import request
from app import app, db
from models import Carrinho, Produto
from routes_produto import *



#Mostrar Carrinho
@app.route("/carrinho", methods=["GET"])
def get_carrinho():
    items = Carrinho.query.all()
    resultado = []
    valor_total = 0  # vai somar todos os produtos

    for i in items:
        subtotal = i.produto.preco * i.quantidade  # preço * quantidade
        valor_total += subtotal
        resultado.append({
            "id": i.id,
            "produto": i.produto.nome,
            "marca": i.produto.marca,
            "preco_unitario": i.produto.preco,
            "quantidade": i.quantidade,
            "subtotal": subtotal
        })

    return {"carrinho": resultado, "valor_total": valor_total}



#Colocar porduto dentro de carrinho
@app.route("/carrinho/addProduto/<int:id>", methods=["POST"])
def adicionar_produto_carrinho(id):
    qnt = request.args.get("qnt", default=1, type=int)
    #Buscar produto por id
    produto = Produto.query.get(id)
    if not produto:
        return {"erro": "Produto não encontrado"}, 404

    item = Carrinho(produto_id=produto.id, quantidade=qnt)
    db.session.add(item)
    db.session.commit()

    return {"mensagem": f"{produto.nome} adicionado ao carrinho"}



#Limpar carrinho
@app.route("/carrinho/limpar", methods=["DELETE"])
def limpar_carrinho():
    # Remove todos os itens do carrinho
    Carrinho.query.delete()
    db.session.commit()
    
    return {"mensagem": "Carrinho limpo"}, 200
