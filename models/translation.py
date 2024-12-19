# models/translation.py
from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self):
        self.supported_languages = ['en']
        self.tokenizers = {}
        self.models = {}
        for lang in self.supported_languages:
            model_name = f'Helsinki-NLP/opus-mt-{lang}-ru'
            self.tokenizers[lang] = MarianTokenizer.from_pretrained(model_name)
            self.models[lang] = MarianMTModel.from_pretrained(model_name)

        self.ru_tokenizers = {}
        self.ru_models = {}
        for lang in self.supported_languages:
            model_name = f'Helsinki-NLP/opus-mt-ru-{lang}'
            self.ru_tokenizers[lang] = MarianTokenizer.from_pretrained(model_name)
            self.ru_models[lang] = MarianMTModel.from_pretrained(model_name)

    def translate_to_ru(self, text, src_lang):
        if src_lang in self.supported_languages:
            tokenizer = self.tokenizers[src_lang]
            model = self.models[src_lang]
            return self._translate(text, tokenizer, model)
        return text

    def translate(self, text, dest_lang):
        if dest_lang in self.supported_languages:
            tokenizer = self.ru_tokenizers[dest_lang]
            model = self.ru_models[dest_lang]
            return self._translate(text, tokenizer, model)
        return text

    def _translate(self, text, tokenizer, model):
        tokens = tokenizer(text, return_tensors='pt', padding=True)
        translated = model.generate(**tokens)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        return translated_text
