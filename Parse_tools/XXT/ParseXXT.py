from bs4 import BeautifulSoup
import re


class ParseXXT:
    def __init__(self):
        self.title = []
        self.choose = []
        self.answer = []
        self.top = ''
        self.re_cid = re.compile(r"[&|?]courseId=(.*?)&")
        self.re_wid = re.compile(r"[&|?]workId=(.*?)&")

    def pasre_total(self, html):
        soup = BeautifulSoup(html, 'lxml')
        find_all = soup.find_all('p', 'clearfix')
        return self.remove_duplication_url(find_all)

    def remove_duplication_url(self, find_all):
        url_dict = dict()
        url_list = []
        for i in find_all:
            a1 = self.re_cid.findall(i.a['href'])[0]
            a2 = self.re_wid.findall(i.a['href'])[0]
            c_set = url_dict.setdefault(a1, set())
            old_len = len(c_set)
            c_set.add(a2)
            new_len = len(c_set)
            if old_len + 1 == new_len:
                url_list.append(i.a['href'])
        return url_list

    def pasre_subject(self, html):

        soup = BeautifulSoup(html, 'lxml')
        find_all_top = soup.find_all('input', id="workLibraryTitle")
        find_all_tm = soup.find_all('div', 'Zy_TItle clearfix')
        find_all_xx = soup.find_all('ul', 'Zy_ulTop')
        find_all_da = soup.find_all('div', 'Py_answer clearfix')
        for i in find_all_top:
            self.top = i.get('value').replace('\n', '')
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
