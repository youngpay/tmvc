#coding:utf-8
import tornado.web
from controller import BaseHandler

class index(BaseHandler):
    def get(self):
        self.render_view("index.html", data = "nil")

class about(BaseHandler):
    def get(self):
        self.render_view("about.html")