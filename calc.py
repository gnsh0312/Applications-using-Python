print("***********************************")
print("*          Simple Calculator      *")
print("***********************************")
print("Enter any of the following code for funtions to be performed")
print("A-Addition")
print("D-Division")
print("M-Multiplication")
print("S-subtraction")
print("P-power")
#defining a function called math
def math():
#taking code for function as input from user
 code=input()
#asking the user to enter the numbers for perfoming math function
 print("Enter the numbers")
 #taking the numbers as input
 num1=int(input())
 num2=int(input())
 #performing the math function based on the code given by the user
 if code == "A":
  a=num1+num2
  print(a)
 elif code == "D":
  b=num1/num2
  print(b)
 elif code == "M":
  c=num1*num2
  print(c)
 elif code == "S":
  d=num1-num2
  print(d)
 elif code== "P":
  print("First number raised to the power of Second number is:")
  e=pow(num1,num2)
  print(e)
#if the entered code of math operation doesn't match
#asking the user to enter a valid code
 else:
  print("Enter a valid code")
#calling the function math
math()