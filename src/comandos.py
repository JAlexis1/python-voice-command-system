from datetime import datetime
import webbrowser

def saludar():
    print("¡Hola! bienvenido al sistema de comandos por voz.")

def mostrar_hora():
    print("Hora actual:", datetime.now().strftime("%H:%M"))

def abrir_google():
    webbrowser.open("https://www.google.com")

def salir():
    print("Hasta luego, gracias por usar nuestro sistema de comandos por voz.")
    exit()

commands = {
    "hola": saludar,
    "hora": mostrar_hora,
    "abrir google": abrir_google,
    "salir": salir
}