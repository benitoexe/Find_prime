num = input("enter a number:  ")
num = int(num)

for i in range(2, num):
    if num% i == 0:
        num = False
        
    else:
        num = True
        
if (num == True):
    print("your number is prime")

else: 
    print("your number isn't prime")
    
    
