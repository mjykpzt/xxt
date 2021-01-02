from bs4 import BeautifulSoup
import re


class ParseXXT:
    def __init__(self):
        self.title = []
        self.choose = []
        self.answer = []
        self.top = ''

    def pasre_total(self, html):
        soup = BeautifulSoup(html, 'lxml')
        find_all = soup.find_all('p', 'clearfix')
        url_set = set()
        for i in find_all:
            url_set.add(i.a['href'])
        return url_set

    def pasre_subject(self, html):

        soup = BeautifulSoup(html, 'lxml')
        find_all_top = soup.find_all('input', id="workLibraryTitle")
        find_all_tm = soup.find_all('div', 'Zy_TItle clearfix')
        find_all_xx = soup.find_all('ul', 'Zy_ulTop')
        find_all_da = soup.find_all('div', 'Py_answer clearfix')
        for i in find_all_top:
            self.top = i.get('value').replace('\n','')
        for i in find_all_tm:
            self.title.append(i.div.text.replace('\n', ''))
        for i in find_all_xx:
            self.choose.append(i.text.replace('\n\n', ''))
        for i in find_all_da:
            self.answer.append(i.text.replace('\n', ''))

    def pasre_pageNum(self, text):
        re_compile = re.compile(r'showPage\(\s*?\d+\s*?,\s*?(\d+)\s*?,.*?\)')
        match = re_compile.findall(text)
        group = match[0]
        return group

    def has_pageNum(self, url):
        cm = 'pageNum'
        return cm in url
