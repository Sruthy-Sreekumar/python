def is_palindrome(n):
 n_str=str(n)
 n_rev=n_str[::-1]
 if n_str==n_rev:
  return True
 return False
n=int(input("Enter a number:"))
result=is_palindrome(n)
if result==True:
  print("The number is palindrome")
else:
  print("The number is not a palindrome")
