for y in range(5):
    for x in range(8):
        if (x+y) % 2 == 0:
            print("x", end=" ")
        else:
            print("O", end=" ")
    print()
