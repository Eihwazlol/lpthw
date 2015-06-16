# -*- coding: utf-8 -*-


x = "There are %d types of people." % 10 # Déclaration de la variable nommée "x", contenant une chaine de caractères qui utilise la variable '10'
binary = "binary" # Déclaraction de la variable nommée "binary" contenant la chaine de caractères "binary" (guillemets inclus)
do_not = "don't" # Déclaration de la variable nommée "do_not", contenant la chaine de caractères "dont't" (guillemets inclus)
y = "Those who know %s and those who %s." % (binary, do_not) # Déclaration de la variable nommée "y", contenant une chaine de caractères qui utlise deux variables (binary, et do_not)

# Study Drills 2 : Number 1 and 2. Binary and do-not are two strings put into another string (y)
print x # Affiche à l'écran le contenu de la variable "x"
print y # Affiche à l'écran le contenu de la variable "y"

#Study Drills 2 : Number 3
print "I said: %r." % x # Affiche à l'écran "I said: (contenu de la variable "x")."

# Study Drills 2 : Number 4
print "I also said: '%s'." % y # Affiche à l'écran "I also said: '(Contenu de la variable "y")."


hilarious = True # Déclaration de la variable nommée "hilarious" contenant la valeur booléene "True"
joke_evaluation = "Isn't that joke so funny?! %r" # Déclaration de la variable nommée "joke_evaluation" contenant la chaine de caractères "Isn't that joke so funny?! %r" et qui utilisera une variable qu'il faudra préciser par la suite.


print joke_evaluation % hilarious # Affiche à l'écran le contenu de la variable "joke_evaluation" et utilise la variable variable "hilarious", le %r utilise donc la variable nommée "hilarious".


w = "This is the left side of..." # Déclare la variable nommée "w" contenant la chaine de caractères "This is the left side of..." (guillemets inclus)
e = "a string with a right side." # Déclare la variable nommée "e" contenant la chaine de caractères "a string with a right side." (guillemets inclus)

print w + e # Affiche à l'écran la concaténation de la variable "w" et de la variable "e" qui sont toutes les deux des chaines de caractères. Les deux chaines sont alors mise l'une à la suite de l'autre.
