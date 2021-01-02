from docx import Document
from io_tools.docx_io.docx_utils import doxc_func
import os

class W_Docx:
    chapters = 0
    qs = 0

    def __init__(self, path, top_size=12, title_size=10, main_size=10, answer_size=10,
                 top_color=None, title_color=None, main_color=None, answer_color=None):
        self.__docx_init(path)
        self.document = Document(path)
        self.path = path
        self.title_size = title_size
        self.main_size = main_size
        self.top_size = top_size
        self.answer_size = answer_size
        self.title_color = [0, 0, 0]
        self.main_color = [0, 0, 0]
        self.top_color = [0, 0, 0]
        self.answer_color = [255, 0, 0]
        if title_color is not None:
            self.title_color = title_color
        if main_color is not None:
            self.main_color = main_color
        if title_color is not None:
            self.top_color = top_color
        if answer_color is not None:
            self.answer_color = answer_color

    def write(self, a, b, c, top):
        W_Docx.chapters += 1
        self.w_top(top)
        for i in range(len(c)):
            self.w_title(str(i + 1) + "." + a[i])
            self.w_main(b[i])
            self.w_answer(c[i])
            W_Docx.qs += 1
        self.__log(top, len(c))

    def __log(self, a, b):
        print("{}下载完成，共{}题".format(a, b))

    def __docx_init(self, path):
        if not os.path.exists(path):
            doc = Document()
            doc.save(path)

    def w_top(self, text):
        doxc_func.AddHeadText(self.document, text, self.top_size, self.top_color)

    def w_title(self, text):
        doxc_func.AddParagraphText(self.document, text, self.title_size, self.title_color)

    def w_main(self, text):
        if text[0] == '\n':
            text = text[1:]
        doxc_func.AddParagraphText(self.document, text, self.main_size, self.main_color)

    def w_answer(self, text):
        doxc_func.AddParagraphText(self.document, text, self.answer_size, self.answer_color)

    def save(self):
        self.document.save(self.path)
