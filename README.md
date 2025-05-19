# 🌍 Buscador de Atractivos Turísticos

Este es un proyecto desarrollado con **Flask** que permite a los usuarios buscar **atractivos turísticos** según el **destino** que indiquen. La aplicación consulta una base de datos en formato JSON y devuelve una lista de lugares recomendados para visitar en la ciudad o país seleccionado.

## 🧭 ¿Cómo funciona?

1. El usuario ingresa el nombre de un destino (por ejemplo: *Chile*, *Estados Unidos*, *Argentina*).
2. La aplicación busca los principales atractivos turísticos relacionados.
3. Se muestra una lista con los nombres, descripciones, y en algunos casos imágenes o enlaces útiles de cada lugar.

> Ideal para viajeros, bloggers o agencias de turismo que deseen integrar un buscador rápido y eficiente en sus plataformas.

## 🖼️ Vista previa

![Pagina alojada en Render, puede tardar varios minutos en cargar](https://flask-project-akosenko.onrender.com)

## 🚀 Tecnologías utilizadas

- Python 3
- Flask
- HTML/CSS (Jinja2)

## 🛠️ Instalación y ejecución

```bash
# Clona el repositorio
git clone https://github.com/tuusuario/buscador-turistico.git
cd buscador-turistico

# Crea y activa un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
python app.py
