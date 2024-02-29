from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Vini v1.0 - System Check"