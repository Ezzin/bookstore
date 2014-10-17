__author__ = 'yxc'

import tornado.options
import tornado.ioloop
import tornado.web
import tornado.httpserver
import os
import MySQLdb

from tornado.options import options, define
define("port", default="8000", help="run on this port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handler = [(r"/", MainHandler),
                   (r"/list", ListHandler)]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={"Book": BookModule},
            debug=True,)
        conn = MySQLdb.connect(user="root", db="blog", passwd=yxc, host="localhost")
        cursor = conn.cursor()
        tornado.web.Application.__init__(self, handler, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("homepage.html", title="yxc")

    def post(self, *args, **kwargs):
        pass


class ListHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("list.html", title=False, bookname="Not yet")

    def post(self, *args, **kwargs):
        book_name = self.get_argument("bookname")
        self.render("list.html", book_name=book_name)


class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string("module/book.html", book=book)

    def css_files(self):
        return "/static/css/main/style.css"

    def javascript_files(self):
        return "/static/js/main.js"


class BookStore(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        book_name = self.get_argument("book_name")
        book_isbn = self.get_argument("book_isbn")
        book_auther = self.get_argument("book_auther")
        book_price = self.get_argument("book_price")
        book_cover = self.get_argument("book_cover")




class BookSearch(tornado.web.RequestHandler):
    def get(self):
        key = self.get_argument("name")
        conn = self.application.db.test
        book = conn.find_one({key: "isbn"})
        if book:
            book_isbn = book
        else:
            book_isbn = 0
        self.render("url", book_isbn)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.httpserver.HTTPServer(Application())
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
