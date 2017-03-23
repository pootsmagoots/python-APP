#Returns the sum of num1 and num2
def add(num1, num2):
	return num1 + num2
#Returns the divided sum of num1 and num2
def div(num1, num2):
	return num1 / num2
#Returns the multiplied sum of num1 and num2
def mul(num1, num2):
	return num1 * num2
#Returns the subtracted sum of num1 and num2
def sub(num1, num2):
	return num1 - num2




def Main(Math):  #Remember +, -, /, %, <, >, * can be used. Also "Return" returns the sum
	print(Math)
	Operation = input("what do you want to do? (+,-,*,/):")
	if(Operation != "+" and Operation != "-" and Operation != "*" and Operation != "/"):
		print("you must enter a valid Operation")		#invalid operation
	else:
		Var1 = int(input("Enter num1: "))
		Var2 = int(input("Enter num2: "))
	if(Operation == "+"):
		print(add(Var1, Var2))
	elif(Operation == "/"):
		print(div(Var1, Var2))
	elif(Operation == "*"):
		print(mul(Var1, Var2))
	else:
		print(sub(Var1, Var2))

Main("Let's do some Mathz!!!")
Main("Not what you were after? Try again!")
Main("Last try, i'm tired of giving you more chances")
