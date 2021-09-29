import requests
import json
import time
from lxml import html

f = open("uid.txt", "r")    # 读入uid文本文档

lines = f.readlines()  # 读取全部内容

for line in lines:
    print('正在处理: ', line)

    # 定义uid，api，headers

    line = line.rstrip("\n")
    uid = int(line)

    api = 'http://api.bilibili.com/x/web-interface/card?mid={}'.format(uid)    # 使用的接口不同
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }

    # 配置response和user_data
    resp = requests.get(api, headers=headers)
    user_data = resp.text
    selector = html.fromstring(user_data)

    # 返回Python数据类型
    user_data = json.loads(user_data)

    #   part 2

    api2 = 'http://api.bilibili.com/x/space/upstat?mid={}'.format(uid)    # 使用的接口不同
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        'Cookie': 'SESSDATA=7f7791ed%2C1648444103%2C7978a*91'
    }

    # 配置response和user_data
    resp2 = requests.get(api2, headers=headers2)
    user_data2 = resp2.text
    selector2 = html.fromstring(user_data2)

    # 返回Python数据类型
    user_data2 = json.loads(user_data2)

    # 定义查询变量
    NickName = user_data['data']['card']['name']  # 昵称
    level = user_data['data']['card']["level_info"]['current_level']  # 用户等级
    # archive_count = user_data['data']["archive_count"]  # 视频数
    follower = user_data['data']['follower']    # 粉丝数
    like_num = user_data['data']['like_num']  # 获赞数
    archive_view = user_data2['data']['archive']['view']
    article_view = user_data2['data']['article']['view']

    time.sleep(2)
    f2 = open('data2.txt', 'a', encoding='utf-8')
    someinfo = f'@[{NickName}](https://space.bilibili.com/{uid}) uid:{uid} 粉丝:{follower} 获赞:{like_num} 视频播放量:{archive_view} 专栏阅读量:{article_view}\n'
    f2.writelines(str(someinfo))
    f2.write('\r')
    f2.close()
