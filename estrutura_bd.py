#TOMAR CUIDADO NA HORA DE CRIAR UMA ESTRUTURA_BD NA RELAÇÃO DE NOME E SENHA POIS ESSES DADOS PRECISAM ESTAR DE ACORDO (continua...
# E PARALELOS AO USUARIO E SENHA DE UMA POSTERIOR API, (CASO CRIE UMA API) -ISSO SE FAZ POR SEGURANÇA PARA OS DADOS SEREM ACESSADOS SOMENTE COM UM LOGIN DE AUTENTICAÇÃO COM USUARIO E POSTERIORMENTE RECEBER UM TOKEN NA HORA DE USÁ-LOS PARA PREENCHIMENTO (continua...
#ACONTECEU DE EU NÃO PRESTAR ATENÇÃO E ALTERAR O USUÁRIO E SENHA E DAR ERRO NO POSTMAN E FIQUEI BOIANDO, (CUSTEI DESCOBRIR O MOTIVO 😒)
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar um API flask
app = Flask(__name__)
# Criar um instância de SQLAlchemy
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db: SQLAlchemy

# Definir a estrutra da tabela Postagem: id_postagem, titulo, autor


class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))
# Definir a estrutra da tabela Autor: id_autor, nome, email, senha, admin, postagens


class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')


def inicializar_banco():
    # Executar o comando para criar o banco de dados
    db.drop_all()
    db.create_all()
    # Criar usuários adminstradores
    autor = Autor(nome='sidemar', email='fatorandoamatematica@gmail.com',
                    senha='123456', admin=True)
    db.session.add(autor)
    db.session.commit()


if __name__ == "__main__":
    inicializar_banco()
