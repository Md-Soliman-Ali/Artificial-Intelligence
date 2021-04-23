def fact(num):
    if num == 1:
        return 1;
    else:
        return num*fact(num-1);
    
num = int(input('Enter a number for calculating factorial: '))

if num < 0:
    print("Factorial Does Not Exist For The Number",num," !!!")
    
elif num == 0:  
   print("The Factorial Of 0 is 1")  
   
else:  
   print("The Factorial Of ",num," Is ",fact(num))