# utils/audio_processing.py
import speech_recognition as sr

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='ru-RU')
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
