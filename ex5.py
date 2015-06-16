# -*- coding: utf-8 -*-

#Déclaration des différentes variables
name = 'Geoffrey R. Blanpain'
age = 27 # not a lie
height = 68.504 #inches 
weight = 141.096 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Blonde'

# Transformation des variables en pounds/inches en unités Françaises : Kilogrames et Centimètres, puis mises dans des variables différentes
height_cm = height / 0.3937 #Taille en Cm
weight_kg = weight / 2.2046 # poids en Kg



print "Let's talk about %s." % name #Utilisation de la variable "name" contenant le nom de la personne, de type "string"

# Utilisation de la variable "height", puis à la ligne suivante des variables en unités Françaises
print "He's %d inches talls." % height
print "That means %d Cm." % height_cm

# Utilisation de la variable "weight", puis à la ligne suivante des variables en unités Françaises
print "He's %d pounds heavy." % weight
print "That means %d Kg." % weight_kg

# Suite de l'exercice, rien de spécial dans ces lignes
print "Actually that's not too heavy at all."
print "He's got %s eyes and %s hair, well, at least a few." % (eyes, hair)
print "His teeth are usually %s depending on the coffee, and tea sometimes." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
