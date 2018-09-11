#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)
app.database = 'sample.db'


@app.route('/')
def index():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in
             cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=posts)


def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
