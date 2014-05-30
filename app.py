#coding:utf-8

from routes import routes

import tornado.web
import os

path = os.path.dirname(__file__)

settings = dict(
    debug = True,
    cookie_secret = "WX3RGTVTM5kmybKC8qtSAF8NCvrDieFb",
    template_path = os.path.join(path, "views"),
    static_path = os.path.join(path, "static"),
)

application = tornado.web.Application(handlers = routes, **settings)