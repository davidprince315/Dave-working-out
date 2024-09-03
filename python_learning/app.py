import random
i = random.randint(0,15)
j = 0
while j < 3:
	j= j+1
	g = int(input('guess: '))
	if g < i:
		print("higer")
	elif g > i:
		print("lower")
	elif g == i:
		print("you win")
		break
	print("you lose")
	
		



