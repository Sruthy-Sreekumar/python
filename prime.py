lower = int(input ("Enter the lower limit: "))  
upper = int(input (" Enter the upper limit : "))  
print ("The prime numbers between",lower,"and",upper,"are: ")  
for number in range (lower, upper + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
