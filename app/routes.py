from flask import render_template, request
from app import app

@app.route("/", methods=["GET", "POST"])
def index():
    imc = None
    mensagem = ""
    if request.method == "POST":
        peso_str = request.form.get("peso")
        altura_str = request.form.get("altura")

        if not peso_str or not altura_str:
            mensagem = "Por favor, preencha todos os campos"
        else:
            try:
                peso = float(peso_str)
                altura = float(altura_str)
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
