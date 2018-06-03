from gridfs import GridFS, GridFSBucket
import os


class HandlePhotoUpload(GridFS):
    def __init__(self, database):
        super().__init__(database)
        self.__database = database

    def get_photo_stream(self, file_id):
        bucket = GridFSBucket(self.__database)
        if not os.path.isdir("../temp"):
            os.makedirs("../temp")
        file = open(f"../temp/{file_id}", "wb+")
        bucket.download_to_stream(file_id, file)
