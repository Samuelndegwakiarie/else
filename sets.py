# these are sets

from turtle import update


towns = {"kenol", "muranga", "embu", "kisii", "kenol" }
cities = {"Nairobi", "Kisumu", "Mombasa","Nakuru"}
fruit = {"banana", "tomato", "pineapple", "orange", "grapes", "pineapple"}
a = 6.5
cars={"volvo", "chervloret", "benz"}

#adding item to a set
#nameofset.add("new item")
fruit.add("melon")
cars.add("audi")
print(towns)
print(fruit)
print(cities)
print(cars)
# determine number of items in a set

print(len(towns))
print(len(fruit))

print(len(cars))
#type casting

print(type(towns))
print(type(fruit))
print(type(a))


#merging two sets
towns.update(cities)
print(towns)