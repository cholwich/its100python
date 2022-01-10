n = input("Input n: ")
if n.isnumeric():
    n = int(n)
    for i in range(1, n+1):
        print("* "*i)
else:
    print("Invalid input")
