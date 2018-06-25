import pdfkit
import os
from datetime import datetime


class MakePDF:
    def __init__(self, content):
        self.__content = content

    def generate_from_string(self):
        if not os.path.isdir("./files/pdf"):
            os.mkdir("./files/pdf")
        filename = datetime.now()
        pdfkit.from_string(self.__content, f"./files/pdf/{filename}.pdf")
        return filename
