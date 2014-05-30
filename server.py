#coding:utf-8

import tornado.ioloop
import sys
import datetime
from app import application

PORT = '8080'

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PORT = sys.argv[1]
        
application.listen(PORT)
print 'Development server is running at http://127.0.0.1:%s/' % PORT
print 'Quit the server with CONTROL-C'
print datetime.datetime.now().isoformat(' ')
tornado.ioloop.IOLoop.instance().start()