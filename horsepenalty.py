name= input("Enter the name of the horse: ")
numwins = int(input("Enter the number of previous wins: "))
penweight = 0

if numwins == 0:
    penweight = 0
    print(name,", ", penweight)
elif numwins ==1 or numwins== 2:
    penweight = 4
    print(name,", ", penweight)
else: 
    penweight=8
    print(name,", ", penweight)

