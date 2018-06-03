from gridfs import GridFS


class HandlePhotoUpload(GridFS):
    def __init__(self, database):
        super().__init__(database)
