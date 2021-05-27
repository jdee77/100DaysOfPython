# DAY-02 27 MAY 2021
## CONTROL OF FLOW, LOGICAL STATEMENT, RANDOMISATION AND PYTHON LIST 

### CONDITIONAL STATEMENT 
	IF/ ELSE statement
		If condition:
			Do this
		Else: 
			Do this 
#### control water level in a bath tub
	waterlevel = 50
	If waterlevel > 50:
		print (“overflow”)
	Else:
		print (“pour water”)

#### NESTED IF ELESE STATEMENT
		If <condition>:
			If <condition>:
				# do this
			else:
				# do this
		else:
			# do this

#### IF ELSE IF LADDER 
		If <condition 1>:
			# do this
		elif <condition 2>:
			# do this
		elif <condition 3>:
			# do this
		else:
			# do this
      
[Pizza order system Program](https://github.com/jdee77/100DaysOfPython/blob/main/Day-02/codes/pizzaorder.py)

	 
### LOGICAL OPERATOR 
AND 		A AND B >> if both A and B true, A AND B is true
OR		A OR B	>> if either of A, B is true, A OR B is true
NOT		NOT A	>> A is true, NOT a is false and vice versa

[love Calculator](https://github.com/jdee77/100DaysOfPython/blob/main/Day-02/codes/love%20calculator.py)
[Treasure Island](https://github.com/jdee77/100DaysOfPython/blob/main/Day-02/codes/treasureisland.py)
[BMI calculator](https://github.com/jdee77/100DaysOfPython/blob/main/Day-02/codes/bmi.py![rockpaper](https://user-images.githubusercontent.com/79501910/119823278-3c7be080-bf12-11eb-990b-42b386ff4028.png)
![rockpaper](https://user-images.githubusercontent.com/79501910/119823334-4f8eb080-bf12-11eb-9cb8-ac7a5203b2a8.png)
)
### RANDOMISATION AND PYTHON LIST
Create unpredictability in computer program e.g. tetris game, snake game, ludo
	
		Import random
		random.randint()	# random integer
		random.random()	# random floating point number 
			# 0.0000000 – 0.9999999
		Random.choice(data structure) # choose a element from data structure
	
### PYTHON LIST 
List is a python data structure
Data structure >> collection of interrelated and organised data 
		
List_Name = [item1, item2, item3, item4, …]
Eg. Fruits = [“mango”, “banana”, “guava”]	
	
Indexing 
		Fruits[0] =>   	mango	= fruits[-3]
		Fruits[1] =>	banana = fruits[-2]
		Fruits[2] => 	guava  	=  fruits[-1]

   Listname.append(“item”) 	// insertinto the list 
    Listname.extend([“item4”, ”item5”, ”item6”])
		Listname.insert(index, “item”)
		Lsitname.remove(“item”)
		
[list](https://github.com/jdee77/100DaysOfPython/blob/main/Day-02/codes/list.py)

#### FINAL PROJECT
[rock paper scissor game](https://github.com/jdee77/100DaysOfPython/tree/main/Day-02/rockPaperScissor)

