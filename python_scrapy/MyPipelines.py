from scrapy.exceptions import DropItem
import json
import pymysql

# 调整改为存入数据库
class MyPipeline(object):
    def __init__(self):
        # # 打开文件
        # self.file = open('data.json', 'w', encoding='utf-8')
        # 创建连接
        self.conn = pymysql.connect(host='192.168.0.145', port=3306, user='admin', password='admin123', db='gaoyu_test', charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()
        print("创建数据库连接")


    # 该方法用于处理数据
    def process_item(self, item, spider):
        # # 读取item中的数据
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # # 写入文件
        # self.file.write(line)
        sql = "insert into imooc_courses(title,url,image_url,introduction,student,image_path) values(%s,%s,%s,%s,%s,%s)"
        param = (item['title'], item['url'], item['image_url'], item['introduction'], item['student'], item['image_path'])
        n = self.cursor.execute(sql, param)
        self.conn.commit()
        print("插入%s行" % n)
        # 返回item
        return item

    # 该方法在spider被开启时被调用
    def open_spider(self, spider):
        print("spider开启")
        pass

    # 该方法在spider被关闭时被调用
    def close_spider(self, spider):
        print("spider关闭")
        # 关闭游标和数据库
        self.cursor.close()
        self.conn.close()
        pass
