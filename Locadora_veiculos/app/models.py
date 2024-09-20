from . import db


""" class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True,nullable=False)

    def __repr__(self):
        return f'<User> {self.username}' """



class usuario(db.Model):
    __tablename__ = 'usuario'
    
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80),nullable=False)
    senha = db.Column(db.int, nullable=False)
    tipo = db.Column(db.String, nullable=False)
    status = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<usuario> {self.nome}'
    
    
class dados_pessoais(db.Model):
    __tablename__ = 'dados_pessoais'
    
    id_dados_pessoais = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(80),nullable=False)
    anoNascimento = db.Column(db.int, nullable=False)
    rg = db.Column(db.int, nullable=False)
    cpf = db.Column(db.int, nullable=False)
    telefone = db.Column(db.int, nullable=False)
    id_usuario = db.Column(db.int, nullable=False)

    def __repr__(self):
        return f'<dados_pessoais> {self.nome}'

class veiculo(db.Model):
    __tablename__ = 'veiculo'
    
    id_veiculo = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(80),nullable=False)
    modelo = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    ano = db.Column(db.int, nullable=False)
    precoDia = db.Column(db.Float, nullable=False)
    disponibilidade = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<veiculo> {self.nome}'
    
class reserva(db.Model):
    __tablename__ = 'reserva'
    
    id_reserva = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String, nullable=False)
    veiculo = db.Column(db.String, nullable=False)
    datainicio = db.Column(db.Date, nullable=False)
    datafim = db.Column(db.Date, nullable=False)
    status = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<reserva> {self.nome}'
    
    
class manutencao(db.Model):
    __tablename__ = 'manutencao'
    
    id_manutencao = db.Column(db.Integer, primary_key=True)
    veiculo = db.Column(db.String(80),nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    datainicio = db.Column(db.Date, nullable=False)
    datafim = db.Column(db.Date, nullable=False)
    

    def __repr__(self):
        return f'<manutencao> {self.nome}'