user_weight = int(input("Weight: "))
pounds_or_kilos =  input("(K)g or (L)bs? ")
if pounds_or_kilos.upper() == "K":
    print("Wegiht in Pounds is", user_weight*2.222)
elif pounds_or_kilos.upper() == "L":
    print("Weight in kilograms is: ", user_weight*0.45)
