import requests
import json
import time
import random
from pyecharts import Pie
#下载第一页数据
def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None
#解析第一页数据
def parse_one_page(html):
    data = json.loads(html)['cmts']
    for item in data:
        yield{
            'data': item['time'].split(' ')[0],
            'nickname': item['nickName'],
            'city': item['cityName'],
            'rate': item['score'],
            'comment': item['content']
        }
#保存数据到文本文档
def save_to_txt():
    for i in range(1, 2):
        url = 'http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        print('正在保存第%d页。' % i)
        for item in parse_one_page(html):
            with open('xie_zheng.txt', 'a', encoding='utf-8') as f:
                f.write(item['data'] + ',' + item['nickname'] + ',' + item['city'] + ',' +str(item['rate'])+','+item['comment']+'\n')
                time.sleep(5 + float(random.randint(1, 100)) / 20)

if __name__ == '__main__':
    save_to_txt()

def xie_zheng(infile,outfile):
    infopen = open(infile, 'r', encoding="utf-8")
    outopen = open(outfile, 'w', encoding='utf-8')
    lines = infopen.readlines()
    list_l = []
    for line in lines:
        if line not in list_l:
            list_l.append(line)
            outopen.write(line)
        infopen.close()
        outopen.close()
if __name__ == '__main__':
    xie_zheng('D:\\文件\\12.txt', 'D:\\文件\\13.txt')
#读取城市数据
from pyecharts import Style
from pyecharts import Geo
from pyecharts import Map
city = []
with open('xie_zheng.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            city.append(row.split(',')[2].replace('\n', ''))
def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result
data = []
for item in all_list(city):
    data.append((item, all_list(city)[item]))
    data = data[1:-1]
    style = Style(
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59"
    )
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff",
          title_pos="center", width=1200,
          height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 20], visual_text_color="#fff",
        symbol_size=15, is_visualmap=True)
geo.render()
import pickle
from  os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImagesColorGenerator

comment = []
with open('quan.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            comment.append(row.split(',')[4].replace('\n', ''))
comment_after_split = jieba.cut(str(comment), cut_all=False)
wl_space_split = "".join(comment_after_split)
#导入背景图
backgroud_Image = plt.imread('C:\\Users\\11826\\Desktop\\E-beijing.jpg')
stopwords = STOPWORDS.copy()
#可以添加多个屏蔽词
stopwords.add("u电影")
stopwords.add("u一部")
stopwords.add("u没有")
stopwords.add("u什么")
stopwords.add("u有点")
stopwords.add("u觉得")
stopwords.add("u真的")
stopwords.add("u还是")
stopwords.add("u不是")
#设置词云参数
#参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
wc = WordCloud(width=1024, height=768, backgroud_color='white',
               mask=backgroud_Image, font_path="C:\\simhei.ttf",
               stopwords=stopwords, max_fot_size=400,
               random_state=50)
wc.generate_from_text(wl_space_split)
img_colors = ImagesColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')#不显示坐标轴
plt.show()
#保持结果到本地
wc.to_file('D:\\文件\\文档\\123.txt')
from pyecharts import ThemeRiver
rate = []
with open('quan.txt',mode='r',encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            rate.append(row.split(',')[3].replace('\n', ''))
print(rate.count('5')+rate.count('4.5'))
print(rate.count('4')+rate.count('3.5'))
print(rate.count('3')+rate.count('2.5'))
print(rate.count('2')+rate.count('1.5'))
print(rate.count('1')+rate.count('0.5'))
#饼状图
from pyecharts import Pie
attr  = ["五星", "四星", "三星", "二星", "一星"]
#分别代表各星级评论数
vl = [3324, 1788, 1293, 553, 1653]
Pie = Pie("饼图-星级玫瑰图示例", title_pos='center', width=900)
Pie.add("7-17", attr, vl, center=[75, 50], is_random=True,
        radius=[30, 75], rosetype='area',
        is_legend_show=False, is_label_show=True)
Pie.render()

data1 = json.load()
