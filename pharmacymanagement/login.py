# Flask imports
from flask import Flask, render_template, request, redirect, url_for, jsonify

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
# Define a route to display the login form
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/logins',methods=['POST'])
def logins():
    if request.method == 'POST':
        # Extract data from the form
        username = request.form['username']
        password = request.form['password']
       
        try:
            # Insert data into the database
            insert_query = "INSERT INTO login (username, password) VALUES (%s, %s)"
            cursor.execute(insert_query, (username, password))
            db.commit()
        except Exception as e:
            return f'Error: {str(e)}'
        
        # Redirect to the afterlogin route upon successful login
        return redirect(url_for('afterlogin'))

# Define a route to display the employee form
@app.route('/employee',methods=['GET','POST'])
def employee():
    return render_template('employee.html')

@app.route('/employees',methods=['POST'])
def employees():
    if request.method == 'POST':
        # Extract data from the form
        emp_id = request.form.get('emp_id')
        emp_name = request.form.get('emp_name')
        emp_phno = request.form.get('emp_phno')
        emp_role = request.form.get('emp_role')
        
        try:
            # Insert data into the database
            insert_querys = "INSERT INTO employee (emp_id,emp_name,emp_phno,emp_role) VALUES (%s, %s, %s, %s)"
            data=(emp_id,emp_name,emp_phno,emp_role)
            cursor.execute(insert_querys,data)
            db.commit()

            # Redirect to the employee list page after successful submission
            return redirect(url_for('employee_list'))
        
        except Exception as e:
            return f'Error: {str(e)}'

# Define a route to display the employee list and handle updates

@app.route('/employee/list', methods=['GET', 'POST'])
def employee_list():          
    # Fetch all employees from the database
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    return render_template('employee_list.html', employees=employees)

# Define a route for the afterlogin page
@app.route('/afterlogin')
def afterlogin():
    return render_template('afterlogin.html')

@app.route('/update_employee', methods=['POST'])
def update_employee():
    if request.method == 'POST':
        data = request.json
        emp_id = data['emp_id']
        emp_name = data['emp_name']
        emp_phno = data['emp_phno']
        emp_role = data['emp_role']
        try:
            update_query = "UPDATE employee SET emp_name=%s, emp_phno=%s, emp_role=%s WHERE emp_id=%s"
            data = (emp_name, emp_phno, emp_role, emp_id)
            cursor.execute(update_query, data)
            db.commit()
            return 'Employee updated successfully'
        except Exception as e:
            return f'Error: {str(e)}'

@app.route('/delete_employee', methods=['POST'])
def delete_employee():
    if request.method == 'POST':
        emp_id = request.json['emp_id']
        try:
            delete_query = "DELETE FROM employee WHERE emp_id = %s"
            cursor.execute(delete_query, (emp_id,))
            db.commit()
            return 'Employee deleted successfully'
        except Exception as e:
            return f'Error: {str(e)}'
        
@app.route('/customer',methods=['GET','POST'])
def customer():
    return render_template('customer.html')

@app.route('/customers',methods=['POST'])
def customers():
    if request.method == 'POST':
        # Extract data from the form
        cust_id = request.form.get('cust_id')
        cust_name = request.form.get('cust_name')
        age = request.form.get('age')
        cust_phno = request.form.get('cust_phno')
        address = request.form.get('address')
        bill_no = request.form.get('bill_no')
        emp_id = request.form.get('emp_id')
        
        try:
            # Insert data into the database
            insert_queryss = "INSERT INTO customer(cust_id,cust_name,age,cust_phno,address,bill_no,emp_id) VALUES (%s, %s, %s, %s,%s,%s,%s)"
            data=(cust_id,cust_name,age,cust_phno,address,bill_no,emp_id)
            cursor.execute(insert_queryss,data)
            db.commit()

            # Redirect to the employee list page after successful submission
            return redirect(url_for('customer_list'))
        
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/customer/list', methods=['GET', 'POST'])
def customer_list():          
    # Fetch all employees from the database
    cursor.execute("SELECT * FROM customer")
    customers = cursor.fetchall()
    return render_template('customer_list.html', customers=customers)
