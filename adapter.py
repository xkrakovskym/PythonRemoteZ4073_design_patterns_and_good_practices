class Student:  # target "interface"
    def __init__(self, full_name, contact_details, age, grades):
        self.full_name = full_name
        self.contact_details = contact_details
        self.age = age
        self.grades = grades

    def get_full_name(self):
        return self.full_name

    def get_contact_details(self):
        return self.contact_details

    def is_adult(self):
        return self.age >= 18

    def get_results(self):
        return self.grades


class Favorite:
    def __init__(self, first_name, last_name, email, age, grades):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age
        self._grades = grades

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_age(self):
        return self._age

    def get_grades(self):
        return self._grades

    def __str__(self):
        return f"Favorite(first_name={self._first_name}, last_name={self._last_name}, email={self._email}, age={self._age}, grades={self._grades})"


class FavouriteAdapter(Student):
    def __init__(self, favorite):
        full_name = f"{favorite.get_first_name()} {favorite.get_last_name()}"
        contact_details = favorite.get_email()
        age = favorite.get_age()
        grades = favorite.get_grades()
        super().__init__(full_name, contact_details, age, grades)


favourite1 = Favorite("Michal", "K", "m@k.com", 29,[1,4,3,2])

print(favourite1)

student1 = FavouriteAdapter(favourite1)

print(student1.get_full_name())