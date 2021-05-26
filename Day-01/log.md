# DAY 1:  WORKING WITH THE VARIABLES & PYTHON DATA TYPE
## PRINTING 
	Print (“Hello world!”) 	# print () function, to print something in console
“string datatypes” are close inside doble quote

Error: EOL while scanning the string literal 
Python interpreter reaches to the end of line while scanning a string 

## STRING MANIPULATION
print (“hello \n world”)
o/p->
hello 
world
	print (“hello” + “world”)		#concantenation of string 
		o/p
		helloworld
	
	print (“##”)
	  print (“##”)	// indentation error: unexpected indent
	  ^ 
## INPUT FUNCTION
	input (“What is your name?”) 	# input (prompt for the user) takes input from the user .
	print (“hello ” + input (“What’s your name:”))
		o/p
		What’s your name: Jagdish
		Hello Jagadish

## COMMENT 
	# this is a comment 
	Comments are the codes which are ignored by the interpreted 
	Written for documentation. 

## STRING LENGTH
	len (“string”)	# len (string_name) returns the length of a string 
	print (len(input(“Enter your name ?”)))
		o/p->
		Enter yout name Jagadish
		8
## PYTHON VARIABLES 
	Name = “hello”
	Print(name) #print hello
	Length = len (name) # 5

	Rules for naming a variable
		Readable	//snake case
			user_name 
			len1
			3len 
			User 234%

## PRIMITIVE DATA TYPES
	#string 
	“Hello”[0]	#H
	“Hello”[1]	#e
		^ index
	Subscripting 
	
	# FLOAT
		3.13324
	# BOOLEAN
		True, False 
	
## TYPE CONVERSION
	Length = Len(“hello”)
	Length_string = str(length) //integer converted into string
	
## MATHEMATICAL OPERATIONS IN PYTHON 
	Addition 	3+5
	Subtraction	5-3
	Multiplication	1*25
	division		6/3	# returns a floating-point number  
	exponent	2**3	# 2 * 2 * 2 = 8
	PEMDAS > () 	** 	* 	/ 	+ 	-



## BMI CALCULATOR
print("BODY MASS INDEX CALCULATOR.")
height = float(input("Enter your height in meter :"))

weight = float(input("Enter your weight in Kilo gram :"))

bmi = round(weight/ (height * height), 3)

print("Your body mass index is :", bmi)


##	F-STRING
		Print(“your score is ”  , score)
		Print(f”your score is {score}”)

# TIP CLACULATOR 
  print("TIP CALCULATOR.")
  total = int(input("What is the total amount : $"))

  tip = int(input("What percentage of bill you want to give : 12, 15, 20 ?"))

  count = int(input("How friends are there :"))

  tip_val = total * tip / 100

  tip_final = round(tip_val / count, 2)

  print(f"The tip amount is $ {tip_final}")






	
	
