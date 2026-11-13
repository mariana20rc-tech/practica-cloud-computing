from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>¡Mi primera aplicación Docker!</h1>
    <p>Aplicación desplegada con Google Cloud.</p>
    <p>Proyecto de Cloud Computing - Tarea 3.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
