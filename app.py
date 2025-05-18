from flask import Flask, render_template, request
import json

app = Flask(__name__)	


@app.route('/')
def portada():
    return render_template("portada.html")

@app.route('/inicio')
def inicio():
    return render_template("inicio.html") 

@app.route('/resultados', methods=['POST'])
def resultados():
    ubicacion_usuario = request.form['busqueda']

    # Si el campo está vacío, mostrar todos los resultados
    if not ubicacion_usuario:
        with open('templates/lugares_naturales.json', encoding='utf-8') as f:
            data = json.load(f)
            lugares = data["lugares_naturales_impresionantes"]
        return render_template('listas.html', lugares=lugares, ubicacion="Todos los lugares")
    
    # Asegúrate de que la ruta al archivo JSON sea correcta
    with open('templates/lugares_naturales.json', encoding='utf-8') as f:
        data = json.load(f)
        lugares = data["lugares_naturales_impresionantes"]

    # Filtrar lugares por coincidencia en la ubicación
    resultados_filtrados = [
        lugar for lugar in lugares
        if ubicacion_usuario in lugar["ubicación"]
    ]

    return render_template('listas.html', lugares=resultados_filtrados, ubicacion=ubicacion_usuario)


@app.route('/detalles/<lugar_nombre>')
def detalles(lugar_nombre):
    with open('templates/lugares_naturales.json', encoding='utf-8') as f:
        data = json.load(f)
        # Buscar el lugar en la lista de lugares
        lugar = next((lugar for lugar in data["lugares_naturales_impresionantes"] if lugar["nombre"].lower() == lugar_nombre.lower()), None)
    
    if lugar:
        return render_template('detalles.html', lugar=lugar)
    else:
        return "Lugar no encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)

app.run("0.0.0.0",5000,debug=True)