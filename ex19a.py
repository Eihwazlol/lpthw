# -*- coding: utf-8 -*-


def addition(numero1, numero2):
    
    #return numero1 + numero2

#print "The first number you want to add ?"
#numero1 = int(raw_input(">"))
#print "The second number you want to add?"
#numero2 = int(raw_input(">"))
    
#resultat = addition(numero1, numero2)
    
#print "The result is : %r" % resultat

    
    print "Le premier nombre est égal à ", int(numero1)
    print "Le second nombre est égal à ", int(numero2)
    resultat = int(numero1) + int(numero2)
    print "Le résultat est : ", resultat
    print "\n"

print "\n"
print "Ce programme effectue une addtion entre le 1er nombre, et le 2ieme."
    
print "En donnant directement les arguments à la fonction :"    
addition(80,7)

print "En utilisant des variables :"
numero1bis = 100
numero2bis = 35
addition(numero1bis, numero2bis)


print "En rajoutant des opérations en interne :"
addition(30 + 25, 15 - 8)


print "En utilisant des variables ET des opérations mathématiques"
numero1ter = 43
numero2ter = 56
addition(numero1ter + 10, numero2ter + 45)

print "En utilisant des raw_input :"
addition(numero1 = raw_input(">"), numero2 = raw_input(">")) 


