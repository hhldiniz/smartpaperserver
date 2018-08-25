from models.User import User
from utils.DBController import DBController


class TestUser(User):
    def __init__(self):
        super().__init__()
        self.set_email("teste@teste.com")
        self.set_name("Usuário Teste")
        self.set_password("123456")
        self.set_username("usuarioteste")

    def suicide(self):
        db_controller = DBController()
        db_controller.connect()
        return db_controller.delete("users", {"email": self.get_email(),
                                              "name": self.get_name(),
                                              "password": self.get_password(),
                                              "username": self.get_username()})

    def save(self):
        db_controller = DBController()
        db_controller.connect()
        insert_result = db_controller.insert("users",
                                             {
                                                 "name": self.get_name(),
                                                 "username": self.get_username(),
                                                 "password": self.get_password(),
                                                 "email": self.get_email(),
                                             })
        return insert_result.inserted_id is not None