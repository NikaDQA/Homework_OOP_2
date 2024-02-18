class Employee:

    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def work(self):
        return "I come to the office."

    def __str__(self):
        return f"Employee: {self.name}"

    def __lt__(self, other):
        return self.daily_salary < other.daily_salary

    def __gt__(self, other):
        return self.daily_salary > other.daily_salary

    def __eq__(self, other):
        return self.daily_salary == other.daily_salary



class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return f"Recruiter: {self.name}"


class Developer(Employee):
    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        return f"Developer: {self.name}"

developer1 = Developer("Dima", 400)
recruiter1 = Recruiter("Yulya", 100)

print(developer1)
print(recruiter1)

print(developer1.work())
print(recruiter1.work())

print(developer1 == recruiter1)
print(developer1 < recruiter1)
print(developer1 > recruiter1)
