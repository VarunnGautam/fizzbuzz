def print100():
	for numb in range(0,101):
		if (numb%3 ==0):
			print ("Fizz")
		elif (numb%5==0):
			print("Buzz")
		elif (numb%3==0 and numb%5==0):
			print("FizzBuzz")
		print (numb)
print100()
