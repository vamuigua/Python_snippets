"""This is a Program that Gets the Exam Statistics Including:Grades, Sum-of-Grades, Grade-Average, Grades-Variance, Grades-Standard-Deviation""""

#List holding Grades
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#Function for printing Grades
def print_grades(grades):
    for grade in grades:
        print grade

#Function for printing Grades-Total
def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total

#Function for printing Average-of-Grades   
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

#Function for printing Grades-Variance
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + ((average - score) ** 2)
    return variance / len(scores)

#Function for printing Grade-Standard-Deviiation    
def grades_std_deviation(variance):
    return variance ** 0.5
    
variance = grades_variance(grades)
grades_std_deviation(variance)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)
