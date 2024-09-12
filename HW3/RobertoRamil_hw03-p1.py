name = input("Please enter your name: ")
print(f"Hello {name}!")

x, y = input("Please enter 2 numbers, x and y: ").split()
x = int(x)
y = int(y)
sum = x+y
dif = x-y
product = x*y
raito = x/y

print(f"You entered {x:8.2f} and {y:8.2f}")
print(f"{x:8.2f} + {y:8.2f} = {sum:8.2f}")
print(f"{x:8.2f} - {y:8.2f} = {dif:8.2f}")
print(f"{x:8.2f} * {y:8.2f} = {product:8.2f}")
print(f"{x:8.2f} / {y:8.2f} = {raito:8.2f}")