from datetime import datetime
import webbrowser
import urllib.parse

def saludar(texto):
    print("¡Hola! bienvenido al sistema de comandos por voz.")

def mostrar_hora(texto):
    print("Hora actual:", datetime.now().strftime("%H:%M"))

def abrir_google(texto):
    webbrowser.open("https://www.google.com")

def buscar_youtube(texto):
    consulta = texto.replace("busca en youtube", "").strip()

    if consulta:
        url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(consulta)}"
        webbrowser.open(url)
    else:
        print("No se entendió qué buscar en YouTube.")

commands = {
    "hola": saludar,
    "hora": mostrar_hora,
    "abrir google": abrir_google,
    "busca en youtube": buscar_youtube,
}