from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mysqldb import MySQL, MySQLdb
import re



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['USER'] = 'Metrelli'
app.config['PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crudapp'

mysql = MySQL(app)
app.secret_key = "flash message"


@app.route('/login', methods = ['POST', 'GET'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        user = cur.fetchone()
        cur.close()

        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('index'))

        else:
            flash("Incorrect username or password.")

    return render_template('login.html')


@app.route('/logout')
def logout():
    # session.clear()
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(url_for('login'))


def rowcount():
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*) FROM administrators")
    row = cur.fetchall()
    cur.close()

    return row[0][0]


@app.route('/', methods = ['POST', 'GET'])
def index():

    if 'loggedin' in session:

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM administrators ORDER BY id")
        data = cur.fetchall()
        cur.close()
        rows = rowcount()

        cur = mysql.connection.cursor()
        cur.execute("SELECT dept FROM departments")
        departments = cur.fetchall()

        return render_template('index.html', administrators = data, rowcount = rows, username=session['username'], departments = departments)

    else:
        return redirect(url_for('login'))


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':
        flash("Administrator Added Successfuly")

        firstName = request.form['firstName']
        lastName = request.form['lastName']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        department = request.form['department']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO administrators (firstName, lastName, username, email, password, department) VALUES (%s,%s,%s,%s,%s,%s)", (firstName, lastName, username, email, password, department))

        mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods = ['POST', 'GET'])
def update(id):


    if request.method == 'POST':

        flash("Data Updated Successfuly")
        
        id = request.form['id']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        department = request.form['department']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE administrators SET firstName=%s, lastName=%s, username=%s, email=%s, password=%s, department=%s WHERE id=%s", (firstName, lastName, username, email, password, department, id))

        mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods = ['POST', 'GET'])
def delete(id):

    flash("Data Deleted Successfuly")

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM administrators WHERE id = %s", [id])
    mysql.connection.commit()
    return redirect(url_for('index'))





if __name__ == "__main__":
    app.run(debug=True)