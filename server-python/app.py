# Copyright 2024 Google LLC
#
# Licenciado bajo la Licencia Apache, Versión 2.0 (la "Licencia");
# No puedes utilizar este archivo excepto en conformidad con la Licencia.
# Puedes obtener una copia de la Licencia en:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# A menos que lo exija la ley aplicable o se acuerde por escrito,
# el software distribuido bajo esta licencia se distribuye "TAL CUAL",
# SIN GARANTÍAS NI CONDICIONES DE NINGÚN TIPO, ya sean expresas o implícitas.
# Consulta la Licencia para más detalles.
from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde un archivo .env ubicado en el mismo directorio.
load_dotenv()

# Inicializar la aplicación Flask para crear y gestionar el servidor web.
app = Flask(__name__)

# Aplicar CORS para permitir solicitudes desde cualquier dominio.
# Esto es especialmente útil en desarrollo y pruebas.
CORS(app)

# ADVERTENCIA: No compartas código con tu clave API expuesta.
# Configurar la clave API de Google Generative AI obtenida desde
# la variable de entorno. Esta clave autentica las solicitudes a la API de Gemini.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Inicializar el modelo generativo con el nombre de modelo especificado.
# Este modelo se usará para procesar las entradas del usuario y generar respuestas.
modelo = genai.GenerativeModel(model_name="gemini-1.5-flash")

@app.route('/chat', methods=['POST'])
def chat():
    """Procesa la entrada del usuario y devuelve respuestas generadas por IA.

    Esta función maneja solicitudes POST al endpoint '/chat'.
    Espera un JSON con un mensaje del usuario y un historial de conversación opcional.
    Devuelve la respuesta generada por IA como un objeto JSON.

    Args:
        Ninguno (usa el objeto `request` de Flask para acceder a los datos POST)

    Returns:
        Un objeto JSON con la clave "text" que contiene la respuesta generada.
    """
    # Extraer los datos JSON de la solicitud.
    datos = request.json
    mensaje = datos.get('chat', '')
    historial = datos.get('history', [])

    # Iniciar una sesión de chat con el historial proporcionado.
    sesion_chat = modelo.start_chat(history=historial)

    # Enviar la última entrada del usuario al modelo y obtener la respuesta.
    respuesta = sesion_chat.send_message(mensaje)

    return {"text": respuesta.text}

@app.route("/stream", methods=["POST"])
def stream():
    """Transmite respuestas de IA en tiempo real para interacciones de chat.

    Esta función inicia una sesión de transmisión con el modelo Gemini AI,
    enviando continuamente entradas del usuario y transmitiendo respuestas en tiempo real.
    Maneja solicitudes POST al endpoint '/stream' con un JSON similar al de '/chat'.

    Args:
        Ninguno (usa el objeto `request` de Flask para acceder a los datos POST)

    Returns:
        Un objeto `Response` de Flask que transmite respuestas generadas por IA.
    """
    def generar():
        datos = request.json
        mensaje = datos.get('chat', '')
        historial = datos.get('history', [])

        sesion_chat = modelo.start_chat(history=historial)
        respuesta = sesion_chat.send_message(mensaje, stream=True)

        for fragmento in respuesta:
            yield f"{fragmento.text}"

    return Response(stream_with_context(generar()), mimetype="text/event-stream")

# Configurar el servidor para ejecutarse en el puerto 9000.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 9000)))
