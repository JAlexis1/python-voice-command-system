from datetime import datetime
import webbrowser
import urllib.parse
import os
import platform

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

def abrir_aplicacion_sistema(texto: str):
    sistema = platform.system()

    apps = {
        "calculadora": {
            "Windows": "calc",
            "Darwin": "open -a Calculator",
            "Linux": "gnome-calculator || kcalc"
        },
        "bloc de notas": {
            "Windows": "notepad",
            "Darwin": "open -a TextEdit",
            "Linux": "gedit || mousepad || xed || gnome-text-editor"
        },
        "terminal": {
            "Windows": "start cmd",
            "Darwin": "open -a Terminal",
            "Linux": "gnome-terminal || xterm || konsole || terminal"
        }
    }

    for app, os_systems in apps.items():
        if app in texto:
            command = os_systems.get(sistema)

            if command:
                print(f"Detectado {sistema}. Abriendo la aplicación del sistema...")
                os.system(os_systems[sistema])

                return

    print("Aplicación no soportada en este sistema operativo.")

def precio_dolar(texto):
    url = "https://www.dolar-colombia.com/"
    webbrowser.open(url)

commands = {
    "hola": saludar,
    "hora": mostrar_hora,
    "abrir google": abrir_google,
    "busca en youtube": buscar_youtube,
    "abrir": abrir_aplicacion_sistema,
    "precio dólar": precio_dolar,
}