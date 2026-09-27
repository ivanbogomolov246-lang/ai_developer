class Developer:
    def __init__(self, name, age, language, experience=0):
        self.name = name
        self.age = age
        self.language = language
        self.experience = experience

    def get_info(self):
        return f"{self.name} | {self.age} лет | {self.language} | опыт: {self.experience}"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "language": self.language,
            "experience": self.experience
        }

    