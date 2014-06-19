import random

__author__ = 'seifu'


class Employee:
    """Common base for all employees"""
    empCount = 0

    def __init__(self, name, salary, is_working):
        self.name = name
        self.salary = salary
        self.is_working = is_working
        Employee.empCount += 1

    def __str__(self):
        return "Name: " + self.name + ", Salary: " + str(self.salary) + ", Is Working: " + str(self.is_working)


class Cook(Employee):
    """Common base for all cooks"""
    cookCount = 0

    def __init__(self, name, salary, is_working, specialty):
        Employee.__init__(self, name, salary, is_working)
        self.specialty = specialty
        Cook.cookCount += 1
        Employee.empCount += 1

    def __str__(self):
        return "Name: " + self.name + ", Salary: " + str(self.salary) + ", Is Working: " \
               + str(self.is_working) + ", Specialty: " + self.specialty

    def make_meal(self):
        print(self.name, 'ist making food now')

    def pick_up(self, name):
        n = random.randint(1, 7)
        if n == 1:
            print('Hey', name, 'lookin\' pretty fly')
        elif n == 2:
            print('Hey', name, 'did it hurt... when you fell from heaven?')
        elif n == 3:
            print('Hey', name, 'are your legs tired... because you\'ve been running through my mind all day')
        elif n == 4:
            print('Hey', name, 'how YOU doin\'?')
        elif n == 5:
            print('Hey', name, 'they say dating is a numbers game, so can I get yours?')
        elif n == 6:
            print('Hey', name, 'how would you like to TAB complete me?')
        else:
            print('Hey my buddies bet me I couldn\' start a conversation with the most beautiful girl in the bar. '
                  'Want to have a drink with their money?')

if __name__ == '__main__':
    cook1 = Cook("bob", "salary", False, "specialty")
    print(cook1)
    emp1 = Employee('emp1', 'salary', False)
    print(emp1)
    #emp1.make_meal()
