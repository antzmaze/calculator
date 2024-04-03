# Asking the user to enter a number
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
# Caclulating the two chosen numbers by the user
print("addition=", a + b)
print("subtraction=", a - b)
print("multiplication=", a * b)
print("division=", a / b)
# Asking the user if they want to continue
cont = input("Do you want to continue? (y/n):")
# Continue if the user says yes
while cont == "y":
  a = int(input("Enter the value of a:"))
  b = int(input("Enter the value of b:"))

  print("addition=", a + b)
  print("subtraction=", a - b)
  print("multiplication=", a * b)
  print("division=", a / b)
# Discontinuing if the user says no
if cont == "n":

  print("Thank you for using the calculator!")
