from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "secreto"

def generar_cartas():
    return random.sample(range(1, 100), 21)

def repartir_cartas(cartas):
    return [cartas[i::3] for i in range(3)]

@app.route("/")
def index():
    session["cartas"] = generar_cartas()
    session["ronda"] = 1
    return render_template("index.html", cartas=session["cartas"])

@app.route("/game", methods=["POST"])
def game():
    cartas = session["cartas"]
    session["montones"] = repartir_cartas(cartas)
    return render_template("game.html", montones=session["montones"], ronda=session["ronda"])

@app.route("/next_round", methods=["POST"])
def next_round():
    monton_elegido = int(request.form["monton"])
    montones = session["montones"]

    if monton_elegido == 0:
        nuevas_cartas = montones[1] + montones[0] + montones[2]
    elif monton_elegido == 1:
        nuevas_cartas = montones[0] + montones[1] + montones[2]
    else:
        nuevas_cartas = montones[0] + montones[2] + montones[1]

    session["ronda"] += 1
    session["cartas"] = nuevas_cartas
    explicacion = generar_explicacion(session["ronda"], monton_elegido, nuevas_cartas)

    if session["ronda"] > 3:
        session["cartas_restantes"] = session["cartas"]
        return redirect(url_for("reveal"))

    session["montones"] = repartir_cartas(nuevas_cartas)
    return render_template("game.html", montones=session["montones"], ronda=session["ronda"], explicacion=explicacion)

@app.route("/reveal")
def reveal():
    session["indice_carta"] = 0
    session["contador"] = 1
    return render_template("reveal.html", carta_actual=session["cartas_restantes"][0], contador=session["contador"])

@app.route("/next_card")
def next_card():
    session["indice_carta"] += 1
    session["contador"] += 1
    indice = session["indice_carta"]
    
    if indice >= 10:
        return redirect(url_for("result"))
    
    return render_template("reveal.html", carta_actual=session["cartas_restantes"][indice], contador=session["contador"])

@app.route("/result")
def result():
    carta_final = session["cartas_restantes"][-11]
    return render_template("result.html", carta_final=carta_final)

def generar_explicacion(ronda, monton_elegido, cartas):
    explicacion = f"<h2>Explicación Matemática - Ronda {ronda}</h2>"
    explicacion += f"<p>Seleccionaste el montón {monton_elegido + 1}. "
    explicacion += "La clave del truco está en cómo se reorganizan las cartas.</p>"
    explicacion += "<p>Siempre ponemos el montón elegido en el centro, lo que provoca que "
    explicacion += "la carta que originalmente estaba en la posición central del montón elegido "
    explicacion += "permanezca cerca del centro en la siguiente ronda.</p>"
    explicacion += f"<p>Después de esta reorganización, la carta en la posición central es {cartas[10]}.</p>"
    return explicacion

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
