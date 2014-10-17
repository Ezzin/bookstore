__author__ = 'yxc'

import MySQLdb


class DB(object):

    conn = MySQLdb.connect(user="root", db="blog", passwd=yxc, host="localhost")
    cursor = conn.cursor()

    def __init__(self):
        pass

    def select(self, **bookInfo):
        self.bookInfo = bookInfo
        if self.bookInfo.get("book_name") & self.bookInfo.get("book_isbn"):
            if self.bookInfo.get("book_author"):
               bookInfo = [self.bookInfo.get("book_name"), self.bookInfo.get("book_isbn"),\
                           self.bookInfo.get("book_author")]
               self.cursor.execute("insert into bookInfo values %s" % bookInfo)

