# -*- coding: utf-8 -*-

#Importe le module "argv" à partir de la librairie "sys". Permet de lancer un script python en lui donnant des arguments.
from sys import argv


# Ligne qui permet de communiquer à "argv" que l'argument qui lui est passé sera stocké dans la variable nommée "filename"
script, filename = argv


# Création de la variable nommée "txt" à laquelle nous attribuons la fonction open, avec comme argument la variable "filename". La variable "txt" ouvre donc le fichier qu'on lui donne en argument à l'ouverture du script.l
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "I will now close the file %r:" % filename


print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
print "I will now close the file %r:" % file_again


