year = int(input("What year are you?: "))
sex = input("male or female?: ")
dept = input("What department are you?: ")
if year == 1 and sex == "male": 
    room = 209
elif year == 1 and sex == "female": 
    room = 210
elif year > 1 and (dept == "MT" or dept == "EM"): 
    room = 301
elif year > 1 and (dept == "IT" or dept == "CPE"): 
    room = 302
else: 
    room = 305
print ("Your room is:", room)
