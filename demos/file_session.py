#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @ 2014 Mitchell Chu

from sys import version
import tornado.web
import tornado.httpserver
import tornado.ioloop
from torndsession.sessionhandler import SessionBaseHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = dict(
            debug=True,
        )
        session_settings = dict(
            driver="file",
            driver_settings=dict(
                host="#_sessions",
            ),
            force_persistence=True,
        )
        settings.update(session=session_settings)
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(SessionBaseHandler):
    def get(self):
        self.write("File Session Example:<br/>")
        # print self.session.keys()
        if "sv" in self.session:
            self.write('sv in session<br/>')
            sv = self.session["sv"]
        else:
            self.write('sv not in session<br/>')
            sv = 0
        if sv == None:
            sv = 0
        else:
            sv = int(sv) + 1
        self.write('Current Session Value:%d<br/>' % sv)
        self.write('Current Python Version: %s' % version)
        self.session["sv"] = sv


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
