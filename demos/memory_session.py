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
            (r'/', MainHandler),
            (r'/del', DeleteHandler),
        ]
        settings = dict(
            debug=True,
        )
        session_settings = dict(
            driver="memory",
            driver_settings=dict(
                host=self,
            ),
            force_persistence=True,
        )
        settings.update(session=session_settings)
        tornado.web.Application.__init__(self, handlers=handlers, **settings)


class MainHandler(SessionBaseHandler):
    def get(self):
        self.write("Memory Session Object Demo:<br/>")
        if "sv" in self.session:
            current_value = self.session["sv"]
        else:
            current_value = 0
        if not current_value:
            self.write("current_value is None(0)<br/>")
            current_value = 1
        else:
            current_value = int(current_value) + 1
        self.write('<br/> Current Value is: %d' % current_value)
        self.write('<br/>Current Python Version: %s' % version)
        self.session["sv"] = current_value


class DeleteHandler(SessionBaseHandler):
    def get(self):
        '''
        Please don't do this in production environments.
        '''
        self.write("Memory Session Object Demo:")
        if "sv" in self.session:
            current_value = self.session["sv"]
            self.write("current sv value is %s, and system will delete this value.<br/>" % self.session["sv"])
            self.session.delete("sv")
            if "sv" not in self.session:
                self.write("current sv value is empty")
        else:
            self.write("Session data not found")


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
