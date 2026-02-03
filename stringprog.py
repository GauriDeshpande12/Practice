#string formatting in python

name = "Gauri"
print(f"Hello,{name}")

name = "Apexon"
print(f"Welcome,{name}")

name = "Gauri"

greeting = "Hello , {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Gauri")

print(with_name)
print(with_name_two)



