print("Rectangle")
print(".....")
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
area=lambda l,b:l*b
print("Area:",area(l,b))
perimeter=lambda l,b:2*(l+b)
print("Perimeter:",perimeter(l,b))
print("Square")
print("....")
a=int(input("Enter the side of square:"))
area=lambda a:a*a
print("Area:",area(a))
perimeter=lambda a:4*a
print("Perimeter:",perimeter(a))
