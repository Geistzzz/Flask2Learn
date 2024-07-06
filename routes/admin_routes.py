# -*- coding = utf-8 -*-
# @Time : 2024/3/10 21:24
# @Author : Geist
# @File ： admin_routes.py
# @Software: PyCharm

from routes import app

@app.route('/creat_article.html')
def create_article():
    return "Create Article"

