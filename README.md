# Juego de Cartas con Flask

Este es un juego de cartas basado en Flask, donde el usuario selecciona montones de cartas en varias rondas y, al final, el sistema "adivina" su carta utilizando un truco matemático.

## 🚀 Características

- Interfaz web con Flask.
- Uso de sesiones para almacenar el progreso del usuario.
- Implementación del truco matemático de las 21 cartas.
- Explicación detallada del proceso en cada ronda.
- Contenedor Docker para fácil despliegue.

## 🛠 Instalación y Uso

### ✅ Requisitos

- Python 3.x
- Flask
- Docker y Docker Compose (opcional para despliegue)

### 📌 Instalación Manual

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta la aplicación:

bash
Copiar
Editar
python app.py
Accede a la aplicación en: http://localhost:5000

🐳 Uso con Docker
Construye la imagen de Docker:

bash
Copiar
Editar
docker build -t flask-cartas .
Ejecuta el contenedor:

bash
Copiar
Editar
docker run -p 5002:5002 flask-cartas
Accede a la aplicación en: http://localhost:5002

⚙️ Uso con Docker Compose
Levanta la aplicación con:

bash
Copiar
Editar
docker-compose up -d
Detén la aplicación con:

bash
Copiar
Editar
docker-compose down
📂 Estructura del Proyecto
bash
Copiar
Editar
/tu-repositorio
│── app.py                  # Código principal de la aplicación Flask
│── templates/              # Archivos HTML para la interfaz
│── static/                 # Archivos estáticos (CSS, JS, imágenes)
│── requirements.txt        # Dependencias del proyecto
│── Dockerfile              # Configuración para construir la imagen Docker
│── docker-compose.yml      # Configuración para despliegue con Docker Compose
│── README.md               # Este archivo
💡 Contribuciones
Si deseas mejorar este proyecto, puedes hacer un fork y enviar un pull request con mejoras.

📌 Autor: [Tu Nombre]
📧 Contacto: [tu-email@example.com]

🚀 ¡Disfruta del juego de cartas con Flask!

go
Copiar
Editar

Este `README.md` sigue un formato limpio, estructurado y visualmente atractivo con emojis para hacerlo más llamativo. Puedes modificarlo según tus necesidades. 🚀





Dijiste:
hazlo todo en md 
ChatGPT dijo:
Aquí tienes el README.md completamente en formato Markdown:

md
Copiar
Editar
# 🃏 Juego de Cartas con Flask

Este es un juego de cartas basado en Flask, donde el usuario selecciona montones de cartas en varias rondas y, al final, el sistema "adivina" su carta utilizando un truco matemático.

## 🚀 Características

- 🌐 Interfaz web con Flask.
- 📌 Uso de sesiones para almacenar el progreso del usuario.
- 🎩 Implementación del truco matemático de las 21 cartas.
- 📖 Explicación detallada del proceso en cada ronda.
- 🐳 Contenedor Docker para fácil despliegue.

---

## 🛠 Instalación y Uso

### ✅ Requisitos

- Python 3.x
- Flask
- Docker y Docker Compose (opcional para despliegue)

### 📌 Instalación Manual

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
Instala las dependencias:


pip install -r requirements.txt
Ejecuta la aplicación:


python app.py
Accede a la aplicación en:
👉 http://localhost:5000

🐳 Uso con Docker
Construye la imagen de Docker:


docker build -t flask-cartas .

Ejecuta el contenedor:


docker run -p 5002:5002 flask-cartas
Accede a la aplicación en:
👉 http://localhost:5002

⚙️ Uso con Docker Compose
Levanta la aplicación con:


docker-compose up -d
Detén la aplicación con:


docker-compose down
📂 Estructura del Proyecto

/tu-repositorio
│── app.py                  # Código principal de la aplicación Flask
│── templates/              # Archivos HTML para la interfaz
│── static/                 # Archivos estáticos (CSS, JS, imágenes)
│── requirements.txt        # Dependencias del proyecto
│── Dockerfile              # Configuración para construir la imagen Docker
│── docker-compose.yml      # Configuración para despliegue con Docker Compose
│── README.md               # Este archivo
💡 Contribuciones
Si deseas mejorar este proyecto, puedes hacer un fork y enviar un pull request con mejoras.

📌 Autor: [Beta-Brayan-GHS]
