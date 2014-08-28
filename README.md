Torndsession Tornado web session
===================

[Torndsession](https://github.com/MitchellChu/torndsession) is a Tornado web framework session extension. At the current, Torndsession support user to use application memory to save session object, file session object, redis and memcached, user also can add other easy.

Hello, Session
==============

Here is a simple "Hello, Session" example web app for Tornado with Torndsession.

    import tornado.ioloop
	import tornado.web
	import datetime
	import torndosession

    class Application(tornado.web.Application):
	    def __init__(self):
		    handlers = [
			    (r"/", MainHandler),
			]
			settings = dict(
			    debug = True
			)
			session_settings = dict(
			    driver = "memory",
				driver_settings = {'host':self,},
				force_persistence = True,
				cache_driver = True,
				cookie_config = {
				    'expires_days':10,
					'expires':datetime.datetime.utcnow(),
				},
			)
			settings.update("session", session_settings)
			tornado.web.Application.__init__(self, handlers, **settings)

    class BaseHandler(tornado.web.RequestHandler, torndosession.SessionMixin):
	    pass

    class MainHandler(BaseHandler):
	    def get(self):
			self.write("Hello, Session.")
			current_value = self.session["autoincrement"]
			if not current_value:
				current_value = 0
			else:
			    current_value = int(current_value) + 1
			self.write('Current Session Value:%d' % current_value)
			self.session["autoincrement"] = current_value
		    

    def main():
	    http_server = tornado.httpserver.HTTPServer(Application())
		http_server.listen(80000)
		tornado.ioloop.IOLoop.instance().start()

    if __name__ == "__main__":
	    main()


Quick User Guide
=============





