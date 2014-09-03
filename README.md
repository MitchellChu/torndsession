Torndsession Session
====================

[Torndsession](https://github.com/MitchellChu/torndsession) is a session extension for [Tornado](https://github.com/tornadoweb/tornado) web framework.
Torndsession support application memory, file, redis or memcached to save session data for request, and it's easy to extend for developer.

Quick links
===========

* [Documentation](http://blog.useasp.net/category/30.aspx)
* [Source(github)](https://github.com/MitchellChu/torndsession)
* [License](https://raw.githubusercontent.com/MitchellChu/torndsession/master/LICENSE)
* [Examples](https://github.com/MitchellChu/torndsession/tree/master/demos)


Hello, Session
==============

Here is a simple "Hello, Session" example web app for Tornado with Torndsession.

	import tornado.web
    import tornado.httpserver
    import tornado.ioloop
	import torndosession

    class Application(tornado.web.Application):
	    def __init__(self):
		    handlers = [
			    (r"/", MainHandler),
			]
			settings = dict(
			    debug = True,
			)
			session_settings = dict(
			    driver = "memory",
				driver_settings = {'host':self,},
			)
			settings.update(session = session_settings)
			tornado.web.Application.__init__(self, handlers, **settings)

    class MainHandler(torndsession.sessionhandler.SessionBaseHandler):
	    def get(self):
			self.write("Hello, Session.<br/>")
			if 'data' in self.session:
                data = self.session['data']
			else:
			    data = 0
			self.write('data=%s' % data)
			self.session["autoincrement"] = data + 1
		    

    def main():
	    http_server = tornado.httpserver.HTTPServer(Application())
		http_server.listen(8000)
		tornado.ioloop.IOLoop.instance().start()

    if __name__ == "__main__":
	    main()


In this example, Request handler obtain memory session feature, it just inherit from SessionBaseHandler. more session example see this [demos](https://github.com/MitchellChu/torndsession/tree/master/demos).


Installation
============

**Automatic installation**:

    pip install torndsession

Torndsession is listed in PyPI and can be installed with `pip`or `easy_install`. Note that this installation can not install demos applicatinos which be included in source code.

**Manual installation**:

In this way, you need download the source from PyPI.

    tar xvzf torndsession.tar.gz
	cd torndsession
	python setup.py build
	sudo python setup.py install

The Torndsession source code is hosted on [GitHub](https://github.com/MitchellChu/torndsession).



Requires
========


+ [Tornado](https://github.com/tornadoweb/tornado)
+ [Redis(Optional)](http://redis.io/)
+ [Memcached(Optional)](http://memcached.org/)


LICENSE
=======
Torndsession is licensed under MIT.
