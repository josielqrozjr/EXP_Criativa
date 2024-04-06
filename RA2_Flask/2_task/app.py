#-----------------
# Criar uma página Web através do Flask que simule uma casa conectada, a qual contenha 2 cômodos. Cada cômodo precisa conter pelo menos um sensor e um atuador. A página precisa conter um menu principal, pelo qual o usuário pode selecionar um dos 2 cômodos. Ao entrar em cada cômodo, o usuário poderá entrar em uma nova tela contendo sensores ou atuadores. Ao clicar em sensores e atuadores, o sistema deve mostrar uma mensagem com o nome do sensor/atuador. É importante a presença da tela retornar.
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
            <title>home</title>
        </head>
        <body>
            <br>
            <h1>my home</h1>
            <hr>
            <ul>
                <li><a href="/room"><button>room</button></a></li>
                <br>
                <li><a href="/bathroom"><button>bathroom</button></a></li>
            <ul>
        </body>
    </html>
"""

@app.route('/room')
def room():
    return """
    <html>
        <head>
            <title>room</title>
        </head>
        <body>
            <br>
            <h1>my room</h1>
            <ul>
                <li><a href="/luminosidade"><button>Sensor de Luminosidade</button></a></li>
                <li><a href="/interruptor"><button>Interruptor</button></a></li>
            </ul>
            <hr>
            <a href="/"><button>Return for my home</button></a>
        </body>
    </html>
"""

@app.route('/interruptor')
def interruptor():
    return """
    <html>
        <head>
            <title>Interruptor</title>
        </head>
        <body>
            <br>
            <h2>interruptor</h2>
            <p>É um dispositivo eletromecânico que converte um sinal elétrico em um movimento linear ou rotativo. Ele é usado para controlar diversos tipos de máquinas e equipamentos, como válvulas, bombas, ventiladores e portas automáticas.</p>
            <hr>
            <a href="/"><button>Return for my home</button></a>
        </body>
    </html>
"""

@app.route('/luminosidade')
def luminosidade():
    return """
    <html>
        <head>
            <title>Sensor de Luminosidade</title>
        </head>
        <body>
            <br>
            <h2>sensor de luminosidade</h2>
            <p>Também chamado de fotocélula, detecta a quantidade de luz presente no ambiente. Sua função principal é converter a luz em um sinal elétrico, que pode ser utilizado para diversos fins.</p>
            <hr>
            <a href="/"><button>Return for my home</button></a>
        </body>
    </html>
"""


@app.route('/bathroom')
def bathroom():
    return """
    <html>
        <head>
            <title>bathroom</title>
        </head>
        <body>
            <br>
            <h1>my bathroom</h1>
            <ul>
                <li><a href="/umidade"><button>Sensor de umidade</button></a></li>
                <li><a href="/umidade"><button>Lâmpada inteligente</button></a></li>
            </ul>
            <hr>
            <a href="/"><button>Return for my home</button></a>
        </body>
    </html>
"""

@app.route('/umidade')
def umidade():
    return """
    <html>
        <head>
            <title>Sensor de umidade</title>
        </head>
        <body>
            <br>
            <h2>sensor de umidade</h2>
            <p>É um dispositivo que mede a quantidade de vapor de água presente no ar ou em outros materiais.</p>
            <hr>
            <a href="/"><button>Return for my home</button></a>
        </body>
    </html>
"""

@app.route('/lampada')
def lampada():
    return """
    <html>
        <head>
            <title>Lâmpada inteligente</title>
        </head>
        <body>
            <br>
            <h2>lâmpada inteligente</h2>
            <p>É um dispositivo que automatiza o controle de lâmpadas tradicionais, transformando-as em lâmpadas inteligentes. Geralmente através de um aplicativo ou assistente virtual.</p>
            <hr>
            <a href="/"><button>Return for my home</button></a>
        </body>
    </html>
"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
