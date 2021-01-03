def Status_200(html):
    if html.status_code == 200:
        return 0
    elif html.status_code == 302:
        print("请确保浏览器已经登录")
        exit(-1)
    elif html.status_code == 404:
        print("链接不存在")
        exit(-1)
