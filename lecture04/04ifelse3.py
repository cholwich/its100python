x = input("How old are you?: ")
y = input("How old is the person to your left?: ")

if x.isnumeric() and y.isnumeric():
    print("Your combined age is", int(x)+int(y))
else:
    print("Cannot calculate your combined age.")
    print("Your responses must be numeric.")
