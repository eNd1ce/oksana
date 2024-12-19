# utils/media.py
from iioksana.utils.ocr import extract_text_from_image
from iioksana.models.face_recognition import FaceRecognizer
from iioksana.utils.audio_processing import transcribe_audio

face_recognizer = FaceRecognizer()

def process_image(image_path):
    identity = face_recognizer.recognize_face(image_path)
    if identity:
        return f"На изображении обнаружено лицо: {identity}"
    else:
        text = extract_text_from_image(image_path)
        if text:
            return f"Извлеченный текст из изображения: {text}"
        else:
            return "Не удалось распознать лица или текст на изображении."

def process_audio(audio_path):
    transcription = transcribe_audio(audio_path)
    if transcription:
        return f"Расшифровка аудио: {transcription}"
    else:
        return "Не удалось распознать речь на аудио."
