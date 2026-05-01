class ConsentScreen:
    def __init__(self, language):
        self.language = language

    def get_text(self):
        if self.language == "uz":
            return "Mening ma'lumotlarimni qabul qilish"
        elif self.language == "ru":
            return "Принятие моих данных"
        elif self.language == "en":
            return "Accept my data"
        else:
            return "Unknown language"

class ConsentScreenText:
    def __init__(self, language):
        self.language = language
        self.consent_screen = ConsentScreen(language)

    def get_consent_screen_text(self):
        return f"Consent screen text for {self.language}: {self.consent_screen.get_text()}"

# Test the code
uzbek_text = ConsentScreenText("uz")
print(uzbek_text.get_consent_screen_text())

russian_text = ConsentScreenText("ru")
print(russian_text.get_consent_screen_text())

english_text = ConsentScreenText("en")
print(english_text.get_consent_screen_text())
