__author__ = 'yxc'
#-*- coding: utf-8 -*-

import MySQLdb


class DB(object):

    conn = MySQLdb.connect(user="root", db="blog", passwd="yxc", host="localhost", charset="utf8")
    cursor = conn.cursor()

    def __init__(self, book_info):
        self.book_info = book_info
        print repr(self.book_info.get("book_name"))
        print repr(self.book_info.get("book_name"))
        self.book_values = (self.book_info.get("book_name"),
                            self.book_info.get("book_isbn"),
                            self.book_info.get("book_author"),
                            self.book_info.get("book_price"))

    @staticmethod
    def select(self):
        DB.cursor.execute("select * from bookInfo")
        data = cursor.fetchall()
        print data
        return data

    def insert(self):
        # book_values call 4 variable, name, isbn, author abd price
        try:
            DB.cursor.execute("insert into bookInfo(book_name, book_isbn, book_author, book_price) values(%s, %s, %s, %s) ",
                          self.book_values)
            DB.conn.commit()
        except MySQLdb.Error,e:
            print 'cannot '


if __name__ == "__main__":
    conn = MySQLdb.connect(user="root", db="blog", passwd="yxc", host="localhost")
    cursor = conn.cursor()
    print cursor.execute('select * from authors where name="yxc"')
    data = cursor.fetchall()
    if data:
        for da in data:
            print da[0], da[1], da[2]
