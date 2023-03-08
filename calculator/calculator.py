#calculator
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def dev(n1,n2):
  return n1/n2


#dictonary
operation={


  "+":add,
  "-":sub,
  "*":mul,
  "/":dev
}


num1=int(input("enter number1:\n"))


for i in operation:
  print(i)



opr=input("enter the operator:")
num2=int(input("enter number2:\n"))




cal_function=operation[opr]
answer=cal_function(num1,num2)

print(f"{num1} {opr} {num2} = {answer}")








