from html.parser import HTMLParser


class HTMLConsumer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__tags_attrs = {}
        self.__html_text = []

    def error(self, message):
        print(message)

    def handle_starttag(self, tag, attrs):
        try:
            value = self.__tags_attrs.__getitem__(tag)
            attrs.append(('text', self.get_html_text()[self.get_html_text().__len__()-1]))
            value.append(attrs)
            self.__tags_attrs.__setitem__(tag, value)
        except KeyError:
            self.__tags_attrs.__setitem__(tag, [attrs])

    def handle_data(self, data):
        self.set_html_text(data)

    def unknown_decl(self, data):
        print(f"Conteúdo desconhecido: #{data}")

    def get_tag_content(self, tag_name, tag_attrs):
        try:
            if tag_name is not None and tag_name is not "":
                all_tags_attrs = self.__tags_attrs.__getitem__(tag_name)
            else:
                all_tags_attrs = self.__tags_attrs
            for attr in all_tags_attrs:
                print(attr)
            return all_tags_attrs
        except KeyError:
            return None

    def get_tags_attrs(self):
        return self.__tags_attrs

    def set_html_text(self, new_text):
        self.__html_text.append(new_text)

    def get_html_text(self):
        return self.__html_text
