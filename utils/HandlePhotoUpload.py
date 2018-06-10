from gridfs import GridFS
import datetime


class HandlePhotoUpload(GridFS):
    def __init__(self, database):
        super().__init__(database)
        self.__database = database

    def write_on_file(self, file_id):
        now = datetime.datetime.now()
        directory = "./files/"
        filename = f"{now}.png"
        file = open(directory+filename, "wb")
        file.write(self.get(file_id).read())
        file.close()
        return filename
