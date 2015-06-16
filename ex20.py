# -*- coding: utf-8 -*-

#Importe le module "argv" à partir de la librairie "sys". Permet de lancer un script python en lui donnant des arguments.
from sys import argv

#Ligne qui permet de communiquer à "argv" que l'argument qui lui est passé lors de l'execution du script, sera stocké dans la variable nommée "input_file"
script, input_file = argv

def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print line_count, f.readline()


current_file = open(input_file)


print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"

rewind(current_file)

print "Let's print three line:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
