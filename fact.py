def fact(n):
 if n==1:
   return n
 else:
   return n*fact(n-1)
number=int(input("user input:"))
result=fact(number)
print("factorial of", number,"is",fact(number))
