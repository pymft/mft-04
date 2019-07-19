import re
import urllib.request


class WebBrowser:
    instances = {}

    def __new__(cls, url):
        if url not in cls.instances:
            cls.instances[url] = super().__new__(cls)
            cls.instances[url].url = url
            cls.instances[url].__text = None
            cls.instances[url].unread = True

        return cls.instances[url]

    @property
    def text(self):
        if self.__text is None:
            fp = urllib.request.urlopen(self.url)
            self.__text = fp.read().decode("utf8")
            self.unread = False
        return self.__text

    @property
    def links(self):
        text = self.text
        pat = r"""href=[\'"]?(https?://[^\'" >]+)"""
        links =re.findall(pat, text)
        return [WebBrowser(link) for link in links]

    @classmethod
    def count(cls):
        return len(cls.instances)

    @classmethod
    def count_read(cls):
        res = [s for s in cls.instances.values() if s.unread == False]
        return len(res)

    def __repr__(self):
        return self.url


if __name__ == '__main__':
    wb1 = WebBrowser("https://www.python.org")

    text = wb1.links[10].links
    text = wb1.links[11].text
    print(WebBrowser.count_read())
    # print(text)


