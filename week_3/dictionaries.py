laptop ={"make":"hp", "colour":"silver", "weight":"1.5kg", "year of manufacture":"2023"}

for key, value in laptop.items():
    print(key)
    print("\n")
    print(value)

#To print specs:
    print(laptop["make"]) 

# changing a value in the dictionary:
laptop["colour"] = "blue" 
print(laptop) 


# Deleting an item in the dictionary:
del laptop["colour"]
print(laptop)

#ASSGNMENT
# Describe your fav car

fav_car = {"make":"Volkswagen",
           "model":"Golf",
           "vehicle_type":"Front wheel drive",
           "engine_type":"Turbocharged and intercooled DOHC 16-valve inline-4,direct fuel injection",
           "displacement":"2000CC",
           "power":"147 hp",
           "torque":"184 1b-ft",
           "transmission":"8-speed manual shifting mode",
           "tires":"16 inch black alloy rims"}

for key, value in fav_car.items():
    print(key)
    print("\n")
    print(value)




        


