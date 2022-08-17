from flaskr import app
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import sqlite3
DATABASE = 'database.db'


@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_materials = con.execute('SELECT * FROM materials').fetchall()
    # db_materials -> [(data1, data2, data3),
    #                  (data1, data2, data3),...]
    con.close()

    materials = []
    for row in db_materials:
        materials.append({'name': row[0], 'inventory': row[1], 'price': row[2]})
    return render_template(
        'index.html',
        materials=materials
    )


@app.route('/form')
def form():
    return render_template(
        'form.html'
    )


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    inventory = request.form['inventory']
    price = request.form['price']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO materials VALUES(?, ?, ?)',
                [name, inventory, price])
    con.commit()
    con.close()
    return redirect(url_for('index'))
