import matplotlib
matplotlib.use('Agg')

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


# d = path.dirname(__file__)


def gen_pic_file(cache_dir, word, pic_file, gen_pic_file_name):
    # 读文本文件
    if word is None:
        text = open().read('app/templates/1.txt')
    else:
        text = word
    # 读取自定义图片
    alice_coloring = np.array(Image.open(os.path.join(cache_dir, pic_file)))
    # 你可以通过 mask 参数 来设置词云形状
    wc = WordCloud(background_color="#fff", max_words=2000,
                   mask=alice_coloring, max_font_size=50, random_state=102, scale=1,
                   font_path="app/templates/font/wqy.ttc").generate(text)
    wc.generate_from_text(text)
    print('加载文本')
    # 改变字体颜色
    img_colors = ImageColorGenerator(alice_coloring)
    # 字体颜色为背景图片的颜色
    wc.recolor(color_func=img_colors)
    # 显示词云图
    plt.imshow(wc, interpolation="bilinear")
    # 是否显示x轴、y轴下标
    plt.axis('off')
    plt.show()
    # 获得模块所在的路径的
    # d = path.dirname(__file__)
    # 将多个路径组合后返回生成图片
    wc.to_file(os.path.join(cache_dir, gen_pic_file_name))
    print('生成词云成功!')