@app.route('/update_customer', methods=['POST'])
def update_customer():
    if request.method == 'POST':
        data = request.json
        cust_id = data['cust_id']
        cust_name = data['cust_name']
        age = data['age']
        cust_phno = data['cust_phno']
        address= data['address']
        bill_no = data['bill_no']
        emp_id = data['emp_id']
        try:
            update_query = "UPDATE customer SET cust_name=%s,age=%s,cust_phno=%s,address=%s,bill_no=%s,emp_id=%s WHERE cust_id=%s"
            data=(cust_name,age,cust_phno,address,bill_no,emp_id,cust_id)
            cursor.execute(update_query, data)
            db.commit()
            return 'customer updated successfully'
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    if request.method == 'POST':
        cust_id = request.json['cust_id']
        try:
            delete_query = "DELETE FROM customer WHERE cust_id = %s"
            cursor.execute(delete_query, (cust_id,))
            db.commit()
            return 'customer deleted successfully'
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/medicine',methods=['GET','POST'])
def medicine():
    return render_template('medicine.html')
@app.route('/medicines',methods=['POST'])
def medicines():
    if request.method == 'POST':
        # Extract data from the form
        drug_name = request.form.get('drug_name')
        price = request.form.get('price')
        stock_qty = request.form.get('stock_qty')
        expire_date = request.form.get('expire_date')
        emp_id = request.form.get('emp_id')
        
        try:
            # Insert data into the database
            insert_querys = "INSERT INTO medicine (drug_name,price,stock_qty,expire_date,emp_id) VALUES (%s, %s, %s, %s,%s)"
            data=(drug_name,price,stock_qty,expire_date,emp_id)
            cursor.execute(insert_querys,data)
            db.commit()

            # Redirect to the employee list page after successful submission
            return redirect(url_for('medicine_list'))
        
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/medicine/list', methods=['GET', 'POST'])
def medicine_list():          
    # Fetch all employees from the database
    cursor.execute("SELECT * FROM medicine")
    medicines = cursor.fetchall()
    return render_template('medicine_list.html', medicines=medicines)
@app.route('/update_medicine', methods=['POST'])
def update_medicine():
    if request.method == 'POST':
        data = request.json
        drug_name = data['drug_name']
        price = data['price']
        stock_qty = data['stock_qty']
        expire_date = data['expire_date']
        emp_id= data['emp_id']
        try:
            update_query = "UPDATE medicine SET price=%s,stock_qty=%s,expire_date=%s,emp_id=%s WHERE drug_name=%s"
            data=(price,stock_qty,expire_date,emp_id,drug_name)
            cursor.execute(update_query, data)
            db.commit()
            return 'customer updated successfully'
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/delete_medicine', methods=['POST'])
def delete_medicine():
    if request.method == 'POST':
        drug_name = request.json['drug_name']
        try:
            delete_query = "DELETE FROM medicine WHERE drug_name = %s"
            cursor.execute(delete_query, (drug_name,))
            db.commit()
            return 'customer deleted successfully'
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/prescription',methods=['GET','POST'])
def prescription():
    return render_template('presc.html')
@app.route('/prescriptions',methods=['POST'])
def prescriptions():
    if request.method == 'POST':
        # Extract data from the form
        presdrug_name = request.form.get('presdrug_name')
        pres_date = request.form.get('pres_date')
        pres_qty = request.form.get('pres_qty')
        cust_id = request.form.get('cust_id')
        emp_id = request.form.get('emp_id')
        pres_id = request.form.get('pres_id')
        
        try:
            # Insert data into the database
            insert_querys = "INSERT INTO prescription (presdrug_name,pres_date,pres_qty,cust_id,emp_id,pres_id) VALUES (%s, %s, %s, %s,%s,%s)"
            data=(presdrug_name,pres_date,pres_qty,cust_id,emp_id,pres_id)
            cursor.execute(insert_querys,data)
            db.commit()

            # Redirect to the employee list page after successful submission
            return redirect(url_for('prescription_list'))
        
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/prescription/list', methods=['GET', 'POST'])
def prescription_list():          
    # Fetch all employees from the database
    cursor.execute("SELECT * FROM prescription")
    prescriptions = cursor.fetchall()
    return render_template('prescription_list.html', prescriptions=prescriptions)
