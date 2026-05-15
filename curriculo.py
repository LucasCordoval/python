from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Lucas Cordoval</li>  
                <li><strong>Email:</strong> lucashenriquecordoval@gmail.com</li>
                <li><strong>Telefone:</strong> (31) 99340-2704</li>
            </ul>

            <h2>Experiência</h2>
            <ul>
                <li><strong>Empresa:</strong> Cotemig</li>
                <li><strong>Cargo:</strong> Estudante</li>
                <li><strong>Período:</strong> Jan/2024 - Dez/2026</li>
            </ul>
        </body>
        </html>
        <style>
            body { background-color: black; color: white; text-align: center;}
            ul{list-style-type: none;}
        </style>
    '''

if __name__ == '__main__':
    app.run(debug=True)
