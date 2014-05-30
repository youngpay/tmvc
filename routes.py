#coding:utf-8

from controllers import HomeController
from tool import Tool

routes = [
    (r'/', HomeController.index),
]
routes.extend(Tool.routes_by_controllers())