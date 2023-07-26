from flask import Flask, render_template

app = Flask(__name__)

# Dados dos posts (substitua com os seus próprios)
posts = [
    {
        'id': 1,
        'titulo': 'Meu primeiro post',
        'conteudo': 'Este é o conteúdo do meu primeiro post.',
        'autor': 'Eu mesmo'
    },
    {
        'id': 2,
        'titulo': 'Outro post',
        'conteudo': 'Conteúdo do segundo post.',
        'autor': 'Eu mesmo'
    }
]

@app.route('/')
def index():
    return render_template('layout.html', posts=posts)

@app.route('/post/<int:id>/')
def post(id):
    post = None
    for p in posts:
        if p['id'] == id:
            post = p
            break
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
