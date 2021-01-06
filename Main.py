from all_module import ChaoXing


if __name__ == '__main__':
    #网站链接
    url = "https://mooc1-1.chaoxing.com/work/getAllWork?classId=15209973&courseId=207575156&isdisplaytable=2&mooc=1&ut=s&enc=6f4cf8d39e4929095e650295b1d1b907&cpi=91622723&openc=54091f0988234fb9fbb85c4f3798b63e"
    #保存地址
    path = r'd:\yaohua.docx'
    #下载所有作业
    ChaoXing.ChaoXing(url,path).get_xxt_one_questions()