#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)
app.database = 'sample.db'

@app.route('/')
def index():
    return "Hello World! EngSoft2"


@app.route('/cidades')
def cidades():
    g.db = connect_db()
    cur = g.db.execute('select * from cidades')
    cidades = [dict(title=row[0], description=row[1]) for row in
             cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=cidades)


@app.route('/estados')
def estados():
    g.db = connect_db()
    cur = g.db.execute('select * from estados')
    estados = [dict(title=row[0], description=row[1]) for row in
             cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=estados)

@app.route('/paises')
def paises():
    g.db = connect_db()
    cur = g.db.execute('select * from estados')
    paises = [dict(title=row[0], description=row[1]) for row in
             cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=paises)



def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
