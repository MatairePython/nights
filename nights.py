miles = int(input("Enter Number Of Miles "))
carsize = input ("Enter size of car ")

if carsize == "small":
    cost = miles * 0.3
elif carsize == "large":
    cost = miles * 0.3
else:
    print("Invalid")
    
    
if cost > 20:
    cost = cost * 0.9

print("Car Size: ", carsize)
print("Miles: ", miles)
print("Cost: ", cost)