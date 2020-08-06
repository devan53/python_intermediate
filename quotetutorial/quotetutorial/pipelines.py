# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector


class QuotetutorialPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='dev12345',
            database='quotes'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS Quotes_tb""")
        self.curr.execute("""create table Quotes_tb(
                            title text,
                            author text,                
                            tags text
                            )""")

    def store_db(self, item):
        self.curr.execute("""insert into Quotes_tb values (%s,%s,%s)""", (
            item['title'],
            item['author'],
            item['tags']
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
