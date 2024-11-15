from datetime import datetime


class PERSONA:
    def __init__(self, surname, birth_date):
        self.surname = surname
        self.birth_date = birth_date

    def age(self):
        today = datetime.now()
        birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    def display_info(self):
        print(f"Фамилия: {self.surname}, Дата рождения: {self.birth_date}, Возраст: {self.age()}")


class ABITURIENT(PERSONA):
    def __init__(self, surname, birth_date, faculty):
        super().__init__(surname, birth_date)
        self.faculty = faculty

    def display_info(self):
        super().display_info()
        print(f"Факультет: {self.faculty}")


class STUDENT(ABITURIENT):
    def __init__(self, surname, birth_date, faculty, course):
        super().__init__(surname, birth_date, faculty)
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Курс: {self.course}")


class PREPODAVATEL(PERSONA):
    def __init__(self, surname, birth_date, faculty, position, experience):
        super().__init__(surname, birth_date)
        self.faculty = faculty
        self.position = position
        self.experience = experience

    def display_info(self):
        super().display_info()
        print(f"Факультет: {self.faculty}, Должность: {self.position}, Стаж: {self.experience} лет")


def main():
    people = [
        ABITURIENT("Иванов", "2000-05-15", "Математика"),
        STUDENT("Петров", "1999-10-20", "Физика", 3),
        PREPODAVATEL("Сидоров", "1985-03-30", "Химия", "Доцент", 10)
    ]

    for person in people:
        person.display_info()
        print("-----")

    age_min = 18
    age_max = 25
    print(f"Персоны в возрасте от {age_min} до {age_max}:")
    found = False 
    for person in people:
        if age_min <= person.age() <= age_max:
            person.display_info()
            print("-----")
            found = True

    if not found:
        print("Нет персон в указанном диапазоне возраста.")


if __name__ == "__main__":
    main()
