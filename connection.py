import psycopg2 as pst
import pymongo
from sqlalchemy import create_engine
import pandas as pd
import urllib
import logging
import databaseUri


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
    def __int__(self):
        pass
    def connect(self):
        try:
            self.uri = databaseUri.mongo_uri
            self.client = pymongo.MongoClient(self.uri)
        except Exception as e:
            logging.critical(e)
    def create_db(self,name):
        try:
            self.db = self.client[name]
        except Exception as e:
            logging.warning(e)
    def create_collection(self,col_name):
        try:
            self.col = self.db[col_name]
        except Exception as e:
            logging.warning(e)
    def insert(self,link):
        try:
            self.df = pd.read_csv(link)
            self.data = self.df.to_dict(orient='records')
            self.col.insert_many(self.data)
        except Exception as e:
            logging.warning(e)
    def update(self, select, update):
        try:
            self.col.update_many(select,update)
        except Exception as e:
            logging.warning(e)
    def delete(self, query):
        try:
            self.col.delete_many(query)
        except Exception as e:
            logging.warning(e)
    def select(self,query):
        try:
            self.res = self.col.find(query)
            logging.info(self.res)
            return self.res
        except Exception as e:
            logging.warning(e)