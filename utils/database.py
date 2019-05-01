# encoding: utf-8
import sqlite3

class DBTool(object):
    def __init__(self, db):
        """
        初始化函数，创建数据库连接
        """
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

    def executeUpdate(self, sql, ob):
        """
        数据库的插入、修改函数
        :param sql: 传入的SQL语句
        :param ob: 传入数据
        :return: 返回操作数据库状态
        """
        try:
            self.c.executemany(sql, ob)
            i = self.conn.total_changes
        except Exception as e:
            print('错误类型： ', e)
            return False
        finally:
            self.conn.commit()
        if i > 0:
            return True
        else:
            return False

    def executeDelete(self, sql, ob):
        """
        操作数据库数据删除的函数
        :param sql: 传入的SQL语句
        :param ob: 传入数据
        :return: 返回操作数据库状态
        """
        try:
            self.c.execute(sql, ob)
            i = self.conn.total_changes
        except Exception as e:
            return False
        finally:
            self.conn.commit()
        if i > 0:
            return True
        else:
            return False

    def executeQuery(self, sql, ob =''):
        """
        数据库数据查询
        :param sql: 传入的SQL语句
        :param ob: 传入数据
        :return: 返回操作数据库状态
        """
        test = self.c.execute(sql, ob)
        return test

    def close(self):
        """
        关闭数据库相关连接的函数
        :return:
        """
        self.c.close()
        self.conn.close()