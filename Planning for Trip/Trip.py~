"""Functions to Calculate Trip Cost"""

#Function for hotel_cost
def hotel_cost(nights):
    return 140 * nights

#Functtion for plane_ride_cost
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

#Function for renting a car
def rental_car_cost(days):
    cost =  days * 40
    if days >= 7:
        return cost - 50
    elif days >= 3: 
        return cost - 20
    return cost    
    
 #Function for Total_Trip_Cost   
def trip_cost(city, days,spending_money):   
    return plane_ride_cost(city) + hotel_cost(days) + rental_car_cost(days) + spending_money

#Printing out the Total_Trip_Cost Function     
print trip_cost("Los Angeles",5,600)    
