# -*- coding: utf-8 -*-


#Défini la fonction nommée "cheese_and_crackers", avec comme argument les variables nommées "cheese_count", et "boxes_of_crackers"

#Cette fonction affiche à l'écran plusieurs lignes.
# La 1ère ligne affiche "You have X cheeses!"  X étant la valeur de la variable "cheese_count".
# La 2ième ligne est similaire mais avec la valeur de la variable "boxes_of_crackers"
# La 3ième et 4ième ligne sont toujours les mêmes
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


#Affiche à l'écran "We can just give the function numbers directly"
print "We can just give the function numbers directly:"
# Puis, utilise la fonction nommée "cheese_and_crackers" en lui donnant directement les arguments necessaire à son fonctionnement. La fonction a besoin de deux arguments, le 1er sera la valeur de cheese_count, le 2ième sera la valeur de boxes_of_crackers
# Ici, cheese_count sera donc égal à 20, et boxes_of_crackers sera égal à 30.
# Les différentes lignes de la fonction seront donc affichées à l'écran avec les valeurs données ici.
cheese_and_crackers(20, 30)


# Même principe que précedemment, sauf que nous créeons des variables dans lesquelles nous mettons des valeurs.
# Ici, les deux variables sont nommées "amount_of_cheese" et "amount_of_crackers", nous leurs donnons comme valeur respectivement 10 et 50.
# Ces variables sont ensuite utilisées comme arguments lors de l'utilisation de la fonction.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)



print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
