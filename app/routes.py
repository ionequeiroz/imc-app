from flask import render_template, request
from app import app


@app.route("/", methods=["GET", "POST"])
def index():
    imc = None
    mensagem = ""
    if request.method == "POST":
        try:
            peso = float(request.form["peso"])
            altura = float(request.form["altura"])
            if peso <= 0 or altura <= 0:
                mensagem = "Peso e altura devem ser maiores que zero"
            else:
                imc = round(peso / (altura ** 2), 2)
                if imc < 18.5:
                    mensagem = "Abaixo do peso"
                elif 18.5 <= imc < 25:
                    mensagem = "Peso ideal"
                elif 25 <= imc < 30:
                    mensagem = "Sobrepeso"
                else:
                    mensagem = "Obesidade"
        except ValueError:
            mensagem = "Insira valores numéricos válidos para peso e altura"

    return render_template("index.html", imc=imc, mensagem=mensagem)
