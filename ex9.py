# -*- coding: utf-8 -*-

# Here's some new strange stuff, remember type it exactly

# Déclare une variable nommée "days" contenant une chaine de caractères "Mon Tue..."
days = "Mon Tue Wed Thu Fri Sat Sun"

# Déclare une variable nommée "months" contenant une chaine de caractères (mois de l'année à la suite). Un "\n" est inséré entre chaque moi afin d'aller à la ligne à chaque fois.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Affiche à l'écran la chaine de caractères "Here are the day: " (sans les guillemets) suivi du contenu de la variable nommée "days" (elle même une chaine de caractères) à la suite, sans passer de ligne
print "Here are the days: ", days

# Affiche à l'écran la chaine de caractères "Here are the months: " (sans les guillemets), suivi du contenu de la variable nommée "months" (elle même une chaine de caractères). Les "\n"  permettent d'aller à la ligne entre chaque mois. Mais il n'y en a pas avant "Jan", donc "Here are the months: " et "Jan" seront sur la même ligne.
print "Here are the months: ", months

# A priori, l'utilisation de 3 guillemets permet de taper plusieurs lignes, et de passer à la ligne sans fermet et réouvrir les guillemets.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
