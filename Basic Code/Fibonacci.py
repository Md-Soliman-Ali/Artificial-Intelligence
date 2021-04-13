def Fibonacci(n):
   if n <= 1:
       return n
   else:
       return(Fibonacci(n-1) + Fibonacci(n-2))

sum = int(input("Input a Digit For Calculating Fibonacci: \n")) 

if sum <= 0:
   print("Not Input Negative Value !!!")
   
else:
   print("Sequence: ")
   for n in range(sum):
       print(Fibonacci(n))

