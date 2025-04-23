class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            return Employee(f"{self.name} & {other.name}", self.salary + other.salary)

    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.salary - other.salary

    def __str__(self):
        return f"Employee(Name: {self.name}, Salary: {self.salary})"
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = emp1 + emp2
print(emp3) 
salary_diff = emp1 - emp2
print(abs(salary_diff))
