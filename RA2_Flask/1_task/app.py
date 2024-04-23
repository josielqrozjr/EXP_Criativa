#-----------------
# Criar o método HTML para retornar a página com a lista de atuadores, como observado no exemplo com sensores. A tela deverá ser acessada via /actuators e deve conter características da tela abaixo.
#-----------------

# app.py
from flask import Flask

app= Flask(__name__)
## __name__ is the application name

@app.route('/')
@app.route('/index')
def index():
    return """
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <br>
            <h1>Página incial</h1>
            <hr>
            <p><a href="/sensors">Clique aqui para voltar a sua casa!</a></p>
        </body>
    </html>
"""


@app.route('/sensors')
def sensors():
    return """
    <html>
        <head>
            <title>Minha Casa</title>
        </head>
        <body>
            <br>
            <h1>Sensores</h1>
            <ul>
                <li>Sensor de Umidade</li>
                <li>Sensor de Temperatura</li>
                <li>Sensor de Luminosidade</li>
            </ul>
            <hr>
            <p><a href="/">Clique aqui para voltar a página inicial!</a></p>
        </body>
    </html>
"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
