#coding:utf-8
import tornado.web

class index(tornado.web.RequestHandler):
    def get(self):
        self.write("user");