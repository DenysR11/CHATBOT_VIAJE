import openai 
from flask import Flask, request, render_template, jsonify, send_file
import pdfkit
import io

openai.api_key = "sk-proj-7LwTHfvvDF6e....." #Por seguridad no colocare la api key 


def interactuar_con_chatgpt(mensaje_usuario):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": """
                    Eres un asistente especializado en planificación de viajes exclusivamente para los destinos: Bacalar, Mahahual, Chetumal, Kohunlich y Xcalak.
                    Para cada destino:
                    1. Responde únicamente con información relevante al lugar mencionado, pero diciendo porque es recomendable ir.
                    2. Incluye un itinerario de 3 días siempre que el usuario no proporcione esa información (actividades, restaurantes, hospedaje).
                    3. Proporciona enlaces de hospedaje para hoteles recomendados usando los sitios de reserva más conocidos como Booking.com, Expedia, o Airbnb.
                    4. No sugieras lugares o actividades fuera de estos destinos.
                    5. Si el destino ingresado no está en la lista, responde: "Actualmente solo tengo información sobre Bacalar, Mahahual, Chetumal, Kohunlich y Xcalak."
                    6. Proporciona los costos aproximados de los hoteles, actividades y restaurantes que mencionas en pesos mexicanos.
                    7. Proporciona enlaces para las actividades sugeridas, desde paginas como booking o agencias de viajes seguras.
                    8.  Pregunta al usuario si ya tiene alguna fecha aproximada de su viaje, si es asi, agrega el como estara el clima en esos dias, si no tiene fecha recomienda una. 
                    Usa saltos de línea y un formato claro y organizado en tus respuestas.
                """},
                {"role": "user", "content": mensaje_usuario}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        respuesta_texto = respuesta.choices[0].message.content

      
        botones_html = """
        <p><b>¿Te gustaría hacer alguna modificación a tu itinerario?</b></p>
        
        <p><b>¿Deseas descargar la información en PDF?</b></p>
        <button onclick="descargarPDF()">Descargar PDF</button>
        """

        if "itinerario" in respuesta_texto.lower() or "día" in respuesta_texto.lower():
            respuesta_html = respuesta_texto.replace("\n", "<br>") + botones_html
        else:
            respuesta_html = respuesta_texto.replace("\n", "<br>")

        return respuesta_html
    except Exception as e:
        return f"Error al obtener respuesta de la API: {e}"


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    mensaje_usuario = request.form["mensaje"]
    respuesta = interactuar_con_chatgpt(mensaje_usuario)
    return jsonify({"respuesta": respuesta})

@app.route("/descargar_pdf", methods=["POST"])
def descargar_pdf():
    contenido = request.form.get("contenido", "")
    if not contenido:
        return "No se proporcionó contenido para el PDF.", 400

    
    contenido_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Planificación de Viaje</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
                padding: 0;
                background-color: #f4f4f4;
            }}
            h1 {{
                text-align: center;
                color: #333;
            }}
            .itinerario {{
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }}
            .itinerario p {{
                font-size: 16px;
                color: #333;
                margin: 5px 0;
            }}
            .itinerario b {{
                font-weight: bold;
                color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <h1>Itinerario Planificado</h1>
        <div class="itinerario">
            {contenido}
        </div>
    </body>
    </html>
    """


    
    try:
        config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Cambia esta ruta según tu sistema
        pdf = pdfkit.from_string(contenido_html, False, configuration=config)
        return send_file(
            io.BytesIO(pdf),
            as_attachment=True,
            download_name="informacion_viaje.pdf",
            mimetype="application/pdf"
        )
    except Exception as e:
        return f"Error al generar PDF: {e}", 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
