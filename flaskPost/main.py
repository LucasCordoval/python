from flask import Flask, request, render_template_string

app = Flask(__name__)

logins = [
    {"usuario": "Lucas", "senha": "12400467"},
    {"usuario": "marcos", "senha": "cotemig2026"},
    {"usuario": "janaina", "senha": "cotemig2026"}
]

def show_the_login_form():
    form_html = '''
    <h2>Login</h2>
    <form method="POST">
        <input type="text" name="usuario" placeholder="Usuário"><br><br>
        <input type="password" name="senha" placeholder="Senha"><br><br>
        <button type="submit">Entrar</button>
    </form>
    '''
    return render_template_string(form_html)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if usuario == "admin" and senha == "123":
        return f"<h1>Bem-vindo, {usuario}!</h1>"

    for registro in logins:
        if registro["usuario"] == usuario and registro["senha"] == senha:
            return f"<h1>Bem-vindo, {usuario}!</h1>"
            
    return "<h1>Usuário ou senha incorretos</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True)

# site de consulta https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping