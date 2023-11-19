num1=int(input ("Enter the first number:"))
num2=int(input ("Enter the second number:"))
operation=input("Choose an arithmetic operation (+,-,*,/,** for exponentiation, // for floor division and % for modulo):")
if operation=="+":
 result=num1+num2
elif operation=="-":
 result=num1-num2
elif operation=="*":
 result=num1*num2
elif operation=="/":
 result=num1/num2
elif operation=="**":
 result=num1**num2
elif operation=="//": 
 result=num1//num2
elif operation=="%":
 result=num1%num2
else:
     print("invalid input")
print("The result of the arithmetic operation is:",result)


