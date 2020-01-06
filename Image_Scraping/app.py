# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 22:53:25 2020

@author: Sudeep
"""

#Image Scraping project

import os
from flask import Flask, request, render_template

app = Flask('__name__')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/searchImages')
def displayImages():
    list_image = os.listdir('static')
    print(list_image)
    try:
        if(len(list_image)>0):
            return render_template('showImage.html', user_images=list_image)
        else:
            return 'Images not present'
    except Exception as e:
        print("No Image found ",e)
        return "Please try with different keyword"
    

if __name__ == '__main__':
    app.run()