#Created class Employee as main/parent/superclass
class Employee(object):
    """Models real-life employees!"""
#Initializing main method
    def __init__(self, employee_name):
        self.employee_name = employee_name
#Initializing the calculating_wage method
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

#Created class PartTimeEmployee that inherits from Employee class
class PartTimeEmployee(Employee):
#Overriding the calculate_wage method from Employee class
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
#Initializing full_time_wage method
    def full_time_wage(self,hours):
#Using super to call the calculate_wage method in PartTimeEmployee class which was overriden from the Employee class therefore the #calculate_wage in the Employee class is used
        return super(PartTimeEmployee,self).calculate_wage(hours)
#Variable milton holdS the name of the PartTimeEmployee which in ourcase is "Santos"
milton = PartTimeEmployee("Santos")
#The wage is to be printed out at 20.00 per hour
print milton.full_time_wage(10)
#Output is: 200
