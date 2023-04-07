#物件下的所有方法要self
#.lower()

class Employee:
    def __init__(self, fn, ln):
        self.first = fn
        self.last = ln
        self.fullname = self.first + " " + self.last
        self.email = self.first.lower() + "." + self.last.lower() + "@company.com"
        self.firstname = self.first



emp_1 = Employee("john", "smith")
emp_2 = Employee("mary", "sue")
emp_3 = Employee("antony", "walker")

print(emp_1.fullname)
print(emp_2.email)
print(emp_3.firstname)