from all_module import ChaoXing


if __name__ == '__main__':

    #下载链接
    url = input("请输入下载链接：")
    #保存地址
    path = input("请输入保存路径:")
    #下载所有作业
    ChaoXing.ChaoXing(url,path).get_xxt_all_questions()