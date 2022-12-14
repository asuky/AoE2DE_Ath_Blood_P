import sys
import yaml

class I18n:
    def __init__(self, file_name: str = "ja_JP.yaml"):
        with open(f"i18n/{file_name}", "r") as file_stream:
            self.locale_file = yaml.safe_load(file_stream)
        self.set_locale("ja_JP")

    def set_locale(self, locale: str):
        self.locale = locale

    def _(self, word: str):
        return self.locale_file[self.locale][word]

sys.modules[__name__] = I18n()