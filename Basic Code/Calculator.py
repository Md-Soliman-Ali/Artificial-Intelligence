def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print("Please Select Your Operation")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")

select=input("Enter your option Using 1 or 2 or 3 or 4: ")

num1= int(input("Input Your First Number: "))
num2=int(input("Input Your Second Number: "))

if select=="1":
    print("Add Result: ", add(num1,num2))
          
elif select=="2":
    print("Sub Result: ",sub(num1,num2))
    
elif select=="3":
    print("Mul Result: ",mul(num1,num2))
    
elif select=="4":
    print("Div Result: ",div(num1,num2))
    
else:
    print("Invalid Input")