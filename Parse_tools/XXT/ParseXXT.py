from bs4 import BeautifulSoup
import re


class ParseXXT_TiMu:
    def __init__(self, top=''):
        self.title = []
        self.choose = []
        self.answer = []
        self.top = top

    def pasre_subject(self, soup):
        # soup = BeautifulSoup(html, 'lxml')
        find_tm = soup.find('div', 'Zy_TItle clearfix')
        self.title.append(find_tm.div.text.replace('\n', '').replace('\t', ''))
        find_xx = soup.find('ul', 'Zy_ulTop')
        if find_xx is not None:
            self.choose.append(find_xx.text.replace('\n\n', '').replace('\t', ''))
        else:
            find_a = soup.find("div", "Py_tk", id=False)
            if find_a:
                self.choose.append(find_a.text)
            else:
                self.choose.append("")
            find_b = soup.find("div", "Py_tk", id=True)
            if find_b:
                self.answer.append(find_b.text)
            else:
                self.answer.append("")
            return
        find_da = soup.find('div', 'Py_answer clearfix')
        self.answer.append(find_da.text.replace('\n', '').replace('\t', ''))


class parseXXTPage:
    def __init__(self):
        self.tiMus = []

    def pasre_timus(self, html):
        soup = BeautifulSoup(html, 'lxml')
        find_all = soup.find_all('div', 'TiMu')
        for i in find_all:
            self.tiMus.append(i)


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
