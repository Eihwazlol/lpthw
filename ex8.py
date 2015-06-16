# -*- coding: utf-8 -*-

# Déclare la variable nommée "formatter" contenant quatres variable de type "raw" indéfinies pour le moment.
formatter = "%r %r %r %r"

# Affiche à l'écran le contenu de la variable nommée "formatter" à laquelle on passe comme argument les chiffres 1, 2, 3 et 4. Ces chiffres sont donc affichés à la suite lors de l'éxécution du programme.
print formatter % (1, 2, 3, 4)

# Affiche à l'écran le contenu de la variable nommée "formatter", à laquelle on passe comme argument les mots/chaines de caractères "one", "two", "three" et "four". On voit donc à l'écran les mots qui s'affichent l'un à la suite des autres, entourés de guillemets.
print formatter % ("one", "two", "three", "four")

# Affiche à l'écran le contenu de la variable nommée "formatter", à laquelle on passe comme argument les valeurs booléennes True False False et True. Mais le type de variable étant "Raw", les arguments sont affichés tel quel, c'est à dire comme des "mots". On voit donc à l'écran les mots qui s'affichent à la suite des autres, True False False True, sans guillemets.
print formatter % (True, False, False, True)

# Affiche à l'écran le contenu de la variable nommée "formatter", à laquelle on passe comme argument lui même, 4 fois. Le contenu de la variable "formatter" étant "%r %r %r %r", on voit s'afficher à l'écran "%r %r %r %r" quatres fois de suites, avec des guillemets.
print formatter % (formatter, formatter, formatter, formatter)

# Affiche à l'écran le contenu de la variable nommée "formatter", à laquelle on passe comme argument 4 phrases entourées de guillemets. On voit donc s'afficher à l'écran ces quatres phrases à la suite, entourées de guillemets.
# 3 Phrases sont affichés avec des guillets simple, l'autre phrase elle, est affichée avec des guillemets double, car elle contient elle même une apostrophe (ligne 23, "didn't")
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
)
