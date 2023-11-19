string=input("enter a string:")
count=0
for i in range(0,len(string)):
       if(string[i]!=''):
        count=count+1
print("The number of character in a string are:"+str(count))
