year = int(input("What year are you?: "))
if year == 1:
    sex = input("male or female? ")
    if sex == "male":
        room = 209
    else:
        room = 210
else:
    dept = input("What department are you?: ")
    if dept == "MT" or dept == "EM":
        room = 301
    elif dept == "IT" or dept == "CPE":
        room = 302
    else: 
        room = 305
print ("Your room is:", room)
