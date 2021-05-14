cars = 100 #number of cars
space_in_a_car = 4.0 #total people can travel in a single car
drivers = 30 #total no. of drivers
passengers = 90 #total passengers to use cars 
cars_not_driven = cars - drivers #cars not driven will be total cars - drivers 
cars_driven = drivers # cars driven will be always equal to number of drivers
carpool_capacity = cars_driven * space_in_a_car #total capacity can be determined by cars driven multiplied by space in each car 
avg_passengers_per_car = passengers / cars_driven 

print("There are", cars, "cars available") 
print("There are only",drivers,"drivers available")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity, "people today")
print("We have", passengers,"to carpool today.")
print("We need to put about", avg_passengers_per_car,"in each car.")


#carpool_capacity is the variable and not car_pool_capacity wrong variable was defined
#1. yes 4 people can sit in a car so how much 30 cars can carry people is determined by it.
#2. 