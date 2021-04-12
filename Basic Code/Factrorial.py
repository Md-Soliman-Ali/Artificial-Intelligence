def fact(num):
    if num == 1:
        return 1;
    else:
        return num*fact(num-1);
    
num = int(input('Input A Number: '))

if num < 0:
    print("Fact Does Not Exist !!!")
    
elif num == 0:  
   print("The Fact Of 0 Will Be 1")  
   
else:  
   print("The Fact Of ",num," Is ",fact(num))

