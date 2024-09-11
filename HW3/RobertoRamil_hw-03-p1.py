name = input("Please enter your name: ")
print(f"Hello {name}!")

x, y = input("Please enter 2 numbers, x and y: ").split()
x = int(x)
y = int(y)
sum = x+y
dif = x-y
product = x*y
raito = x/y

print(f"You entered {x:3.2f} and {y:3.2f}")
print(f"{x:3.2f} + {y:3.2f} = {sum:3.2f}")
print(f"{x:3.2f} - {y:3.2f} = {dif:3.2f}")
print(f"{x:3.2f} * {y:3.2f} = {product:3.2f}")
print(f"{x:3.2f} / {y:3.2f} = {raito:3.2f}")