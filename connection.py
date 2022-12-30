import psycopg2 as pst
from sqlalchemy import create_engine
import pandas as pd
import urllib
import logging


class PostgreSql:
    logging.basicConfig(filename="connection.log", level=logging.DEBUG)
    def __init__(self,user,host,port,password,dbname):
        self.user = user
        self.host = host
        self.port = port
        self.password = password
        self.dbname = dbname
    def connect(self):
        try:
            self.uri = "postgresql+psycopg2://"+self.user+":" + urllib.parse.quote(self.password) + "@"+self.host+":"+self.port+"/"+self.dbname+""
            self.engine = create_engine(self.uri)
        except Exception as e:
            logging.critical(e)
    def insert(self,link,name):
        try:
            self.df = pd.read_csv(link)
            self.df.to_sql(name=name,con=self.engine,if_exists='replace',index=False)
        except Exception as e:
            logging.error(e)
    def update(self,table_name,set,condition):
        try:
            self.con = pst.connect(database=self.dbname,user=self.user,host=self.host,port=self.port,password=self.password)
            self.cur = self.con.cursor()
            self.query = "UPDATE "+table_name+" SET "+set+" WHERE "+ condition
            logging.info(self.query)
            self.cur.execute(self.query)
            self.con.commit()
        except Exception as e:
            logging.warning(e)
        finally:
            if(self.con):
                self.cur.close()
                self.con.close()

    def delete(self,table_name,condition):
        try:
            self.con = pst.connect(database=self.dbname,user=self.user,host=self.host,port=self.port,password=self.password)
            self.cur = self.con.cursor()
            self.query = "DELETE FROM "+table_name+" WHERE "+condition
            self.cur.execute(self.query)
            self.con.commit()
        except Exception as e:
            logging.warning(e)
        finally:
            if(self.con):
                self.cur.close()
                self.con.close()

    def select(self, row, table_name, condition):
        try:
            self.con = pst.connect(database=self.dbname,user=self.user,host=self.host,port=self.port,password=self.password)
            self.cur = self.con.cursor()
            self.query = "SELECT "+row+" FROM "+table_name+" WHERE "+condition
            self.cur.execute(self.query)
            self.con.commit()
            return self.cur.fetchall()
        except Exception as e:
            logging.warning(e)
        finally:
            if(self.con):
                self.cur.close()
                self.con.close()



class MongoDB:
    pass