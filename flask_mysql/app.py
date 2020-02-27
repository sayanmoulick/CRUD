import datetime
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'new_schema'

mysql = MySQL(app)


@app.route('/flask/mysql/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        userEmail = details['userEmail']
        userPassword = details['userPassword']
        createdOn = datetime.datetime.now()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO ADMIN_USER(first_name, last_name, email, password, created) VALUES (%s, %s, %s, %s, %s)", (firstName, lastName, userEmail, userPassword, createdOn))
        mysql.connection.commit()
        cur.close()
        return {'message':'success', 'status':200}
    return {'message':'method not allowed', 'status':500}

@app.route('/flask/mysql/read', methods=['GET', 'POST'])
def read():
    if request.method == "POST":
        details = request.form
        userEmail = details['userEmail']
        cur = mysql.connection.cursor()
        cur.execute("SELECT first_name, last_name, email, password FROM ADMIN_USER WHERE email=%s", [userEmail])
        data = cur.fetchone()
        # mysql.connection.commit()
        cur.close()
        if data == None:
            return {'message':'Userid not exists', 'status':404}
        else:
            return jsonify(data)
    return {'message':'method not allowed', 'status':500}

@app.route('/flask/mysql/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        userEmail = details['userEmail']
        userPassword = details['userPassword']
        cur = mysql.connection.cursor()
        cur.execute("SELECT first_name, last_name, email, password FROM ADMIN_USER WHERE email=%s", [userEmail])
        data = cur.fetchone()
        cur.close()
        if data == None:
            return {'message':'Userid not exists', 'status':404}
        else:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE ADMIN_USER set first_name=%s, last_name=%s, password=%s WHERE email=%s", [firstName, lastName, userPassword, userEmail])
            mysql.connection.commit()
            cur.close()
            return {'message':'success', 'status':200}
    return {'message':'method not allowed', 'status':500}

@app.route('/flask/mysql/delete', methods=['GET', 'POST'])
def delete():
    if request.method == "POST":
        details = request.form
        userEmail = details['userEmail']
        cur = mysql.connection.cursor()
        cur.execute("SELECT first_name, last_name, email, password FROM ADMIN_USER WHERE email=%s", [userEmail])
        data = cur.fetchone()
        cur.close()
        if data == None:
            return {'message':'Userid not exists', 'status':404}
        else:
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM ADMIN_USER WHERE email=%s", [userEmail])
            mysql.connection.commit()
            cur.close()
            return {'message':'success', 'status':200}
    return {'message':'method not allowed', 'status':500}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
