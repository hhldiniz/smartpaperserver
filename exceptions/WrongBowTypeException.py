class WrongBowTypeException(BaseException):
    def __init__(self, *message, **errors):
        super().__init__(*message, **errors)
