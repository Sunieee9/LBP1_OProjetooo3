# Lista de usuários e senhas
usuarios = {
    "jorginho1": "senha1",
    "paulinha2": "senha2",
    "jordania9": "senha3",
}

class Login:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
def verificar_credenciais(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    return False

usuario_input = input("Digite o nome de usuário: ")
senha_input = input("Digite a senha: ")

if verificar_credenciais(usuario_input, senha_input):
    print("Acesso permitido.")
else:
    print("Usuário ou senha incorretos.")


