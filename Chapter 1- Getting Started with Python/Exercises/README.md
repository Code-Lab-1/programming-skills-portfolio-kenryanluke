# Chapter 1 Exercises

Exercises with a tick mark :ballot_box_with_check: represent exercises that must be submitted as part of your Programming Skills Portfolio as a minimum expectation. Completing more exercises provides the opportunity to attain higher marks. For each exercise you should create a _**new project**_ with the name of the exercise and save it to this exercises folder in your local repository.

Once you have completed your solution you should make sure you commit and push your solutions to your remote repository on GitHub. You can commit and push as many changes to your solutions as you wish, only those pushed before the chapter deadlines will be marked for the Programming Skills Portfolio.  


&nbsp;

## Exercise 1: Print Strings :ballot_box_with_check:

Write a Python program to print the following string in a specific format.

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

print("Twinkle, twinkle, little star,")
print("How I wonder what you are! Up above the world so high,")
print("Like a diamond in the sky.")
print("Twinkle, twinkle, little star, How I wonder what you are") 

&nbsp;
&nbsp;
&nbsp;
## Exercise 2: Print the Version of Python :ballot_box_with_check:

 Write a Python program to get the Python version you are using.

import sys
print("Python version")
print (sys.version)

&nbsp;
&nbsp;
&nbsp;
## Exercise 3: Print date and Time :ballot_box_with_check:

Write a Python program to display the current date and time.

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

&nbsp;
&nbsp;
&nbsp;
## Exercise 4: Strings Concatination :ballot_box_with_check:
Write three strings in different variables and print the output as one string.

word1 = "three"
word2 = "different"
word3 = "variables"
print(word1 ,word2 ,word3)

&nbsp;
&nbsp;
&nbsp;

## Exercise 5: Compute area of Circle :ballot_box_with_check:

Write a Python program which accepts the radius of a circle from the user and compute the area.

r = int(input("Enter radius of circle: "))
pi = 3.14159
area = pi * r **2
print(area)

&nbsp;
&nbsp;
&nbsp;

