import time
print(time.time())

hogwarts_students = ['harry', 'ron', 'hermione']
#for loops
#for loops in Python have a variable that you temporarily store the value of each element as you iterate through. This one is called student.
for student in hogwarts_students:
    #then print each time.
    print(f"{student.title()}! It's leviOsa, not leviosA!\n")
    #Python uses indentation to indicate when one line of code is connected to the line above it.

#range for loop
for value in range(1,5):
    print(value)
    #this prints 1 through 4 because when it reaches 5 it stops running and never reaches the print. 


#list range function
numbers = list(range(1, 5))
print(numbers)

#skipping numbers
#This function starts with 2, then adds 2 until it reaches 11 and stops.
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for square in squares:
    square =  value**2
    















    
