# -*- coding: utf-8 -*-

#Déclare la variable "cars" et y assigne la valeur "100"
cars = 100

#Déclare la variable "space_in_a_car" et y assigne la valeur "4.0"
space_in_a_car = 4.0

#Déclare la variable "drivers" et y assigne la valeur "30"
drivers = 30

#Déclare la variable "passengers" et y assigne la valeur "90"
passengers = 90

#Déclare la variable car_not_driven et y assigne le résultat de : la valeur de la variable "cars" moins la valeur de la variable "drivers", soit ici cars_not_driven = 100 - 30 = 70
cars_not_driven = cars - drivers

#Déclare la variable "cars_driven" et y assigne la valeur de la variable "drivers". Si la valeur de "drivers" change, alors la valeur de "cars_driven" aussi.
cars_driven = drivers

#Déclare la variable "carpool_capacity" et y assigne le résultat de : la valeur de la variable "cars_driven" fois la valeur de la variable "space_in_a_car". Tout en sachant que la variable "cars_driven" est égale à la valeur de la variable "drivers"
#Soit : 30 * 4.0 = 120.0 (Le résultat est affiche avec une décimale nulle car la valeur de la variable "space_in_a_car" possède une décimale nulle.
carpool_capacity = cars_driven * space_in_a_car


#Déclaire la variable "average_passengers_per_car" et y assigne le résultat de : la valeur de la variable "passengers" divisé par la valeur de la variable "cars_driven". Tout en en sachant que la variable "cars_driven est égale à la valeur de la variable "drivers"
#Soit : average_passengers_per_car = 90 divisé par 30 = 3
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers,"drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport", carpool_capacity,"people today."
print "We have", passengers,"to carpool today."
print "We need to put about", average_passengers_per_car,"in each car."



#ex 4 Study Drills
# Traceback (most recent call last):
#  File "ex4.py", line 8, in <module>
#  average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

#>Cette erreur nous indique que la variable "car_pool_capacity" utilisé à la ligne 8 du code de cet exemple est inconnue. Probablement car non déclarée en début de code. (ligne 3 à 10 sur mon code)
#Le code ne peut donc pas effectuer le cacul car l'une des variables n'est pas connue, donc erreur.

#

