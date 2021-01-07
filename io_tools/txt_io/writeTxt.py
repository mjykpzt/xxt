class WriteTxt:
    chapters = 0
    qs = 0

    def __init__(self, path):
        self.path = path
        self.encoding = 'utf8'
        self.mode = 'a+'

    def write(self, a, b, c, top):
        WriteTxt.chapters += 1
        with open(self.path, self.mode, encoding=self.encoding) as fp:
            fp.write(top+'\n')
            for i in range(len(c)):
                WriteTxt.qs += 1
                fp.write(str(i + 1) + "." + a[i]+'\n')
                if len(b[i])>0 and b[i][0] =='\n':
                    b[i]=b[i][1:]
                fp.write(b[i]+'\n')
                fp.write(c[i]+'\n')
                fp.write('\n\n')
        self.__log(top, len(c))

    def __log(self, a, b):
        print("{}下载完成，共{}题".format(a, b))
