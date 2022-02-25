#program to caluclate the area of the triangle

a=float(input("Enter first side of the triangle:"))
b=float(input("Enter the second side of the triangle:"))
c=float(input("Enter the third side of the triangle:"))

#to caluclate the semi-perimeter
s=(a+b+c)/2

#to caluclate the area of the traingle
area=(s*(s-a)*(s-b)*(s-c))**0.5
print( area)