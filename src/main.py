from voz_archivo import reconocer_voz
from comandos import commands


def ejecutar_comando(texto):
    cmd = texto.lower()

    for keyword, action in commands.items():
        if keyword in cmd:
            action()
            return

    print("Comando no reconocido.")


def main():
    texto = reconocer_voz()

    if texto:
        print("Dijiste:", texto)
        ejecutar_comando(texto)
    else:
        print("No se pudo reconocer el audio.")


if __name__ == "__main__":
    main()