# -*- coding = utf-8 -*-
# @Time : 2024/3/10 21:29
# @Author : Geist
# @File ： __init__.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__, template_folder='../templates',
            static_folder='../assets', static_url_path='/assets')

from routes import admin_routes, uers_routes
