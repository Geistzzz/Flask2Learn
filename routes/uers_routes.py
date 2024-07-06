# -*- coding = utf-8 -*-
# @Time : 2024/3/10 21:24
# @Author : Geist
# @File ： uers_routes.py
# @Software: PyCharm
from routes import app
from flask import render_template


@app.route('/')
@app.route('/index.html')
def home_page():
    return render_template('index.html')


@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/login.html')
def login_page():
    return "login page"
