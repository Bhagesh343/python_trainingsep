class Employee:
    def __init__(self,name,designation,salary)-> None:
        self.name = name
        self.designation = designation
        self.salary = salary

    def __str__(self) -> str:
        return f'{self.name}, {self.designation},{self.salary}'
    
emp1 = Employee('bhagesh','student',1250000)
print(emp1)
print(print(emp1.designation))

