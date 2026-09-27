class Developer:
    def __init__(self, name, age, language, experience=0):
        self.name = name
        self.age = age
        self.language = language
        self.experience = experience

    def introduce(self):
        return f"Привет! Меня зовут {self.name}, мне {self.age} лет, и я изучаю {self.language}."
    
    def add_experience(self):
        self.experience += 1

    def change_language(self, new_language):
        self.language = new_language

    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Язык программирования: {self.language}, Опыт: {self.experience} лет"

ivan = Developer("Иван", 20, "Python", 0)
anna = Developer("Анна", 22, "Java")
oleg = Developer("Олег", 25, "C++")
print(f"Имя: {ivan.name}")
print(f"Возраст: {ivan.age}")
print(f"Язык программирования: {ivan.language}") 
print(ivan.introduce())
print(anna.introduce())
print(oleg.introduce())
print(f"Опыт до: {ivan.experience}")
ivan.add_experience()
print(f"Опыт после: {ivan.experience}")
print(f"Язык до: {ivan.language}")
ivan.change_language("JavaScript")
print(f"Язык после: {ivan.language}")
print(ivan.get_info())
print(anna.get_info())
print(oleg.get_info())