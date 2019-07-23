# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2


class DemoPipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect(host="localhost", database="postgis", user="postgres", password="1234")
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        sql = "insert into k_movie(title, name) values (%s, %s)"
        self.cursor.execute(sql, (item["title"], item["name"]))
        self.connection.commit()
        return item
