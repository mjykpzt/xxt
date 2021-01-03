from bs4 import BeautifulSoup
import re


class ParseXXTPage:
    def __init__(self, top=''):
        self.title = []
        self.choose = []
        self.answer = []
        self.top = top

    def pasre_subject(self, html):
        soup = BeautifulSoup(html, 'lxml')
        find_all_tm = soup.find_all('div', 'Zy_TItle clearfix')
        find_all_xx = soup.find_all('ul', 'Zy_ulTop')
        find_all_da = soup.find_all('div', 'Py_answer clearfix')
        for i in find_all_tm:
            self.title.append(i.div.text.replace('\n', '').replace('\t', ''))
        for i in find_all_xx:
            self.choose.append(i.text.replace('\n\n', '').replace('\t', ''))
        for i in find_all_da:
            self.answer.append(i.text.replace('\n', '').replace('\t', ''))


class ParseXXTUrl:
    re_cid = re.compile(r"[&|?]courseId=(.*?)&")
    re_wid = re.compile(r"[&|?]workId=(.*?)&")
    re_compile = re.compile(r'showPage\(\s*?\d+\s*?,\s*?(\d+)\s*?,.*?\)')

    def __init__(self):
        self.urls = []
        self.tops = []

    def pasre_total(self, html):
        soup = BeautifulSoup(html, 'lxml')
        find_all = soup.find_all('p', 'clearfix')
        self.remove_duplication_url(find_all)

    def remove_duplication_url(self, find_all):
        url_dict = dict()
        for i in find_all:
            url = i.a['href']
            a1 = ParseXXTUrl.re_cid.findall(url)[0]
            a2 = ParseXXTUrl.re_wid.findall(url)[0]
            c_set = url_dict.setdefault(a1, set())
            old_len = len(c_set)
            c_set.add(a2)
            new_len = len(c_set)
            if old_len + 1 == new_len:
                self.urls.append(url)
                self.tops.append(i.a["title"])

    def pasre_pageNum(self, text):
        match = ParseXXTUrl.re_compile.findall(text)
        group = match[0]
        return group

    def has_pageNum(self, url):
        cm = 'pageNum'
        return cm in url
