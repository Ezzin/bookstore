__author__ = 'yxc'
#-*- coding: utf-8 -*-

import tornado.options
import tornado.ioloop
import tornado.web
import tornado.httpserver
import os

import db

from tornado.options import options, define
define("port", default="8000", help="run on this port", type=int)


class Application(tornado.web.Application):

    def __init__(self):
        handler = [(r"/", MainHandler),
                   (r"/list", ListHandler),
                   (r"/blog", ArticleHandler),
                   (r"/me", MeHandler),
                   (r"/login", LoginHandler),
                   (r"/book",BookSelectHandler)]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,)
        tornado.web.Application.__init__(self, handler, **settings)


class MainHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render("homepage.html", title="yxc", page_name="YXC")

    def post(self, *args, **kwargs):
        pass


class ListHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render("list.html", title=False, book_name="Not yet", page_name="List")

    def post(self, *args, **kwargs):
        book_name = self.get_argument("book_name")
        book_isbn = self.get_argument("book_isbn")
        book_author = self.get_argument("book_author")
        book_price = self.get_argument("book_price")
        book_info = dict(
            book_name=book_name,
            book_isbn=book_isbn,
            book_author=book_author,
            book_price=book_price
        )
        inner = db.DB(book_info)
        inner.insert()
        self.render("list.html", book_name=book_name, page_name="List")


class BookSelectHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        print db.DB.select()





# class BookModule(tornado.web.UIModule):
#
#     def render(self, book):
#         return self.render_string("module/book.html", book=book)
#
#     def css_files(self):
#         return "/static/css/main/style.css"
#
#     def javascript_files(self):
#         return "/static/js/main.js"


# class BookStore(tornado.web.RequestHandler):
#     def get(self, *args, **kwargs):
#         book_name = self.get_argument("book_name")
#         book_isbn = self.get_argument("book_isbn")
#         book_author = self.get_argument("book_author")
#         book_price = self.get_argument("book_price")
#         book_cover = self.get_argument("book_cover")


class ArticleHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render("book.html", title="blog", page_name="Blog" )

    def post(self, *args, **kwargs):
        pass


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


class MeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("me.html",title="Me", page_name="About Me")

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login", title="Login", page_name="Login")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.httpserver.HTTPServer(Application())
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
