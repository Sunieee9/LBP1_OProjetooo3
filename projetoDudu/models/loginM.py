class Login:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
    def validate(self, username, password):
        return self.username == username and self.password == password