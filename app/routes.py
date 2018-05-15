import imghdr
import os
import sys
import uuid

from flask import render_template, flash, redirect, url_for, request, send_from_directory

from app import app, genlogo, gen_file_name

interface_path = os.path.dirname(__file__)
sys.path.insert(0, interface_path)


@app.route('/')
@app.route('/index')
def index():
    return render_template("pic.html")


@app.route("/upload", methods=['post'])
def upload():
    pic = request.files.get('pic')  # 获取上传的文件
    word = request.form.get('word')
    if pic:
        img_type = imghdr.what(pic)
        if img_type == 'jpeg':
            cache_dir = 'app/static/cache/'
            tmp = str(uuid.uuid4())
            new_pic_name = gen_file_name.gen_new_file_name(tmp, pic.filename)

            pic.save(os.path.join(cache_dir, new_pic_name))  # 保存文件到指定路径
            gen_pic_name = 'g_' + new_pic_name

            genlogo.gen_pic_file(cache_dir, word, new_pic_name, gen_pic_name)
            return '{"msg":"<a target=\'_blank\' href=\'cache?pic=' + new_pic_name + '\'>下载</a>"}'
        else:
            return '{"msg": "文件类型不正确"}'
    else:
        return '{"msg": "请上传文件！"}'


@app.route("/cache", methods=['get'])
def show_gen():
    pic_name = request.args.get('pic')
    return render_template("gen.html", pic_name="static/cache/" + pic_name, gen_pic_name="static/cache/g_" + pic_name)
