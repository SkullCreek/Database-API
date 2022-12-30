from sqlalchemy import create_engine
import pandas as pd
import urllib
import logging
logging.basicConfig(filename="connection.log",level=logging.DEBUG,format=("%(levelname)s %(level)s %(message)s"))

class PostgreSql:
    def __init__(self,user,host,port,password):
        self.user = user
        self.host = host
        self.port = port
        self.password = password
    def connect(self):
        try:
            self.uri = "postgresql+psycopg2://"+self.user+":" + urllib.parse.quote(self.password) + "@"+self.host+":"+self.port+"/pandas"
            self.engine = create_engine(self.uri)
        except Exception as e:
            logging.CRITICAL(e)
    def insert(self,link,name):
        try:
            self.df = pd.read_csv(link)
            self.df.to_sql(name=name,con=self.engine,if_exists='replace',index=False)
        except Exception as e:
            logging.CRITICAL(e)



class MongoDB:
    pass