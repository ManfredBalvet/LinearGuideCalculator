from urllib import request
from html.parser import HTMLParser


def get_live_price(shaft_lengths: list[int]) -> list[float]:
    price_list = []
    for i, shaft_length in enumerate(shaft_lengths):
        parser = ReadHTML()
        url = f"https://vention.io/parts/16mm-shaft-for-linear-bearings-{shaft_length}mm-147{i + 1}"
        response = request.urlopen("https://vention.io/parts/16mm-shaft-for-linear-bearings-585mm-1471")
        web_content = response.read().decode('UTF-8')
        parser.feed(web_content)
        price_list.append(parser.price)

    return price_list


class ReadHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag = ""
        self.attr = ""
        self.price = float()

    def handle_starttag(self, tag, attrs):
        self.tag = tag
        self.attr = attrs
        print(attrs)

    def handle_endtag(self, tag: str) -> None:
        self.tag = tag

    def handle_data(self, data):
        print(self.attr)
        if "product-page-viewer-price" in self.attr[1]:
            self.price = float(data.split(" ")[0].replace("$", ""))
