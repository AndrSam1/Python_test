class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


class Worker(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

class Manager(Worker):
    salary_rate = 0.3

    def __init__(self, name, salary, number_of_subordinates):
        self.name = name
        self.__salary = salary
        self.number_of_subordinates = number_of_subordinates

    def get_salary(self):
        return self.__salary * self.number_of_subordinates * self.salary_rate

    def set_number_of_subordinates(self, number_of_subordinates):
        self.number_of_subordinates = number_of_subordinates

    def get_number_of_subordinates(self):
        return self.number_of_subordinates


class Director(Manager):
    salary_rate = 0.5

    def __init__(self, name, salary, number_of_subordinates):
        self.name = name
        self.__salary = salary
        self.number_of_subordinates = number_of_subordinates

    def get_salary(self):
        return self.__salary * self.number_of_subordinates * self.salary_rate

# ***************************** Main program *****************************

emp = Employee("Viktor Prohorov", 1200)
print(f'Employee {emp.get_name()} salary ${emp.get_salary()}')

wor = Worker("Sergey Demidov", 1500)
print(f'Worker {wor.get_name()} salary ${wor.get_salary()}')

man = Manager("Ivan Shishkin", 1600, 10)
print(f'Manager {man.get_name()} salary ${man.get_salary()}')

director = Director("Stanislav Kuznetsov", 2100, 100)
print(f'Director {director.get_name()} salary ${director.get_salary()}')
print(f'Director - number of subordinates {director.number_of_subordinates}')
