from gridfs import GridFS


class HandlePhotoUpload(GridFS):
    def __init__(self, database):
        super().__init__(database)
        self.__database = database

    def write_on_file(self, file_id):
        directory = "./files/"
        filename = f"{file_id}.png"
        file = open(directory+filename, "wb")
        file.write(self.get(file_id).read())
        file.close()
        return filename
