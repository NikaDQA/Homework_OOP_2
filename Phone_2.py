class Employee:

    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def work(self):
        return "I come to the office."

    def __str__(self):
        return f"Employee: {self.name}"


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return f"Developer: {self.name}"


class Developer(Employee):
    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        return f"Recruiter: {self.name}"

