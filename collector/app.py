import os
import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

db_file = "log_collector.db"
if not os.path.exists(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE posts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 titulo TEXT NOT NULL,
                 conteudo TEXT NOT NULL,
                 autor TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def obter_todos_os_posts():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM posts")
    posts = c.fetchall()
    conn.close()
    return [{'id': post[0], 'titulo': post[1], 'conteudo': post[2], 'autor': post[3]} for post in posts]

def obter_post_por_id(id):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM posts WHERE id=?", (id,))
    post = c.fetchone()
    conn.close()
    if post:
        return {'id': post[0], 'titulo': post[1], 'conteudo': post[2], 'autor': post[3]}
    return None

def criar_novo_post(titulo, conteudo, autor):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("INSERT INTO posts (titulo, conteudo, autor) VALUES (?, ?, ?)", (titulo, conteudo, autor))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    posts = obter_todos_os_posts()
    return render_template('layout.html', posts=posts)

@app.route('/post/<int:id>/')
def post(id):
    post = obter_post_por_id(id)
    return render_template('post.html', post=post)

@app.route('/criar_post', methods=['POST'])
def criar_post():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        autor = request.form['autor']
        criar_novo_post(titulo, conteudo, autor)
        return jsonify({"result": "success"})
    return jsonify({"result": "fail"})

if __name__ == '__main__':
    app.run(debug=True)
