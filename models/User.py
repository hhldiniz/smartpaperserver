import os

from utils.DBController import DBController
from utils.HandlePhotoUpload import HandlePhotoUpload


class User:
    def __init__(self, name="", email="", username="", password="", photo=None):
        self.__name = name
        self.__email = email
        self.__username = username
        self.__password = password
        self.__photo = photo
        self.__id = None

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_photo(self, photo):
        self.__photo = photo

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_photo(self):
        return self.__photo

    def __get_photo_stream(self):
        if os.environ.get("MONGODB_URI") is None:
            db_controller = DBController()
        else:
            db_controller = DBController(uri=os.environ.get("MONGODB_URI"))
        db_controller.connect()
        handle = HandlePhotoUpload(db_controller.get_database())
        file_id = self.get(
            {
                "username": self.get_username(),
                "password": self.get_password()
            })[0]["photo"]
        return handle.write_on_file(file_id)

    def get_user_photo(self, send_from_directory):
        return send_from_directory(f"./files", self.__get_photo_stream())

    def __save_photo(self):
        if os.environ.get("MONGODB_URI") is None:
            db_controller = DBController()
        else:
            db_controller = DBController(uri=os.environ.get("MONGODB_URI"))
        db_controller.connect()
        handle = HandlePhotoUpload(db_controller.get_database())
        return handle.put(self.get_photo())

    def save(self):
        if os.environ.get("MONGODB_URI") is None:
            db_controller = DBController()
        else:
            db_controller = DBController(uri=os.environ.get("MONGODB_URI"))
        db_controller.connect()
        insert_result = db_controller.insert("users",
                                             {
                                                 "name": self.__name,
                                                 "username": self.__username,
                                                 "password": self.__password,
                                                 "email": self.__email,
                                                 "photo": self.__save_photo()
                                             })
        return insert_result.inserted_id is not None

    @staticmethod
    def get(select_filter):
        if os.environ.get("MONGODB_URI") is None:
            db_controller = DBController()
        else:
            db_controller = DBController(uri=os.environ.get("MONGODB_URI"))
        db_controller.connect()
        return db_controller.as_array("users", select_filter)
