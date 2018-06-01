from models.User import User


class TestUser(User):
    def __init__(self):
        super().__init__()
        self.set_email("teste@teste.com")
        self.set_name("Usuário Teste")
        self.set_password("123456")
        self.set_username("usuarioteste")
