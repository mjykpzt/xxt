from all_module import ChaoXing


if __name__ == '__main__':
    #网站链接
    url = "https://mooc1-1.chaoxing.com/work/getAllWork?classId=32156934&courseId=214651812&isdisplaytable=2&mooc=1&ut=s&enc=86e44f785249b6d120323d8520afe8ba&cpi=91622723&openc=fa826f178f47fb0a3ea03b8d1ef1e039"
    #保存地址
    path = r'd:\yaohua.docx'
    #下载所有作业
    ChaoXing.ChaoXing(url,path).get_xxt_one_questions()