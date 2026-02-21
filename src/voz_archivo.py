import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import tempfile, os

SRATE = 16000     # tasa de muestreo
DUR = 5           # segundos

def reconocer_voz():
    print("Grabando... habla ahora!")
    audio = sd.rec(int(DUR * SRATE), samplerate=SRATE, channels=1, dtype='int16')
    sd.wait()
    print("Listo, procesando...")

    tmp_wav = tempfile.mktemp(suffix=".wav")
    write(tmp_wav, SRATE, audio)

    r = sr.Recognizer()

    with sr.AudioFile(tmp_wav) as source:
        data = r.record(source)

    try:
        texto = r.recognize_google(data, language="es-ES")
        return texto
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
    finally:
        if os.path.exists(tmp_wav):
            os.remove(tmp_wav)