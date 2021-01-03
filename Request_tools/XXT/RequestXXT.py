from Browser_tools import BrowserReader
import requests
from Request_tools import StatusTreatment

class RequestXXT:
    def __init__(self, url):
        self.url = url
        self.headers = self.__init_headers()

    def __init_cookie(self):
        cookies1 = BrowserReader.GoogleBrowerCookie(".chaoxing.com").get_cookie_str()
        cookies2 = BrowserReader.GoogleBrowerCookie("mooc1-1.chaoxing.com").get_cookie_str()

        return (cookies1 + cookies2)[:-1]

    def __init_headers(self):
        headers = dict()
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
                                ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        headers['host'] = 'mooc1-1.chaoxing.com'
        headers["accept-language"] = 'zh-CN,zh;q=0.9'
        headers['accept'] = 'text/html,application/xhtml+xml,application/xml;' \
                            'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,' \
                            'application/signed-exchange;v=b3;q=0.9'
        headers['Connection'] = 'keep-alive'
        headers['Cache-Control'] = 'max-age=0'
        headers['Upgrade-Insecure-Requests'] = '1'
        headers['Referer'] = self.url
        headers['cookie'] = self.__init_cookie()

        return headers

    def request_xxt(self):
        html = requests.get(self.url, headers=self.headers, allow_redirects=False)
        html.encoding = html.apparent_encoding
        StatusTreatment.Status_200(html)
        return html.text
