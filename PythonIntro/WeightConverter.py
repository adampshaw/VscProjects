
weight = float(input("Enter Weight: "))
weight_mesure = input("(K)g or (L)bs: ")

if weight_mesure.upper() == "K":
    converted = weight / 0.45
    print("Weight in lbs is: " + str(converted))
else: 
    converted = weight * 0.45 
    print("Weight in kg is: " + str(converted))

