import speech_recognition as sr
import pvporcupine

r = sr.Recognizer()

def mic_recognition_ru():
    with sr.Microphone(device_index=1) as source:
        try:
            print("Я слушаю")
            audio_data = r.listen(source)
            r.adjust_for_ambient_noise(source)
            call = r.recognize_google(audio_data, language="ru-RU")
            call = call.lower()
            print("Распознано:", call)
            return call
        except:
            print("Не раслышала")
            pass

def mic_recognition_en():
    with sr.Microphone(device_index=1) as source:
        try:
            print("Я слушаю")
            audio_data = r.listen(source)
            r.adjust_for_ambient_noise(source)
            call = r.recognize_google(audio_data, language="en")
            call = call.lower()
            print("Распознано:", call)
            return call
        except:
            print("Не раслышала")
            pass