def swap_values(x,y):
    print("Values before swapping X = ",x , "Y = ",y)
    x = x + y
    y = x - y
    x = x - y
    print("Values after swapping X = ",x , "Y = ",y)

x = int(input("Enter the value for X: "))
y = int(input("Enter the value for Y: "))
swap_values(x,y)