from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')
@app.route('/price')
def price():
    check = True
    password_entered = request.args.get('password')
    conn = sqlite3.connect('flask.db')
    cur = conn.cursor()
    cur.execute('''select * from user_table where Password={}'''.format(password_entered))
    data = cur.fetchall()
    if len(data) == 0:
        check = False
        return render_template('login.html', check=check)
    else:
        return render_template('price.html',data=data)

if __name__ == '__main__':
    app.run()
