class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # Novo parâmetro para armazenar o papel do usuário

    def validate(self, username, password):
        return self.username == username and self.password == password
