#coding=utf-8
# 导入库
from scrapy.utils.project import get_project_settings
import pymysql
from hqdmzj.items import HqdmzjItem
from hqdmzj.items import ContentItem

# 写入数据库
class HqdmzjPipeline(object):
    def connect_db(self):
        # 从settings.py文件中导入数据库连接需要的相关信息
        settings = get_project_settings()

        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        # 连接数据库
        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.name,  # 数据库名
            charset = self.charset,
        )

        # 操作数据库的对象
        self.cursor = self.conn.cursor()

    # 连接数据库
    def open_spider(self, spider):
        self.connect_db()

    # 关闭数据库连接
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    # 写入数据库
    def process_item(self, item, spider):
        # 写入数据库内容
        # 这里根据需求自行设置要写入的字段及值
        # 保存的字段内容有双引号时前面变量写单引号
        if isinstance(item, HqdmzjItem):
            #sql = "insert into dmzj (time, title,cover,url,author,content) values ('%s','%s','%s','%s','%s','%s')" % (item['time'], item['title'], item['cover'], item['url'], item['author'], item['content'])
            sql = "insert into dmzj (time, title,cover,url,author) values ('%s','%s','%s','%s','%s')" % (item['time'], item['title'], item['cover'], item['url'], item['author'])
            self.cursor.execute(sql)
            self.conn.commit()
            return item
        else:
            sql = "insert into content (url,text) values ('%s','%s')" % (item['url'], item['text'])
            self.cursor.execute(sql)
            self.conn.commit()
            return item