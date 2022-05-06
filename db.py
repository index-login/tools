import sqlite3

import records
import ujson
import os
from urllib import parse

#一个url表 一个域名表 端口表（ip）

# con.execute(query)

class Ato():
    def __init__(self,domain):
        self.domains=domain
        # self.__creat_sql()
        self.jsons =os.getcwd()+"/tmp/"
        # self.__oneforall(j=self.jsons)
        # self.__subfinder(j=self.jsons)
        self.data="sqlite:///tuhu.org.db"
    def __creat_sql(self):
        self.data=self.domains+".sqlite3"
        con = sqlite3.connect(self.data)
        query = """CREATE TABLE domain
        (id integer PRIMARY KEY AUTOINCREMENT,
        domains  varchar(30) UNIQUE,
        title varchar(20),
        code  char(5)
        );"""
        try:
            con.execute(query)
        except Exception:
            pass
        con.close()

    def __oneforall(self,j):
        con = sqlite3.connect(self.data)
        #with open("tuhu.org.json") as f:
        with open(j+self.domains+".json") as f:
            data = ujson.load(f)
            for line in data:
                title = str(line['title'])
                title = title.replace('\'', '')
                title = title.replace('\\n', '')
                sql = "insert into domain(domains,title,code) values('%s','%s','%s')" % (line['url'], title, line['status'])
                #         print(sql)
                #         # sql="insert into domain(domains,title,code) values('%s',%s,%d)" %(line['subdomain'],line['title'],line['status'])
                #         # print(sql)
                try:
                    con.execute(sql)
                except Exception:
                    pass
        con.commit()
        con.close()
    def __subfinder(self,j):
        con = sqlite3.connect(self.data)
        #with open("sub_tuhu.org.json", encoding='UTF-8') as  f:
        with open(j+"sub_"+self.domains+".json",encoding='UTF-8') as  f:
            for t in f:
                data=ujson.loads(t)
                if parse.urlsplit(data['url']).port == 80:
                    data['url']=data['url'][:-3]
                if parse.urlsplit(data['url']).port == 443:
                    data['url']=data['url'][:-4]
                sql = "insert into domain(domains,title,code) values('%s','%s','%s')" % (data['url'], data['title'], data['status-code'])
                try:
                    con.execute(sql)
                except Exception:
                    pass #重复数据
        with open(j + "amass_" + self.domains + ".json", encoding='UTF-8') as ff:
            for t in ff:
                data=ujson.loads(t)
                if parse.urlsplit(data['url']).port == 80:
                    data['url']=data['url'][:-3]
                if parse.urlsplit(data['url']).port == 443:
                    data['url']=data['url'][:-4]
                sql = "insert into domain(domains,title,code) values('%s','%s','%s')" % (data['url'], data['title'], data['status-code'])
                try:
                    con.execute(sql)
                except Exception:
                    pass #重复数据

        con.commit()
        con.close()
    # def __amass(self,j):
    #     con=sqlite3.connect(self.sql)
    #     with open(j+self.domains+".json") as f:
    #         data = ujson.load(f)
    #         for line in data:
    #
    #             sql = "insert into domain(domains,title,code) values('%s','%s',%d)" % (line['url'], title, line['status'])
    #             #         print(sql)
    #             #         # print(sql)
    #             try:
    #                 con.execute(sql)
    #             except Exception:
    #                 pass
    #     con.commit()
    #     con.close()


    def show(self):
        db=records.Database(self.data)
        db=db.get_connection()
        row=db.query("select * from domain")
        temp= str(row.dataset)
        return temp


if __name__ == '__main__':
    a = Ato(domain="tuhu.org")
    a.show()
# con=sqlite3.connect("tuhu.org.db")
# a=con.execute("select * from domain;")
# b=a.fetchall()
# for t in b:
#     print(t)
# with open("sub_tuhu.org.json",encoding='UTF-8') as  f:
#     for t in f:
#         data=ujson.loads(t)
#         print(data['url'])
