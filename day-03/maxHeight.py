student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
max_score = 0
min_score = 999

for score in student_scores:
	if score< min_score:
		min_score = score
	if score> max_score:
		max_score = score 
	
print(f"The highest scsore in the class is :{max_score}")



