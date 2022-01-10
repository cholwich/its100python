import math as m

a, b, c = input("Input a,b,c: ").split()
if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = float(a), float(b), float(c)
    if b**2-4*a*c < 0:
        print("There is not real-number solutions.")
    elif a == 0:
        print("This is not a quadratic equation.")
    else:
        s = m.sqrt(b**2 - 4*a*c)
        x1, x2 = (-b + s)/(2*a), (-b - s)/(2*a)
        print("Solution = %.2f %.2f" % (x1, x2))
else:
    print("Error: non-numeric coefficients")
