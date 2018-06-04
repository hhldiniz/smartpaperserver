from gridfs import GridFS
import os
import datetime
import hashlib


class HandlePhotoUpload(GridFS):
    def __init__(self, database):
        super().__init__(database)
        self.__database = database

    def write_on_file(self, file_id):
        if not os.path.isdir("../temp"):
            os.makedirs("../temp")
        m = hashlib.md5()
        now = datetime.datetime.now()
        file = open(f"(../temp/{m.update(now).digest()}", "wb+")
        file.write(self.get(file_id).read())
        file.close()
        return file.name
