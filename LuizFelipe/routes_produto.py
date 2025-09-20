from flask import request
from app import app, db
from models import Produto



# Rota raiz
@app.route("/")
def home():
    return {"mensagem": "Bem Vindo a api-carrinho"}



# Listar todos os produtos
@app.route("/produto/all", methods=["GET"])
def get_produtos():
    # Buscar todos os produtos no banco
    produtos = Produto.query.all()
    
    # Transformar objetos Produto em dicionário para JSON
    lista = []
    for p in produtos:
        lista.append({
            "id": p.id,
            "nome": p.nome,
            "marca": p.marca,
            "preco": p.preco,
            "descricao": p.descricao
        })
    return {"PRODUTOS": lista}



# Criar novo produto
@app.route("/produto/save", methods=["POST"])
def post_produto():
    dados_json = request.json

    obrigatorio = ["nome", "marca", "preco", "descricao"]
    for campo in obrigatorio:
        if campo not in dados_json:
            return {"erro": f"Dado faltando: {campo}"}, 400

    # Criando objeto Produto (representa uma linha no banco)
    novo_produto = Produto(
        nome=dados_json["nome"],
        marca=dados_json["marca"],
        preco=dados_json["preco"],
        descricao=dados_json["descricao"]
    )

    # Salvando no banco
    db.session.add(novo_produto)
    db.session.commit()

    return {"mensagem": "Produto criado", "id": novo_produto.id}, 201



# Buscar produto por ID
@app.route("/produto/<int:id>/buscar")
def get_produto_especifico(id):
    # Busca no banco
    produto = Produto.query.get(id)

    if not produto:
        return {"erro": "Produto não encontrado"}, 404

    return {
        "id": produto.id,
        "nome": produto.nome,
        "marca": produto.marca,
        "preco": produto.preco,
        "descricao": produto.descricao
    }



# Atualizar produto
@app.route("/produto/<int:id>/update", methods=["PUT"])
def update_produto(id):
    dados_json = request.json

    produto = Produto.query.get(id)
    if not produto:
        return {"erro": "Produto não encontrado"}, 404

    # Atualizando campos
    produto.nome = dados_json["nome"]
    produto.marca = dados_json["marca"]
    produto.preco = dados_json["preco"]
    produto.descricao = dados_json["descricao"]

    db.session.commit()

    return {"mensagem": f"{produto.nome} atualizado"}


# Deletar produto
@app.route("/produto/<int:id>/delete", methods=["DELETE"])
def deletar_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return {"erro": "Produto não encontrado"}, 404

    db.session.delete(produto)
    db.session.commit()

    return {"mensagem": "Produto deletado"}