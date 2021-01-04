import sqlite3
import ujson
import os
#一个url表 一个域名表 端口表（ip）

#con.execute(query)
# con=sqlite3.connect("tuhu.org.sqlite3")
# a=con.execute("select * from domain;")
# b=a.fetchall()
# for t in b:
#     print(t)
class Ato():
    def __init__(self,domain):
        self.domains=domain
        self.sql=self.__creat_sql()
        self.jsons ="tmp/"+self.domains+".json"
        self.__oneforall(j=self.jsons)

    def __creat_sql(self):
        name=self.domains+".sqlite3"
        con = sqlite3.connect(name)
        query = """CREATE TABLE domain
        (id integer PRIMARY KEY AUTOINCREMENT,
        domains  varchar(30) UNIQUE,
        title varchar(20),
        code  int(5)
        );"""
        try:
            con.execute(query)
        except Exception:
            pass
        con.close()
        return name
    def __oneforall(self,j):
        con = sqlite3.connect(self.sql)
        with open(j) as f:
            data = ujson.load(f)
            for line in data:
                title = line['title']
                title = title.replace('\'', '')
                title = title.replace('\\n', '')
                sql = "insert into domain(domains,title,code) values('%s','%s',%d)" % (line['url'], title, line['status'])
                #         print(sql)
                #         # sql="insert into domain(domains,title,code) values('%s',%s,%d)" %(line['subdomain'],line['title'],line['status'])
                #         # print(sql)
                try:
                    con.execute(sql)
                except Exception:
                    pass
                con.commit()
        con.close()
Ato(domain="tuhu.org")