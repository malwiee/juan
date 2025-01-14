import random

x = int(input("Inserisci un numero: "))
y = random.randint(0, 1000000)
print("Let's go gambling!")

while x != y:
    y = random.randrange(0, 1000000)
    print("Ah dangit!")
    print("Let's go gambling!")


print("I found your number: ")
#prova merge