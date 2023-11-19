num=int(input("Enter a number:"))
def sum(n):
     a=0
     if n<=1:
        return n
     else:
        return n+sum(n-1)
        return a
print("The sum is:",sum(num))
