# -*- coding: utf-8 -*-

#Importation du module "argv" de la librairie sys
from sys import argv

# Utilisation du module argv, qui demandera qu'un argument soit donné dés l'application du script. Cet argument sera la variable nommée "user_name"
# Script est une variable
script, user_name = argv

# Déclaration de la variable nommée "prompt" qui sera utilisée avant les "raw input", afin d'indiquer plus clairement aux personnes utilsant le script que l'on attends une réponse de leur part
prompt = '>> '

# Affiche à l'écran 
print "Hi %s, I'm the %s script." % (user_name, script)


print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)


print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
