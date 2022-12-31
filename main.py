import connection as con
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/postgresql/insert',methods=['GET','POST'])
def create_table():
    if(request.method == 'POST'):
        user = request.json['user']
        host = request.json['host']
        port = request.json['port']
        password = request.json['password']
        dbname = request.json['dbname']
        dataset = request.json['dataset']
        dataset_name = request.json['dataset_name']
        postgre_conn = con.PostgreSql(user,host,port,password,dbname)
        postgre_conn.connect()
        postgre_conn.insert(dataset,dataset_name)
        return jsonify("successfully inserted data")

@app.route('/postgresql/update',methods=['GET','POST'])
def update_table():
    if (request.method == 'POST'):
        user = request.json['user']
        host = request.json['host']
        port = request.json['port']
        password = request.json['password']
        dbname = request.json['dbname']
        table_name = request.json['table_name']
        setp = request.json['set']
        condition = request.json['condition']
        postgre_conn = con.PostgreSql(user, host, port, password, dbname)
        postgre_conn.update(table_name,setp,condition)
        return jsonify("successfully updated data")

@app.route('/postgresql/delete',methods=['GET','POST'])
def delete_table():
    if (request.method == 'POST'):
        user = request.json['user']
        host = request.json['host']
        port = request.json['port']
        password = request.json['password']
        dbname = request.json['dbname']
        table_name = request.json['table_name']
        condition = request.json['condition']
        postgre_conn = con.PostgreSql(user, host, port, password, dbname)
        postgre_conn.delete(table_name,condition)
        return jsonify("successfully updated data")

@app.route('/postgresql/select',methods=['GET','POST'])
def select_table():
    if (request.method == 'POST'):
        user = request.json['user']
        host = request.json['host']
        port = request.json['port']
        password = request.json['password']
        dbname = request.json['dbname']
        row = request.json['row']
        table_name = request.json['table_name']
        condition = request.json['condition']
        postgre_conn = con.PostgreSql(user, host, port, password, dbname)
        ans = postgre_conn.select(row,table_name,condition)
        return jsonify(ans)

@app.route('/mongodb/insert',methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        dbname = request.json['dbname']
        colname = request.json['colname']
        link = request.json['link']
        mongo = con.MongoDB()
        mongo.connect()
        mongo.create_db(dbname)
        mongo.create_collection(colname)
        mongo.insert(link)
        return jsonify("successfully inserted the data")

@app.route('/mongodb/update',methods=['GET','POST'])
def update():
    if request.method == 'POST':
        dbname = request.json['dbname']
        colname = request.json['colname']
        select = request.json['select']
        update = request.json['update']
        mongo = con.MongoDB()
        mongo.connect()
        mongo.create_db(dbname)
        mongo.create_collection(colname)
        mongo.update(select,update)
        return jsonify("successfully updated the data")

@app.route('/mongodb/delete',methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        dbname = request.json['dbname']
        colname = request.json['colname']
        query = request.json['query']
        mongo = con.MongoDB()
        mongo.connect()
        mongo.create_db(dbname)
        mongo.create_collection(colname)
        mongo.delete(query)
        return jsonify("successfully deleted the data")

@app.route('/mongodb/select',methods=['GET','POST'])
def select():
    if request.method == 'POST':
        dbname = request.json['dbname']
        colname = request.json['colname']
        query = request.json['query']
        mongo = con.MongoDB()
        mongo.connect()
        mongo.create_db(dbname)
        mongo.create_collection(colname)
        ans = mongo.select(query)
        dist = {"data":list(ans)}
        return jsonify(str(dist))



if __name__ == "__main__":
    app.run()