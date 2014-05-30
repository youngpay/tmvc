#coding: utf-8

import tornado.web
from tool import Tool
from models import *

class BaseHandler(tornado.web.RequestHandler):
    module_name = None
    controller_name = None

    def parent(self):
        return super(BaseHandler, self)

    def initialize(self):
        self.module_name = self.__module__

        controller_begin = self.module_name.find(".") + 1
        self.controller_name = self.module_name[controller_begin:-10]

    def get_current_user(self):
        return self.parent().get_current_user()

    def render_view(self, template_name, **kwargs):
        return self.parent().render(self.controller_name + "/" + template_name, **kwargs)

        