from Request_tools.XXT import RequestXXT
from Parse_tools.XXT import ParseXXT
from io_tools.txt_io import writeTxt
from io_tools.docx_io import WriteDocx
import time
import random
import re


class ChaoXing:
    def __init__(self, url, path):
        self.base_url = "http://mooc1-1.chaoxing.com"
        self.url_st = "&pageNum="
        self.url = url
        self.path = path
        self.save_type = self.__parse_path()
        # self.url_type= self.__parse_url()
        self.start_page = 1
        self.end_page = int(self.get_end_page())
        self.url_flag = ParseXXT.ParseXXTUrl().has_pageNum(url)
        self.res = re.compile(r"{}\d+".format(self.url_st))
        self.sleep_time = [3, 5]

    def get_main_text(self, url):
        return RequestXXT.RequestXXT(url).request_xxt()

    def get_end_page(self):
        return ParseXXT.ParseXXTUrl().pasre_pageNum(self.get_main_text(self.url))

    def get_xxt_one_questions(self, url=None):
        """
        获取当前页面的题目
        :param url:
        :return:
        """
        if url is None:
            url = self.url
        parseXXTUrl = ParseXXT.ParseXXTUrl()
        parseXXTUrl.pasre_total(self.get_main_text(url))
        for i in range(len(parseXXTUrl.urls)):
            text = RequestXXT.RequestXXT(self.base_url + parseXXTUrl.urls[i]).request_xxt()
            xxt_page = ParseXXT.parseXXTPage()
            xxt_page.pasre_timus(text)
            all_tm = ParseXXT.ParseXXT_TiMu(top=parseXXTUrl.tops[i])
            for j in xxt_page.tiMus:
                all_tm.pasre_subject(j)
            self.__write(all_tm)
            time.sleep(random.uniform(self.sleep_time[0], self.sleep_time[1]))

    def get_xxt_all_questions(self):
        """
        获取所有的题目
        :return:
        """
        self.get_xxt_one_questions()
        if self.end_page > 1:
            url = self.url
            if not self.url_flag:
                url += self.url_st + "2"
            for i in range(2, self.end_page + 1):
                new_url = self.res.sub(self.url_st + str(i), url, 1)
                self.get_xxt_one_questions(new_url)
                time.sleep(random.uniform(self.sleep_time[0], self.sleep_time[1]))
        self.__log()

    def __parse_path(self):
        """
        解析保存路径来判断保存的文件格式，默认是txt
        :return:
        """
        a = self.path.split('.')[-1]
        if a == 'docx':
            return 1
        return 0

    # def __parse_url(self):
    #     re_compile = re.compile(r"mooc2-ans.chaoxing.com")
    #     findall = re_compile.findall(self.url)
    #     return len(findall)>0

    def __write(self, all_tm):
        """
        根据type来调用相应的写函数
        :param all_tm:
        :return:
        """
        if self.save_type == 0:
            writeTxt.WriteTxt(self.path).write(all_tm.title, all_tm.choose, all_tm.answer, all_tm.top)
        elif self.save_type == 1:
            w_docx = WriteDocx.W_Docx(self.path)
            w_docx.write(all_tm.title, all_tm.choose, all_tm.answer, all_tm.top)
            w_docx.save()

    def __log(self):
        print("下载全部完成，一共{}章节,{}题".format(writeTxt.WriteTxt.chapters, writeTxt.WriteTxt.qs))
