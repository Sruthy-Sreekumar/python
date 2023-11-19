student={}
n=int(input("enter the number of students:"))
for i in range(0,n):
 name=input("enter the name:")
 age=int(input("enter the age:"))
 grade=input("enter the grade:")
 student[name]=[age,grade]
 print("list of students:",student)