@app.route('/update_prescription', methods=['POST'])
def update_prescription():
    if request.method == 'POST':
        data = request.json
        presdrug_name = data['presdrug_name']
        pres_date = data['pres_date']
        pres_qty = data['pres_qty']
        cust_id = data['cust_id']
        emp_id= data['emp_id']
        pres_id= data['pres_id']
        try:
            update_query = "UPDATE prescription SET pres_date=%s,pres_qty=%s,cust_id=%s,emp_id=%s ,pres_id=%s WHERE presdrug_name=%s"
            data=(pres_date,pres_qty,cust_id,emp_id,pres_id,presdrug_name)
            cursor.execute(update_query, data)
            db.commit()
            return 'prescription updated successfully'
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/delete_prescription', methods=['POST'])
def delete_prescription():
    if request.method == 'POST':
        presdrug_name = request.json['presdrug_name']
        try:
            delete_query = "DELETE FROM prescription WHERE presdrug_name = %s"
            cursor.execute(delete_query, (presdrug_name,))
            db.commit()
            return 'prescription deleted successfully'
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/bill',methods=['GET','POST'])
def bill():
    return render_template('bill.html')
@app.route('/bills',methods=['POST'])
def bills():
    if request.method == 'POST':
        # Extract data from the form
        bill_no = request.form.get('bill_no')
        cust_name = request.form.get('cust_name')
        cust_id = request.form.get('cust_id')
        dateandtime = request.form.get('dateandtime')
        totalmedicine_qty = request.form.get('totalmedicine_qty')
        totalamount = request.form.get('totalamount')
        payment_status = request.form.get('payment_status')
        emp_id = request.form.get('emp_id')
        
        try:
            # Insert data into the database
            insert_querys = "INSERT INTO bill (bill_no,cust_name,cust_id,dateandtime,totalmedicine_qty,totalamount,payment_status,emp_id) VALUES (%s, %s, %s, %s,%s,%s,%s,%s)"
            data=(bill_no,cust_name,cust_id,dateandtime,totalmedicine_qty,totalamount,payment_status,emp_id)
            cursor.execute(insert_querys,data)
            db.commit()

            # Redirect to the employee list page after successful submission
            return redirect(url_for('bill_list'))
        
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/bill/list', methods=['GET', 'POST'])
def bill_list():          
    # Fetch all employees from the database
    cursor.execute("SELECT * FROM bill")
    bills = cursor.fetchall()
    return render_template('bill_list.html', bills=bills)
@app.route('/update_bill', methods=['POST'])
def update_bill():
    if request.method == 'POST':
        data = request.json
        bill_no = data['bill_no']
        cust_name= data['cust_name']
        cust_id= data['cust_id']
        dateandtime = data['dateandtime']
        totalmedicine_qty= data['totalmedicine_qty']
        totalamount= data['totalamount']
        payment_status= data['payment_status']
        emp_id= data['emp_id']
        try:
            update_query = "UPDATE bill SET cust_name=%s,cust_id=%s,dateandtime=%s,totalmedicine_qty=%s,totalamount=%s,payment_status=%s,emp_id=%s WHERE bill_no=%s"
            data=(cust_name,cust_id,dateandtime,totalmedicine_qty,totalamount,payment_status,emp_id,bill_no)
            cursor.execute(update_query, data)
            db.commit()
            return 'prescription updated successfully'
        except Exception as e:
            return f'Error: {str(e)}'
@app.route('/delete_bill', methods=['POST'])
def delete_bill():
    if request.method == 'POST':
        bill_no= request.json['bill_no']
        try:
            delete_query = "DELETE FROM bill WHERE bill_no = %s"
            cursor.execute(delete_query, (bill_no,))
            db.commit()
            return 'prescription deleted successfully'
        except Exception as e:
            return f'Error: {str(e)}'
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
