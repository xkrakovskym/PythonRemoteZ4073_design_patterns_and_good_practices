class Student:
    def get_full_name(self):
        pass

    def get_contact_details(self):
        pass

    def is_adult(self):
        pass

    def get_results(self):
        pass


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


class FavoriteAdapter(Student, Favorite):
    def __init__(self, first_name, last_name, email, age, grades):
        super().__init__(first_name, last_name, email, age, grades)

    def get_full_name(self):
        return self.get_first_name() + " " + self.get_last_name()

    def get_contact_details(self):
        return self.get_email()

    def is_adult(self):
        return self.get_age() >= 18

    def get_results(self):
        return self.get_grades()
