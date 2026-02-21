from datetime import datetime
import webbrowser
import urllib.parse

from voz_archivo import reconocer_voz

def saludar():
    print("¡Hola! bienvenido al sistema de comandos por voz.")

def mostrar_hora():
    print("Hora actual:", datetime.now().strftime("%H:%M"))

def abrir_google():
    webbrowser.open("https://www.google.com")

def buscar_youtube(texto):
    consulta = texto.replace("busca en youtube", "").strip()

    if consulta:
        url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(consulta)}"
        webbrowser.open(url)
    else:
        print("No entendí qué buscar en YouTube.")

def salir():
    print("Hasta luego, gracias por usar nuestro sistema de comandos por voz.")
    exit()

commands = {
    "hola": saludar,
    "hora": mostrar_hora,
    "abrir google": abrir_google,
    "busca en youtube": buscar_youtube,
    "salir": salir
}