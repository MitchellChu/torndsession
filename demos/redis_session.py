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
        handlers = [
            (r'/', MainHandler),
        ]
        settings = dict(
            debug = True,
        )
        session_settings = dict(
            driver = "redis",
            driver_settings = dict(
                host = 'localhost',
                port = 6379,
                db = 0,
                max_connections = 1024,
            )
        )
        settings.update(session = session_settings)
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(SessionBaseHandler):
    def get(self):
        self.write("Redis Session Example:<br/>")
        if 'sv' in self.session:
            sv = self.session["sv"]
        else:
            sv = 0
        self.write('Current Session Value:%s' % sv)
        self.session['sv'] = sv + 1


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
