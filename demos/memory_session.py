#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 Mitchell Chu

import tornado.web
import tornado.httpserver
import tornado.ioloop
from torndsession.sessionhandler import SessionBaseHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r'/', MainHandler),
        ]
        settings = dict(
            debug = True,
        )
        session_settings = dict(
            driver="memory",
            driver_settings=dict(
                host = self,
            ),
            force_persistence = True,
        )
        settings.update(session=session_settings)
        print settings
        tornado.web.Application.__init__(self, handlers=handlers, **settings)

class MainHandler(SessionBaseHandler):
    def get(self):
        self.write("Memory Session Object Demo:")
        current_value = self.session["sv"]
        if current_value == None:
            print 'current_value is None'
            current_value = 0
        else:
            current_value = int(current_value) + 1
        self.write('<br/> Current Value is: %d' % current_value)
        self.session["sv"] = current_value

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
