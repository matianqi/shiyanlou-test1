#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import render_template,Flask
import os
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']= True

@app.route('/')
def index():
    result={}
   # course=[]
    filepath="/home/shiyanlou/files"
    for lists in os.listdir(filepath):
        p=os.path.join(filepath,lists)
        with open(p) as file:
         result[lists[:-5]]=json.loads(file.read())
    course=[item['title'] for item in result.values()]
    #     box=json.loads(file.read())
    #     a=box['title']
    #course.append(a)     
    return render_template("index.html",course=course)

@app.route('/files/<filename>')
def file(filename):
    filepath="/home/shiyanlou/files"
    t=os.path.join(filepath,filename)
    x=t+"."+"json"
    if os.path.exists(x) == True:
        with open(x,'r') as file:
           course=json.loads(file.read())
           return render_template("file.html",course=course)
    else:
       abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"),404


if __name__ == '__main__':
     app.run()
