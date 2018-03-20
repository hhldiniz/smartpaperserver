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

    def get_tag_content(self, tag_name, tag_attrs):
        try:
            all_tags_attrs = self.__tags_attrs.__getitem__(tag_name)
            for attr in all_tags_attrs:
                print(attr)
        except KeyError:
            return None
