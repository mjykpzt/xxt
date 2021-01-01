from all_module import ChaoXing


if __name__ == '__main__':
    url = "http://mooc1-1.chaoxing.com/work/getAllWork?classId=15209973&courseId=207575156&isdisplaytable=2&mooc=1&ut=s&enc=6f4cf8d39e4929095e650295b1d1b907&cpi=91622723&openc=54091f0988234fb9fbb85c4f3798b63e"
    path = r'C:\yaoli.txt'
    ChaoXing.ChaoXing(url,path).get_xxt_all_questions()