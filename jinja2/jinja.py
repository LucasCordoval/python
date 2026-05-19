from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    nome = "Turma de Python"
    return render_template('base.html', nome=nome)

@app.route("/alunos")
def alunos():
    lista_alunos = [
    {"nome" : "Lucas", "nota": 8},
    {"nome" : "Davi", "nota": 7},
    {"nome" : "Paulo", "nota": 6}
    ]
    return render_template('alunos.html', alunos=lista_alunos)


if __name__ == "__main__":
    app.run(debug=True)

