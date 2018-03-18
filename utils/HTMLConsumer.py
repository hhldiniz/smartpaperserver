from html.parser import HTMLParser


class HTMLConsumer(HTMLParser):
    def error(self, message):
        print(message)

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
