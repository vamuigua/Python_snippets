#Created class Employee as main/parent/superclass
class Employee(object):
#Main method that is instantiated
    def __init__(self, name):
        self.name = name
#Instantiating method called greet
    def greet(self, other):
        print "Hello, %s" % other.name
#Creating class CEO with argument Employee
class CEO(Employee):
#This method overrides the method in the Employee class
    def greet(self, other):
        print "Get back to work, %s!" % other.name
#Declared variables for the CEO and Employee name
ceo = CEO("Emily")
emp = Employee("Steve")

#Calling the method greet in class Employee
emp.greet(ceo)
#Output is: Hello, Emily

#Calling the method greet in class CEO
ceo.greet(emp)
#Output is: Get back to work, Steve!
