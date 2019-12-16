#coding=utf-8
from __future__ import unicode_literals
import requests
import json
import time
import random
from pyecharts.datasets.coordinates import get_coordinate
from pyecharts.chart import Chart
#下载第一页数据
def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

#解析第一页数据
def parse_one_page(html):
    data = json.loads(html)['cmts']
    for item in data:
        yield{
        'comment':item['content'],
        'date':item['time'].split(' ')[0],
        'rate':item['score'],
        'city':item['cityName'],
        'nickname':item['nickName']
        }

#保存数据到文本文档
def save_to_txt():
    for i in range(1, 11):
        url = 'http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        print('正在保存第%d页。'% i)
        for item in parse_one_page(html):
            with open('xie_zheng.txt','a',encoding='utf-8') as f:
                f.write(item['date'] + ',' + item['nickname'] + ',' + item['city'] + ',' +str(item['rate'])+','+item['comment']+'\n')
        time.sleep(5 + float(random.randint(1, 100)) / 20)

if __name__ == '__main__':
    save_to_txt()
def xie_zheng(infile,outfile):
    infopen = open(infile,'r',encoding='utf-8')
    outopen = open(outfile,'w',encoding='utf-8')
    lines = infopen.readlines()
    list_l = []
    for line in lines:
        if line not in list_l:
            list_l.append(line)
            outopen.write(line)
    infopen.close()
    outopen.close()

if __name__ == '__main__':
    xie_zheng('D:\\文件\\12.txt','D:\\文件\\13.txt')
from pyecharts import Style
from pyecharts import Geo

#读取城市数据
city = []
with open('xie_zheng.txt',mode='r',encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            city.append(row.split(',')[2].replace('\n',''))

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result
data = []
for item in all_list(city):
    data.append((item, all_list(city)[item]))
    style = Style(
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59"
        )
data = data[1:]
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff",
          title_pos="center", width=1200,
          height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 20], visual_text_color="#fff",
        symbol_size=15, is_visualmap=True)
geo.render()
