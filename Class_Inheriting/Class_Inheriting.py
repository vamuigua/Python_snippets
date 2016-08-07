#Our main class Triangle
class Triangle(object):
#Initializing main method 
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
#Number_of_sides variable for 3 sides of a Triangle      
    number_of_sides = 3
#Check_angles method if angles equals 180        
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3 == 180:
            return True
        else:
            return False
#creating an instance of our Triangle class.
my_triangle = Triangle(90,30,60)
#Printing the number of sides of the triangle
print my_triangle.number_of_sides
#Checking if angles sum function/method is True or False
print my_triangle.check_angles()

#New class Equilateral that inherits from Triangle Class
class Equilateral(Triangle):
    angle = 60
    def __init__(self):
#The angles are set to one value because an Equilateral Triangle has 3 angles that are equal
        self.angle1=self.angle
        self.angle2=self.angle
        self.angle3=self.angle
        
