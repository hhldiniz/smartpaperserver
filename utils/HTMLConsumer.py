from html.parser import HTMLParser


class HTMLConsumer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__tags_attrs = {}

    def get_tags_attrs(self):
        return self.__tags_attrs

    def error(self, message):
        print(message)

    def handle_starttag(self, tag, attrs):
        try:
            value = self.__tags_attrs.__getitem__(tag)
            value.append(attrs)
            self.__tags_attrs.__setitem__(tag, value)
        except KeyError:
            self.__tags_attrs.__setitem__(tag, [attrs])

    def handle_endtag(self, tag):
        pass
        # print("Encountered an end tag :", tag)
