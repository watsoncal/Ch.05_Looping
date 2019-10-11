  #Sign your name: Cal Watson

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0
for i in range(3):
    x = int(input("Enter a number: "))
    total+=x
print("The total is:",total)

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101,2):
    print(i)

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i=10
while i<11 and i>-1:
    print(i)
    i-=1
    if i==0:
        print(i)
        print("Blast Off!")
        break

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
number = random.randint(1,10)
print(number)

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total = 0
positive = 0
zero = 0
negative = 0
for i in range(7):
    num = int(input("Enter a number. "))
    total+=num
    if num>0:
        positive+=1
    elif num<0:
        negative+=1
    else:
        zero+=1
print("The sum of your numbers is",total)
print("There are",positive,"positive numbers.")
print("There are",zero,"numbers equal to zero.")
print("There are",negative,"negative numbers.")