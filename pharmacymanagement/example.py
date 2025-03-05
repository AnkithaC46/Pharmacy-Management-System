from flask import Flask, render_template, request, redirect, url_for

# Your existing imports
import mysql.connector
import os

app = Flask(__name__, template_folder=os.getcwd())

# MySQL configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="selection_db"
)
cursor = db.cursor()
@app.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/afterlogin',methods=['GET', 'POST'])
def afterlogin():
    return render_template('afterlogin.html')

@app.route('/employee',methods=['GET', 'POST'])
def employee():
    return render_template('employee.html')


@app.route('/customer',methods=['GET', 'POST'])
def  customer():
    return render_template('customer.html')


@app.route('/presc',methods=['GET', 'POST'])
def presc():
    return render_template('presc.html')


@app.route('/medicine',methods=['GET', 'POST'])
def medicine():
    return render_template('medicine.html')


@app.route('/bill',methods=['GET', 'POST'])
def bill():
    return render_template('bill.html')
import hashlib
@app.route('/login', methods=['GET','POST'])
def register():
    username=request.form.get('username')
    password=request.form.get('password')
    cursor=mysql.connection.cursor()
    #pwd = hashlib.md5(pwd.encode('utf-8')).digest()
    cursor.execute(''' INSERT INTO login(username,password) VALUES(%s,%s)''',(username,password))
    mysql.connection.commit()
    cursor.close()
    return "success"
@app.route('/employee', methods=['GET','POST'])
def emp():
    EMP_ID=request.form.get('employeeid')
    EMP_NAME=request.form.get('employeename')
    EMP_PHNO =request.form.get('employeephone')
    EMP_ROLE=request.form.get('employeerole')
    cursor=mysql.connection.cursor()
    #pwd = hashlib.md5(pwd.encode('utf-8')).digest()
    cursor.execute(''' INSERT INTO employee(EMP_ID,EMP_NAME,EMP_PHNO,EMP_ROLE) VALUES(%s,%s,%s,%s)''',(EMP_ID,EMP_NAME,EMP_PHNO,EMP_ROLE))
    mysql.connection.commit()
    cursor.close()
    return "success"