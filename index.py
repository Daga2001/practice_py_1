#print("Hello world!")
#print("Susan!")
#print("David")

# 1. Write a Python program to check if a given positive integer is a power of two. Go to the editor
# Input : 4
# Output : True

# name: p2
# Purpose: function which checks if a given positive integer is a power of two
# proofs:
# p2(4) --> true
# p2(7) --> false

def p2(num):
    var = 0

    while(var <= num):
        if (2**var == num):
            return True
        var += 1

    return False

print(p2(4))
print(p2(7))

numero = 0

while(numero <= 10):
    print(numero)
    numero += 1

number = 0

while(number < 3):
    print("Hola!")
    number += 1

# numero += 1
# numero = numero + 1
