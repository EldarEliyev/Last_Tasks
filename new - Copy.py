#-Printing-
#A.Write a simple program that prints "Python is the beast!"
# print("Python is the beast!")

#B.Write a simple that prints "I love coding."
# print("I love coding.")


#C.Write a simple program that prints "I am going to master Python soon":
# print("I am going to master Python soon")


#D.Write a simple program that prints "I am learning Python, hooray!!":
# print("I am learning Python, hooray!!")

#E.Write a simple program that prints "Python is the most powerful programming language!":
# print("Python is the most powerful programming language!")


#-Variables-:
#A.Create a variable named "fruit" and assign any fruit-related string to it.Print that variable:
# fruit = "apple, banana, cherry"
# print(fruit)

#B.Create a variable named "sentence" and assign any string to it.Print that variable.
# sentence = "I love programming is Python and C#"
# print(sentence)


#C.Create a variable named "name" and assign any name-related string to it.Print that variable:
# name = "Eldar"
# print(name)


#D.Create a variable named "surname" and assign any name-related string to it.Print that variable.
# surname = "Eliyev"
# print(surname)


#E.Create a variable named "full_name" and assign any name-related string to it.Print that variable:
# full_name = "Eldar Eliyev"
# print(full_name)


#F.Create a variable named "colour" and assign any colour-related string to it. Print that variable:
# colour = "blue, black, white, yellow, brown"
# print(colour)


#G.Create a variable named "gender" and assingn any gender-related string to it.Print that variable:
# gender = "Male"
# print(gender)


#H.Create a variable named "brand" and assign any brand-related string to it. Print that
# variable:
# brend = "Toyota Prius"
# print(brend)



#Variables-:
#A.Create a variable which's name consists of 2 words.Assign appropriate String value to it:
# programming_language = "Python, C#" 
# print(programming_language)

#B.Create a variable which's name consists of 3 words.Assign appropriate String value to it:
# technology = "Computer, phone, mouse"
# print(technology)


# C.What's the name of the standard variable naming principle in Python?
#Answer: Snake Case

#D.What's the label(name) of any imaginary created box in computer memory?
#Answer: Variable


#-Strings-
#Create variables with appropriate names according to the following topics:
#A.Genre of music:
# genre_of_music = "Ehmed Cavadov"
# print(genre_of_music)
#B.Color:
# color = "gray, black, orange, yellow, purple, white"
# print(color)
#C.Car brand:
# car_brand = "Toyota Prius"
# print(car_brand)

#D.Digit:
# digit = 19
# print(digit)
#E.Hobby:
# hobby = "Learning is Python programming"
# print(hobby)
#F.Language:
# language = "English"
# print(language)
#G.Firstname:
# firstname = "Eldar"
# print(firstname)
#E.Lastname:
# lastname = "Eliyev"
# print(lastname)

#I.Address:
# address = "Bine Settlement"
# print(address)


#Question:
#A.A line of text that Python won't try to run as code:
#a) comment

#B.Which is used to make single line comments?
#b)#


#C.Which Python command (function) is used to output information to the screen (terminal, console) ?
#c)print


#D.What is the output of the print() function call?
# a = 'foo'
# b = 'bar'
# print(a*2+b)
#e)foofoobar


#E.What is the output of the print() function call?
# salary = "17000"
# phrase = "My salary is"
# print(phrase, salary)
#e)My salary is 17000.


#F.What is the output of the print() function call?
# salary = "17000"
# phrase = "My salar is" 
# print(salary, phrase)
#f)error



# -String Formattings-:
# A.Create a variable called 'genre'.Give it a string value:
# genre = "Uzeyir Hajibeyov"
# #B.Create a variable called 'producer' . Give it a string value:
# producer = "Film produce"
# #C.Create a variable called 'song'. Give it a string value:
# song = "Yasa Azerbaycan"
# #D.Using three Python String Formatting types(f-strings, format(), %s) create 3 variables accordingly to the formats count, and make it equal to little text (story) using all variables from Task A to C.:
# sentence = f"My janr is {genre}. My producer is {producer}. My favorite song is {song}"
# print(sentence)


#E.Create a variable called 'firstname'.Give it an appropriate value:
# firstname = "Eldar"
#F.Greate a variable called 'lastname'.Give it an appropriate value.
# lastname = "Eliyev"
#G.Create a variable called 'age'.Give it an appropriate value:
# age = 19
#H.Create a variable called "gender". Give it an appropriate value.
# gender = "Male"
#I.Using all of string formatting methods and variables from Task E to H, 
# print as the following:
# My name is John Smith, and I am 27 years old. My gender is - Male.
# word = f"My name is {firstname}, and I am {age} years old. My gender is - {gender}"
# print(word)


#J.Create a variable called 'language'. Make it equal 'Python'. Using f-strings
# print 'I love Python. I will repeat this word 5 times: PythonPythonPythonPythonPython.'
# language = "Python"
# make = f"Make it equal {language}"
# print(make)
# print("Python"*5)


#K. Create a variable called 'hello'. Make it equal 'Hello'.
# Create a variable called 'world'. Make it equal 'World'. 
# Using math operations and '.format' string-formatting method print 'Hello World!'.
# hello = "Hello"
# world = "World"
# make = f"{hello} {world}"
# print(make)


#L. Create a variable called 'hello'. Make it equal the date of your birthday in
# the following format => "01.01.2001". Using '%s' string-formatting method print
# the following:
# My birth date is 01.01.2001.

# birth_day = "02.12.2005"
# print("My birthday is, %s" % birth_day)


# M. Create a text-story using all variables created through all tasks in this
# homework file. You should use multi-line strings.
# genre = "Uzeyir Hajibeyov"
# producer = "Film producer"
# song = "Yasa Azerbaycan"
# firstname = "Eldar"
# lastname = "Eliyev"
# age = 19
# gender = "Male"
# language = "Python"
# f_string = f"My genre is {genre} . My producer is {producer}. My favorite song is {song}. My name is {firstname} {lastname}. I am {age} years old. Gender is {gender}. Make it equal {language}"
# print(f_string)



#N. Create a variable with a string value that will contain 4 curly brackets 
# (you will fill them soon). Additionally, create 4 different variables of any type 
# on your own. Using '.format' string-formatting method and those 4 variables fill 
# the previous string with 4 curly brackets. Print it.:
# name = "Eldar"
# age = 19
# f_format = "My name is {}, I'm {} years old".format(name,age)
# print(f_format)
# favorite_color = "white, black"
# f_format_favorite_color = "My favorite color is {}".format(favorite_color)
# print(f_format_favorite_color)


# favorite_language = "Python, C#"
# language_format = "My favorite language is {}".format(favorite_language)
# print(language_format)


#O. Perform math operations with strings in a 'f-string' string-formatting method.:
# num1 = 19
# num2 = 20
# answer = f"My answer is {num1+num2} "
# print(answer)


#P.Create a variable called 'expression'. Give it any string value.
# Using a variable which you have created previously and contains 4 curly brackets
# print the 'expression's value 4 times using '.format' string-formatting method.
# expressions = "Hello"
# expressions_color = "black"
# expressions_age = 19
# expressions_course = "Jed Academy"
# f_string = "My expressions is {}. My favorite color is {}. I am {} years old.I am go {} to course".format(expressions, expressions_color,expressions_age, expressions_course )
# print(f_string)


#Quiz:
#A.In the following code 'Hello is a string literal. True or False'?:
# s = 'Hello'
#a)True


#B.The two strings 'Hello' and "Hello" are identical to each other. Yes or no?
#a)Yes

#C.Is there a problem in the code below? If yes, then how can we rectify it?:
# s = 'Python's call!'
#c)Yes, bu using a multiline string


#D. How to denote a multiline string in Python?:
#a)Using """ """


#E.When used on strings, what does the * operator do?:
#a)Replicates them



#Strings:
#A.Create a variable called 'long_sentence.'Make it equal a sentence minimum.Print 'long_sentences's length.
# long_sentence = "Hello my name is Eldar. I am 19 years old"
# print(long_sentence)
# print(len(long_sentence))


#B. Replace Print function's 'end' parameter from default '\n' to '\t'.
# Write 2 Print functions with it.
# print("\nHello my name is Eldar", end="")
# print("\tI am 19 years old",end="")



#C.Change Print function's 'end' parameter, so that it links values with stars.Example: Today*is*a*good*day!
# sentence = "Today is a good day"
# word = "*".join(sentence)
# print(word)


#D. Write 3 different Print functions with according string ("He", "is", "cool.")
# in such way so you can see this on your console (you can use any method):
# He is cool.
# mytuple = ("He", "is", "cool")
# word = " ".join(mytuple)
# print(word)


#E.The same task as previous (D), but now make it look like:
# H e#is#cool.
# word = ("He", "is", "cool")
# symbol = "#".join(word)
# print(symbol)



#F. Create a variable named 'color'. Give it a string 'Python' value.
# color = 'Python'
#G. Create a variable named 'item'. Give it a string 'Developer' value.
# item = 'Developer'
#H.Use all methods you know about string-formattings and Print function
# to concatenate these two variables, so you can see 'Python Developer' on your
# console (terminal).
# f_string = f"{color} {item}"
# print(f_string)



#I. Replace Print function's 'end' parameter from default value to '...'.
# Write 3 Print functions with it.
# print("My favorite color is black", end='...')
# print("I am learning programming language is Python", end='....')
# print("I am 19 years old", end='....')



#J. Suppose you have the following variable:
word = "Hello. I am Taylor."

# Using slicing method:
# 1. Create a variable called 'prefix'. Make it equal to 'Hello.' part of 'word' variable.:
# prefix = word[0:7]
# print(prefix)


#2. Create a variable called 'middle_part'. Make it equal to ' I am ' part of 'word' variable.:
# middle_part = word[7:11]
# print(middle_part)



#3.Create a variable called 'name'. Make it equal to 'Taylor.' part of 'word' variable.
# name = word[12:19]
# print(name)


#Create a variable named 'recreated_word' or 'result' and use all previous variables (prefix, middle_part, name) to recreate the 'word'phrase.
# result = prefix, middle_part, name
# print(result)



#K. Suppose you have the following value:
# word = "abababababa"
#       01234567890
# Using slicing method, get all 'a' characters from the value and assign it to a
# variable, then print that variable
# a = word[::-2]
# print(a)


#L.Create a formula that finds the last index of a string.:
# word = "Potato"
# s = word.rfind("o")
# print(s)


#M.What is the difference between 1 and "1"? Are they equal values, why?

#Both are not the same.One is string and one is integer.

#N. Using all your Python knowledge, find the amount of words the following sentence:
# "The mission of the Python Software Foundation is to promote, protect, and advance 
# the Python programming language, and to support and facilitate the growth of a 
# diverse and international community of Python programmers."

# word = "The mission of the Python Software Foundation is to promote , protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and iternational community of Python programmers."
# print(word.count("Python"))
# print(word.count("Foundation"))
# print(word.count("programming"))
# print(word.count("language"))


#-String Methods-:
#A. Use all these string methods and test it in your code:
# 1. title
# 2. capitalize
# 3. count
# 4. endswith
# 5. find
# 6. index
# 7. isalpha
# 8. isdigit
# 9. islower
# 10. isupper
# 11. lower
# 12. upper
# 13. replace
# 14. split
# 15. strip
# 16. startswith
# 17. join


#1.title:
# word = "my programming language is python"
# print(word.title())


#2.capitalize:
# sentence = "i am favorite color is black"
# print(sentence.capitalize())


#3.count:
# word = "apple, banana,apple,kiwi"
# print(word.count("apple"))


#4.endswith:
# word = "Hello my name is Jamal."
# print(word.endswith("."))


#5.find:
# txt = "Hello, welcome my home"
# print(txt.find("welcome"))


#6.index:
# fruit = "apple, banana, berry, cherry"
# print(fruit.index("banana"))


#7.isalpha:
# sentence = "I have a question"
# print(sentence.isalpha())


#8.isdigit:
# word = "1.Name, 2.Surname"
# num = "2024"
# print(word.isdigit())
# print(num.isdigit())


#9.islower:
# text = "I am favorite sports is football "
# print(text.islower())


#10.isupper:
# test = "PYTHON LANGUAGE"
# print(test.isupper())


#11.lower:
# language = "PYTHON, C#, JAVASCRIPT"
# print(language.lower())


#12.upper:
# electronics = "phone, computer, television"
# print(electronics.upper())


#13.replace:
# word = "Hey, my name"
# print(word.replace("y", "a"))


#14.split:
# string = "What is your name?"
# print(string.split())


#15.strip:
# fruit = "           berry"
# print(fruit.strip())


#16.starstwith:
# txt = "Hello, my name is eldar"
# print(txt.startswith("Hello"))


#17.join:
# symbol = "he is cool"
# wor = "#".join(symbol)
# print(wor)


#B.Combine several string methods at once:
# combine = "      hello  I   am    19    years    old"
# print(combine.strip())


#C. Create any string-valued variable. First, call the 'lower' method on it,
# then call 'islower' method. What value will it always give you and why?
# low = "boy male"
# print(low.lower())
# print(low.islower())
#Because, two are small



#D.Suppose you have the following variable:
# my_value = "Obviously, today is a hot day."
# print(my_value.replace("o", "0"))
# Replace all 'o' characters with 0 (zeros). 



#E.Count how many times the word 'likes' occured in the following string:
# word = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
# print(word.count("like"))



#String Formattings:
#A.Create a variable 'name' and assign your name to it.
# Create a variable 'age' and assign your age to it.
# Using the f-string method, create a formatted string that displays your name 
# and age in the following format:
# "My name is [name] and I am [age] years old."
# name = "Eldar"
# age = 19
# f_string = f"My name is {name} I am {age} years old"
# print(f_string)


#B.Create a variable item and assign a string representing an item name.
# Create a variable quantity and assign an integer representing the quantity of the item.
# num = 1
# number = 2
# different = "I want to buy %d units of %s" % (num, number)
# print(different)



#C. Make your best and create a hard task by your own using string formattings.:
#?

#Chat GPT's Homework:
#A.Use the len() function to find the length of the following strings:
#1."programming"
#2."python is fun"
#3."12345"

# word = "programming"
# print(len(word))
# language = "python is fun"
# print(len(language))
# num_string = "12345"
# print(len(num_string))


#B.Convert the following string to uppercase string:
# word = "hello world"
# print(word.upper())


#C.Check if the string "python" is present in the following sentence:
# sentence = "I enjoy programming in Python."
# print(word.count("Python"))


#D. Given the string "programming", access the following elements using positive and negative indexing:
# 1. The first character
# 2. The last character
# 3. The third character
# 4. The second-to-last character
# word = "programming"
# print(word[0])#first character
# print(word[10])#last character
# print(word[5])#third character
# print(word[2])# The second-to-last character


#E.Using string slicing, extract the word "is" from the string:
# word = "Python is a versatile programming language"
# print(word[7:9])


#F.Retrieve the substring "quick brown" from the following sentence:
# sentence = "The quick brown fox jumps over the lazy dog."
# print(sentence[4:15])


#G. Reverse the following string using slicing:
# "redivider"
# word = "redivider"
# print(word[::-1])


#H.Write a program that capitalizes the first letter of each word in the following sentence:
# sentence = "welcome to the world of programming"
# print(sentence.capitalize())



#- Interview Questions -
# A. Reverse any string using slicing method.
# sentence = "Hello my name is Eldar"
# print(sentence[0:5])
# B. Print the whole string using slicing method, not knowing the length of a string.
# sentence = "Python is programming language"
# print(sentence[0:])


#Quiz:
#A.What does len('Hello') return?
#b)5

#B.What is the output of the following code snippet:
# sphere = "Web Development"* 2 + "" * 6
# length = len(sphere)
# print(length)

#Answer: 30


#C.Which of the operator can be used in Strings?
#c)Both of the above


#D.What is the output of the following code snippet:
# comment = "I like your blue pants"
# pattern = comment[19:4:-3]
# print(pattern, len(pattern))

#a)"n lry", 5


#E.Is the following variable named correctly, why?
# myVariable = "Python is best!"
#c)it depends on the code editor you type



#A.Write a program that asks user for his/her name.Print the name in capitalized form, so if the user types in'aysel', we should see 'Aysel' on the console:
# username = input("What's your name")
# print(username.title())


#B.Ask the user for their age.Substract this age from 50.:
# age = int(input("Enter your age: "))
# different = age-50
# print(different)


#C.Ask user for their address, favorite color, car brand. Using multi-line string formatting print this values using it in a sentence:
# address = input("Enter your address: ")
# favorite_color = input("Enter your favorite color: ")
# car_brand = input("Enter your car brand: ")
# f_string = f"My address is {address}. I am favorite color is {favorite_color}. My car brand is {car_brand}."
# print(f_string)


#D.Write a calculator that plusses user's inputted numbers.:
# num = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# multiple = num*num2
# sum_number = num+num2
# different = num-num2
# slices = num / num2
# print("Multiple :", multiple)
# print("Sum: ", sum_number)
# print("Different: ", different)
# print("Slices: ", slices)



#E. Write a calculator that subtracts user's inputted numbers:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# different = first-second
# print(different)



#F. Write a calculator that multiplies user's inputted numbers.:
# second = int(input("Enter your second number: "))
# third = int(input("Enter your third number: "))
# multiple = second*third
# print(multiple)



#G. Write a calculator that divides user's inputted numbers.:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# divices = first / second
# print(divices)


#H. Ask user for 3 different numbers. Multiply first two numbers
# and then divide the result by the third inputted number.:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# third = int(input("Enter your third number: "))
# divices = (first*second)/ third
# print(divices) 



#I. Write a program that prints the length of user's full name.:
# full_name = input("Please enter your full name: ")
# print(full_name)
# print(len(full_name))


#J. Write a program that asks user for some Float number. This program
# soon will round this float number. Additionally, we need to ask for
# how many decimal digits user want to round it to. Print its rounded
# value.:
# float_number = float(input("Enter your float number: "))
# num = int(input("Enter your num"))
# round_num = round(float_number, num)
# print(round_num)


#K. Write a program that asks for 2 numbers. 1st number is the main
# number, and the 2nd number is for the power the user wants the 1st
# number to raise to. So if the 1st number is 16, and the 2nd is 2,
# we should see 256 on the console.:
# num = int(input("Please enter your pow number: "))
# power = num ** 2
# print(power)



#L. Write a program that asks user for any single word. Then ask for
# any number, because we will call String's 'center' method and give
# it the number user inputted.:
# word = input("Please enter your word")
# num = int(input("Please enter your integer: "))
# x = word.center(num)
# print(x)



#M. Write a program that asks 'How many times should the program
# type "Python" word?'. Print the 'Python' word given number times.
# For example, if user gives us the 5 number, we should see on console:
# PythonPythonPythonPythonPython
# language = input("Enter your language: ")
# num = int(input("Enter your num: "))
# multiple = language*num
# print(multiple)



#N. Write a program that asks user for any sentence. The program should
# replace all characters in the sentence with its capitalized form.
# Given "I love the Python", the program should give us:
# I LOVE THE PYTHON:
# sentence = input("Please enter your sentence: ").upper()
# print(sentence)



#O. Write a program that asks user for any sentence. The program should
# replace all 'a' character in the sentence with 'o'. Given "Today is a
# great day!", the program should give us:
# # Todoy is o greot doy!:
# sentence = input("Please enter your sentence: ").replace("a", "o")
# print(sentence)


#P. Write a program that asks user for any input. The program should
# print 'True' if all characters in the input are lower characters.
# word = input("Please enter your word: ")
# print(bool(word.lower()))


#Q. Write a program that asks user for any input. The program should
# print 'True' if all characters in the input are digits.
# num = int(input("Enter your num: "))
# print(bool(num))



#R. Write a program that asks user for any phrase. The program should also
# ask for the amount the phrase will be printed. Depending on that amount print
# the user's phrase to terminal output.:
# expression = input("Please enter your expression: ")
# amount = expression*3
# print(amount)


#S. Write a program that asks user for any amount. Depending on that amount you
# should print the stars before and after the 'Hello world' phrase. Example:
# (Amount is 3)
# *** Hello world ***
# symbol = input("Please enter your symbol: ")
# word = input("Enter your word: ")
# print(symbol+ word+symbol)


#Chat GPT's Homework -
# Task 1. Create a Python program that greets the user and asks for their name. 
# Use the input() function to receive the user's input and then print a personalized greeting.
# name = input("Enter your name: ")
# print("Hello", name)


#Task2.Extend the program from Task 1 to ask the user for their birth year and 
# calculate their age. Display a message that includes their name and age.
# birth_year = int(input("Enter your birth year: "))
# now_year = int(input("Enter your now year: "))
# age = now_year - birth_year
# name = input("Enter your name: ")
# f_string = f"My name is {name}. I am {age} years old."
# print(f_string)


#Task3.Write a program that takes two numbers as input from the user and performs 
# the following math operations:
# A. Addition
# B. Subtraction
# C. Multiplication
# D. Division

# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# addition = first+second
# substraction = first-second
# multiplication = first*second
# division = first/second
# print("Addition: ", addition)
# print("Substraction: ", substraction)
# print("Multiplication: ", multiplication)
# print("Division: ", division)


#Task 4. Create a program that calculates the area of a triangle.
# Ask the user for the necessary inputs for calculations. 
# a = 5
# b = 6
# c = 7

# s = (a+b+c) / 2
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input("Enter third side: "))
# area = (s*(s-a)* (s-b)* (s-c)) ** 0.5
# print("Triangle area is: ", area)


#Task 5. Create a program that calculates the area of a rectangle.
# Ask the user for the necessary inputs for calculations
# width = float(input("Enter width: "))
# height = float(input("Enter height: "))
# area = width* height
# print("Area of rectangle= ", area)


#Task 6. Create a program that calculates the area of a square.
# Ask the user for the necessary inputs for calculations.
# num = int(input("Enter your number: "))
# second = int(input("Second: "))
# square = num ** second
# print(square)


# Task 7 (Extra!). For an extra challenge, implement a unit conversion feature. 
# Ask the user for a distance in meters and convert it to feet and inches. 
# There are approximately 3.28084 feet in a meter and 39.3701 inches in a meter. 
# Display the converted distances.:
# print("This program will convert a height given meters to a height given in feet and inches. ")
# meters = float(input("Enter height in meters:"))
# meters_in_ft = meters // .3048
# meters_in_in = meters_in_ft % 12
# print("The height is", meters_in_ft,"feet and",meters_in_in, "inches")



#Quiz:
# 1. Which of the following functions is used to convert a value to an integer in Python?:
#a)int()

#2.When using the input() function in Python, what data type is the input value 
# stored as by default?:
#c)str


#3.You want to find out how many characters are in a user-inputted sentence. 
# Which Python function would you use?:
#c)len()


#4.If a user enters "3.14159" as input using the input() function, how can you 
# convert it to a floating-point number?:
#a)float(input())


#5.If a user enters "5.7" as input using the input() function and you use 
# int(input()) for conversion, what will happen?:
#a)An error will occur since int() cannot handle decimal values.


#6.You want to display the length of a user-inputted string "Hello, World!" with a 
# descriptive message. Which option achieves this?:
#a)print("The length of the input is:", len(input()))


#7. What happens if a user enters "42" as input and you use float(input()) for 
# conversion?
#b)The value is converted to the floating-point number 42.0.


#8.To style the user prompt and concatenate it with a variable, which option is correct?:
#c)input("Enter your name: ") .format(name)


#Integers:
#A.Create a variable called 'speed'.Assign any integer value between 60 and 80 to it.:
# speed = 79
#B.Create a variable called 'limit'.Assign any integer value between 90 and 110 to it.:
# limit = 110
#C.Create a variable called 'difference'.Make it equal the difference between the 'limit' and the 'speed' variable.Print the 'difference'variable.:
# difference = limit-speed
# print(difference)

#D.Create a variable called 'amount'.Assign any integer value between 5 and 20 to it.:
# amount = 15
#E.Create a variable called 'double_amount'.Make it equal the double value of the 'amount'variable.:
# double_amount = amount*2
# print(double_amount)

#F.Create a varaible called 'triple_amount'. Make it equal the triple value of the 'amount'
# variable. Print these variables (amount, double_amount, triple_amount) separately.
# triple_amount = amount*3
# print(double_amount, triple_amount)

#G. Create a variable called 'distance'. Assign any integer value between 500 and 2000 to it.:
# distance = 1500
#H. Create a variable called 'passed_distance'. Assign any integer value between 100 and 500 to it.:
# passed_distance = 400
#I.Print the difference between the 'distance' variable and the 'passed_distance'variable:
# different = distance - passed_distance
# print(different)

#J.Create a variable called 'number_one'.Give it any integer value:
# number_one = 25
#K.Create a variable called 'number_two'.Give it any integer value:
# number_two = 30
# L.Create a variable called 'number_three'. Make it equal to the sum of 'number_one' and 'number_two'.
# Print the value of 'number_three' variable.
# number_three = 21
# sum_number = number_one+number_two
# print(sum_number)
# print(number_three)


#M. Create a variable called 'a'. Make it equal 15.:
# a = 15
#N. Create a variable called 'b'. Make it equal 35.:
# b = 35
#O. Create a variable called 'c'. Make it equal 20.:
# c = 20
#P. Create a variable called 'result'. Make it equal the sum of 'a' and 'b' minus 'c'. Print its value.:
# sum_number = (a+b)-c
# print(sum_number)


#Q.Create a variable called 'my_number'.Make it equal 4.
# my_number = 4
#R.Print 'my_numbers'raised to the third power value.:
# power = my_number**3
# print(power)


#-Floats-:
#A.Create a variable called 'temperature'.Make it equal any float number:
# temperature = 36.4
#B.Create a variable called 'weight'.Make it equal any float number:
# weight = 80.5
#C.Create a variable called 'length'. Make it equal any float number.:
# lenght = 21.4
#D. Create a variable on your own (name it appropriately). Make it equal any float number:
# price = 30.5
#E.Print all those variables from Task A to D.:
# print(temperature)
# print(weight)
# print(price)


#F. Create a variable called 'x'. Make it equal any float number between 1 and 2 with 2 decimal points.:
# x = 2.26
#G.Create a variable called 'double_x'. Make it equal double-value of 'x':
# double_x = x*2
# print(double_x)

#H. Print all those variables from Task F to G.:
# print(x)
# print(double_x)


#I. Make your best and create a hard task by your own using floats.:
# temperature = float(input("Please enter your temperature degree.:"))
# if temperature < 0:
#     print("The weather is cold")
# elif 0<= temperature <=10:
#     print("Wold")
# elif 10<= temperature <=20:
#     print("Average")
# else:
#     print("Hot")


#-Built-in functions-:
#A. Create a variable called 'long_sentence'. 
# Make it equal a long sentence. Print 'long_sentence's length.:
# long_sentence = "My favorite sport is football"
# print(long_sentence)
# print(len(long_sentence))


#B. Create a variable called 'accurate_number'.
# Make it equal any float number between 10 and 11 with 5 decimal points
# Print this variable.:
# accurate_number = 5.10

#C.Create a variable called 'rounded_accurate_number'.
# Make it equal the 'accurate_number's value rounded to 2 decimal points.
# Print this variable.:
# rounded_accurate = round(accurate_number, 2)
# print(rounded_accurate)


#D.Override 'rounded_accurate_number' variable.
# Make it equal the 'accurate_number's value rounded to 3 decimal points.
# Print this variable.:
# rounded = round(accurate_number,3)
# print(rounded)


#E.Using 'round'method round 175233, so it gives us 175000.:
# rounded = round(1.75233,2 )
# print(rounded)


#Math Module:
#A.Find the 'math' module's method by its definition:
#1.The  sqrt method returns the square root of a number.
#2.The pow method returns the value of x raised to power y.
#3.The floor method rounds a number UP to the nearest integer, if necessary, and returns the result.
#4.The _ceil____ method rounds a number DOWN to the nearest integer, if necessary, 
# and returns the result.

#B.Round π (Pi) to two decimal places.:
# rounded = round(3.141592653589793, 2)
# print(rounded)


#C.The area of a square is 700 square units. Find the side of that square.:
# area = 700
# side = area **2
# print(side)


#D. One side of a rectangle is 5 units longer than other side. Find the area of
# rectangle, if the perimeter is 100 units.
# side = 5
# rectangle = 100
# device = rectangle / side
# print(device)


#E.Round 5.7 down to the nearest integer.:
# rounded = round(5.7 )
# print(rounded)

#F. Round 5.7 up to the nearest integer.:
# round_number = round(5.7)
# print(round_number)


#- Expressions - 
# Simplify these expressions:
# A. (5 * 5 + 5 // (5 + 5 % 5) // 5) + 5**5 + 5 - 5**0
# B. (20 + 30 * (15 - 7) // (3 + 4 % 2) + 10**2 // 5) + 2**6 + 50 - 3**1
# C. (70 - 25 + 3 * (8 + 4) // (6 + 9 % 3) + 15**2 // 7) + 4**3 + 90 - 2**4

# A = (5*5+5) // (5+5%5) // 5+5**5-5**0
# print(A)

# B = 20+30*(15-7) // (3+4%2) + 10**2 // 5+(2**6) + (50-3**1)
# print(B)

# C = 70-25+3*(8+4) // (6+9%3) + 15**2//7 + 4**3 + (90-2**4)
# print(C)



#- Chat GPT's Homework -:
#Task1.Mixed Operations and Variable Naming Solve the following mixed arithmetic expressions, using appropriate variable names:
#a)Calculate the perimeter of a square with side length 6 units.
# square = 6**2
# print(square)


#b)You have $150.If you spend $47.25 and then receive $30.50, how much money do you have left?
# dollar = 150-47.25+30,50
# print("$", dollar)

#c)A train is moving at a speed of 80 km/h. How far will it travel in 1.5 hours?:
# train = 80-1.5
# print(train)


#Task2.Float Operations:
#Perform the following floating-point operations and round the answers to two decimal places:
# a = 4.25+2.68
# print(round(a,2))

# b = 9.75+3.85
# print(round(b,2))

# c = 3.5*1.2
# print(round(c, 2))

# d = 7.8 / 2.5
# print(round(d,2))



#Task3:Accessing the Value of π (Pi):
# A. Use the math.pi attribute to access the value of π (Pi) and store it in a variable.:
# from math import pi
# print(pi)
# B. Calculate and print the circumference of a circle with a radius of 7 units using 
# the π value from the math.pi attribute.

# r = float(input("Input the radius of the circle: "))
# area = pi * r**2
# print("The area of the circle with radius " + str(r) + " is: " + str(area))


# Task 4. Using 'sqrt' Method:
#A. Calculate and print the square root of 16 using the math.sqrt() method.:
# import math
# print(math.sqrt(16))

#B.Calculate and print the square root of 25 using the math.sqrt() method:
# import math
# print(math.sqrt(25))


#C.Calculate and print the square root of 10 using the math.sqrt() method:
# import math
# print(math.sqrt(10))



#Task 5. Using 'pow' Method:
#A. Calculate and print the result of raising 2 to the power of 5 using the math.pow() method.:
# num = 2
# now = pow(num, 5)
# print(now)

#B. Calculate and print the result of raising 3 to the power of 4 using the math.pow() method.:
# number = 3
# power = pow(number, 4)
# print(power)



#Task6.Use the math.ceil() method to round the following numbers up to the nearest integer:
# import math
# a = 6.1
# print(math.ceil(a))
# b = 10.9
# print(math.ceil(b))

# c = -2.3
# print(math.ceil(c))



#Task7. Use the math.floor() method to round the following numbers down to the nearest integer:
# import math
# a  = 4.7
# print(math.floor(a))

# b = 9.2
# print(math.floor(b))

# c = -3.8
# print(math.floor(c))


#Quiz:
#1.Which of the following is a comparison operator in Python?
#c)==

#2.What is the result of 15.5 - 7.2 rounded to two decimal places?
#a)8.3


#3.What is the result of 1.5 - 1.0 rounded to two decimal places?
#d)-0.5


#4.If 'a = 12' and 'b = 7', which expressions are True?
#b) a>b


#5.What is the value of 20/4?
#d)5.0


#6.Which of the following are integers?:
#b)-15



#7.What is the absolute value of -25?
#a)25


#8. If 'x = 5' and 'y = 8', what is the value of x^y (x raised to power of y)?
# x = 5
# y = 8
# print(x^y)
#a)13


#9.What does the math module in Python provide?
#b) Functions for working with complex numbers.


#10.Given the equation 3 x 8 - 5, what is the correct result?
#a)19


#11.What is the result of 17+23?
#d)40.0


#12.What is the result of "17" + "23"?
#d)"1723"




#A
# expression = True and False or True
# step_one = (True and False) or (True)
# step_two = (False) or (True)
# step_three = True
# print(step_three == expression)


#Booleans-:
# A = True or False and True
# B = False and False or False
# C = (True or False) and True
# D = True or(True or False and True) and True
# E = False or False and False and not False
# F = (True or True or False) and True
# G = False or(True and False)
# H = False and False and False and False and False or True and False
# I = True or False or True
# J = False or (not False)
# K = not True or not False
# L = False and not False or not False
# M = True or not False and True or not not True
# N = not not not False
# O = not N
# P = True or False and not True or(not True and False) and not True or False
# Q = True or not False or not True or True
# R =  False and (not True or False or (False or not True and True or False)) and True
# S = False and not not not True and (False or True or not False) and True or False
# T = not(True or False) or not False or(True and False or False)
# U = (True or not not False) and (True or (True or (False)))
# V = False and False or (not False and (not False))
# W = (not True or not False) and (not True or (not False))
# X =  False or False and not True or not False and (not True and False)
# Y =  True and True and True and True and not True and True and True or False
# Z =  False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True)
# print(A)
# print(B)
# print(C)
# print(D)
# print(E)
# print(F)
# print(G)
# print(H)
# print(I)
# print(J)
# print(K)
# print(L)
# print(M)
# print(N)
# print(O)
# print(P)
# print(Q)
# print(R)
# print(S)
# print(T)
# print(U)
# print(V)
# print(W)
# print(X)
# print(Y)
# print(Z)



#Programs:
#A.Write a program that asks user for their personal data (name, age, nationality). The program should decoratively print this values to the terminal:
# name = input("Enter your name: ")
# age = int(input("Enter your Age: "))
# nationality = input("Enter your nationality: ")
# print("Name: ", name)
# print("Age:", age)
# print("Nationality:", nationality)



#B. Write a simple calculator program that can only sum the values.
# If user inputs 10 and 5, the program should print 15:
# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# sum_number = first+second
# print(sum_number)


#C. Write a string calculator program that adds strings to strings.
# If user inputs:
# 1. 'Hello' and 'World', the program should print 'HelloWorld'.
# word = input("Enter your word: ")
# text = input("Enter your text: ")
# print(word+text)
# 2. 10 and 5, the program should print 105.
# num = input("Enter your num: ")
# number = input("Enter your number: ")
# print(num+number)
# 3. 'Hello' and 10, the program should print Hello10
# word = input("Enter your word: ")
# test = input("Enter your test: ")
# print(word+test)


# - Modules -
# A. Which Python module provides a collection of string constants, such as ascii_letters?
#string
# B. If you want to create a password generator that includes both uppercase 
# and lowercase letters, which constant from the 'string' module might be useful?
#ascii_lowercase
# C. What is the purpose of using constants like ascii_letters from the string module in Python programming?
#Draws all the letters
# D. What is 'getpass' function from 'getpass' module for?
#Generates random passwords


#- Python Tricks -
# A. Suppose you have the following variables:
# a = "Hello"
# b = 5
# a,b = b,a
# print("A=", a)
# print("B=", b)
# One-line change the value of 'a' to value of 'b', and vice versa.
# Print their values


#Constants:
#A. Create a constant variable related to Mathematics.
# NUM = int(input("Enter your num: "))
# NUMBER = int(input("Enter your number: "))
# print(NUM - NUMBER)

#B.Create a constant variable related to Physics.:
# V = 5
# T = 7
# S = V*T
# print(S)


#C. Create a constant variable related to Price.:
# PRICE_NUM = int(input("Enter your price: "))
# PRICE_NUMBER = int(input("Enter your price number: "))
# price = (PRICE_NUM*PRICE_NUMBER) / 100
# print("Price $", price)


# D. Create a constant variable related to Time.
#?


# E. Are Python constants really carry constant values?
#Yes


#- Math -
#A.Round down 57_999.99 to the nearest integer.
# number = 57_999.99
# print(round(number))


#B.Find the square root of 57_999.99. Round it to one decimal point.:
# import math
# print(math.sqrt( 57_999.99))
# print(round(240.83187081447505,1))


#C.Round up 0.0592481 to the nearest integer:
# print(round(0.059281))

#D.Find the value of 5.5 raised to power 5.
# print(pow(5.5, 5))

#NoneType:
#A.What is None in Python? How is this value described in other programming
# languages?:
#None is a unique and special data type in Python.

#B.What is the best practices of using None in Python?
# Basic solutions include checking for None before concatenation, adding a default return statement to functions, and explicitly assigning a default value to variables that may have None values.


#C.How Python evaluates the NoneType? (True / False):
#False


#D.Create any NoneType object. Print it.
# string = None
# print(string)


#Built-ins:
#A.Create two variables (x and y). Using built function raise 'y' to 'x' power.
# x = 5
# y = 4
# print(pow(x, y))

#B.Using built in fuction and variables from Task A raise 'x' to 'y' power:
# x = 5
# y = 2
# print(pow(x, y))


#C.Ask user for two integers.Raise first integer to second integer power:
# number = int(input("Enter your first number: "))
# num = int(input("Enter the second number: "))
# print(pow(number, num))



#String Formattings:
#A. You have the math's Pi number. Using f-strings, round it to two decimal points.:
# import math
# n = 2
# p = math.pi
# f_string = f"{p:.{n}f}"

# print(f_string)

#B.Write a program that represents 5_000_000 as (5,000,000) in console
# number = 5_000_000
# print(number)


#C.Write a program that calculates the percentage of apples left in the fridge.
# Initially you got 28 apples, but you ate 4. Using f-strings print the percentage
# of the apples left.:
# refrigerator = 28-4/100
# f_string = f"The percentage of apples left in the refrigerator {refrigerator}"
# print(f_string)


#Chat GPT's Homework -
# 1. What does the random.choice(seq) function do?
#c)Generates a random integer from a given range.


#2. How do you generate a random integer between 5 and 10 (inclusive) 
#using random.randint(a, b)?
# import random
# a = 5
# b = 10
# print(random.randint(a,b))
#Yes


#3. Write a code snippet that generates a random float between 0 and 1 
# (exclusive) using random.random().
# import random
# number = random.random()
# print("The float random number is: ", number)


#4.What does the random.sample(seq, k) function do?:
# import random
# number = [10,11,12,13,14,15,16]
# print(random.sample(number, k=2))

#B) Selects multiple unique random elements from the sequence.



#5.Calculate the square root of 25 using the math.sqrt() function.
# import math
# print(math.sqrt(25))


#6.How do you access the value of pi using the math module?
# import math
# print(math.pi)

#7.If you have a float value x = 7.6, how would you round it up to the nearest integer using the math ceil() function?
# import math
# print(math.ceil(7.6))


#8.Write a Python program that generates and prints 5 random integers between 50 and 100(inclusive) using the random.randint() function:
# import random
# print(random.randint(50,100))


#9.Write a Python program that takes a floating-point number as input and prints 
# its square root using the math.sqrt() function.:
# import math
# print(math.sqrt(5.21))


#10. Implement a Python "Roll Dice" program that simulates rolling a six-sided die. 
# The program should return a random number between 1 and 6.:
#?


#Interview Questions:
#1.Reverse a string with slicing method:
# word = input("Enter your word: ")
# print(word[::-1])


#Quiz:
#1.What does the None keyword represent in Python?
#d)An operaor for performing null checks


#2. Which type is assigned to a variable that has no value assigned to it in Python?
#b)NoneType


#3.What is the result of evaluating the expression: type(None)?
#a)<class 'NoneType'>


#4.Which statement assigns the value None to the variable 'result'?:
#b)result = None


#5.What is the correct way to check if a variable value is set to None?
#a) if value is not None


#6. Can None be used in arithmetic operations in Python?:
#b)No,trying to perform arithmetic with None will result in an error.


#7. What does the math.floor(x) function do?
#c)Rounds x to the nearest integer.


#8.Which of the following is the correct way to import the 'math' module in Python?
#b)import math



#9.The math.ceil(x) function does what?
#b)Returns the value of x rounded up to the nearest integer.
#c) Returns the value of x rounded down to the nearest integer.


#10.. What does the math.pow(x, y) function do?
#c)Calculates the power of x  raised to the yth power.


#11.The math.sqrt(x) function is used to:
#a)Calculate the square root of x.


#12.What is the output of the following code:
# import math
# value = 3.05
# print(math.floor(value))
#a)3



#13 What is the output of the following code:
# from math import pi
# a = round(pi,2)
# print(a*2)
#c)6.28


#14.What is the purpose of the random.choice(seq) function?
#c)It generates a random integer from a given range



#15.. Which of the following methods is used to select multiple unique random 
# elements from a sequence?
#b)random.sample(seq,count)


#16. How would you import the random module correctly in Python?
#d)import random



#17. If you want to generate a random integer between 1 and 100 (inclusive), 
# which random module method would you use?
#a)random.randint(1,100)


# 18.I n Python, what is the process of combining multiple strings into one?
#a)Concatenation



#19.What does the ascii_letters constant include?
#c)Both uppercase and lowercase letters


#20.Which PEP provides recommendations and guidelines for writing clean, readable, and maintainable Python code?
#b)PEP 8


#21. What is the primary purpose of the "as" keyword in Python's "import" statement?
#b) It allows importing multiple modules at once.


#Lists:
#A.Create an empty list and add 5 user-input integers to it:
# num = []
# num.append(1)
# num.append(2)
# num.append(3)
# num.append(4)
# num.append(5)
# print(num)


#B.Take a list of integers as input and print the sum of all the elements in the list.:
# list_number = [1,2,3,4,5,6,7,8,9,10]
# print(sum(list_number))


#C. Ask the user for a sentence and store each word as an element in a list.:
# sentence = input("Please enter your sentence: ")
# print(list(sentence))


#D.Write a program that asks user for six countries. The program should create a list of
# those countries and ask for three countries to delete from the list. Make the program
# user-friendly, and print each time the content of a list to show the user which countries
# are in a list.:
# countries = []
# countries.append("Georgia")
# countries.append("Germany")
# countries.append("Azerbaijan")
# countries.append("Turkey")
# countries.append("Amerika")
# countries.append("Arabia")
# print(countries)
# countries.pop(1)
# countries.pop(2)
# countries.pop(3)
# print(countries)



#E. Which list method makes any list look the same. The lists are the same if its content,
# elements and all other properties are the same.
# vegetables = ["eggplant", "carrot", "tomato", "potato"]
# x = vegetables.copy()
# print(x)


#F.Create an empty list and print its length.
# Write a function that accepts a list of names and returns the name with the longest length.:
# name = []
# print(len(name))
# name.append("Eldar")
# name.append("John")
# name.append("Mellim")
# name.append("Kenan")
# print(name)
# print(len(name))


#H.Ask the user for a list of integers and find the mean value of that list.:
# number = [10,100,32,4,2,1]
# print(max(number))

#I.Ask the user for a list of integers and find the third-smallest number in the list.:
# num = [22,21,1,2,3,4,5,6,7]
# print(min(num))


#J.. Write a program that asks the user for three colors separated by spaces. The
# program should print all those colors using comma (you should use string 'join' method). 
# For example:
# Your colors are red, blue, white.:
# color = input("Enter your color: ")
# x = ",".join(color)
# print(x)


#K.Write a program that asks the user for four capital cities separated by spaces. 
# The program should print all those cities the following structure:
# There are many capital cities in the world. For example, Baku, Moscow and Kyiv.
# You should follow all instructions, and not make changes to the structure of final sentence.

# cities = []
# cities.append("Baku")
# cities.append("Moscow")
# cities.append("Kyiv")
# x = "  ".join(cities)
# print(x)


#L. Take a list of strings as input and sort it in alphabetical order.:
# fruit = ["banana", "kiwi", "berry", "lemon", "strawberry", "apple", "zogal", "pear"]
# fruit.sort()
# print(fruit)


#M. Take a list of numeric values as input and sort it in descending order.:
# numeric = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
# numeric.sort()
# print(numeric)


#N. Remove duplicates from a list entered by the user while preserving the original order.:
# vegetables = ["carrot", "potato", "tomato", "eggplant"]
# vegetables.remove("carrot")
# print(vegetables)


#O. Write a program that accepts two lists and concatenates them into a single list.:
# num = [1,2,3,4,5,6]
# number = [7,8,9,10]
# print(num+number)


#The first list is a list of fruits, the second is a list of vegetables.:
# vegetables = ["carrot", "potato", "tomato", "eggplant"]
# fruit = ["banana", "kiwi", "berry", "lemon", "strawberry", "apple", "zogal", "pear"]
# print(fruit+vegetables)


#P. Write a program that prints 'True' if there is at least one item in a 'my_list' list.:
# my_list = [1,2,3,4,5]
# print(bool(my_list))


#- List Comprehension -:
#Suppose you have the following lists:
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['p', 'y', 't', 'h', 'o', 'n']
times = [1, 2, 3, 4, 5]
#A. Create a list containing raised to power two values of 'digits' list.:
# squares = list(map(lambda x:pow(x,2), digits))
# print(squares)

#B.Create a list containing capitalized version of letter values of 'letters' list.:
# input = ['p', 'y', 't', 'h', 'o', 'n']
# lst = [x.upper() for x in input]
# print(lst)


#C.Create a list containing the 'Comprehension' string value the amount of 'times'
# list's length time.:
# print(len(times))


#D. Create a list containing 5 random integers between -5 and 5. find the second-smallest 
# number in the list. The program should print 'True' if that number is negative, and 'False'
# otherwise.:
# import random
# number = random.randint(-5, 5)
# if number <0:
#     print(True, number)
# else:
#     print(False, number)



#E. Create a list of 10 random numbers and find the maximum and minimum values.:
# import random

# number = [10, 20, 1, 4, 5, 6, -1, -2, -3, 100, 99]

# max_num = max(number)
# min_num = min(number)

# x = random.choice([max_num, min_num])

# print("Random selected number:", x)



#- Chat GPT's Homework -:
#A.Create a list of colors and write a function that duplicates each color in the 
# list. For example, if the list contains "red," it should become ["red", "red"]. 
# Print the modified list.:
# color = ["red", "blue", "white"]
# colors = ["red", "purple", "black"]
# color.extend(color)
# colors.extend(colors)
# print(color)
# print(colors)


#B.How many methods do you know to create an empty list in Python? :
#[] list()


#C.Which list method is used to add an element to the end of a list?:
#append


#D.Write a Python code snippet to access the third element in a list named my_list. :
# my_list = ["orange", "apple", "carrot", "purple"]
# my_list.insert(3, "Bmw")
# print(my_list)


#E. Which list method is used to remove the last element from a list? :
#pop()


#F. What list method is used to insert an element at a specific position? :
#insert()


#G. Write Python code to reverse a list called my_list in-place. :
# my_list = ["orange", "apple", "carrot", "purple"]
# my_list.reverse()
# print(my_list)


#H. How can you create a shallow copy of a list in Python? :
#copy()


#I. Which list method is used to count the number of occurrences of a specific element in a list? :
#count()


#J. Write a Python code snippet to concatenate two lists, list1 and list2. 
# list1 = ["carrot", "potato", "tomato", "onion", "eggplant"]
# list2 = ["apple", "banana", "cherry", "kiwi", "berry"]
# print(list1+list2)


#K. What list method can be used to sort a list in ascending order? :
#sort()


#L. Write Python code to remove the first occurrence of an element 'x' from a list. :
# x = ["Bmw", "orange", "computer", "mouse", "screen"]
# x.remove("orange")
# print(x)


#M. Explain the difference between append() and extend() methods when adding elements to a list. :
#append method adds one by one but not all, but extend method adds all


#N. Which list method can be used to remove all elements from a list? :
#remove()


#O.Write Python code to find the index of the first occurrence of an element 'x' in a list. 
# x = ["computer", "screen", "phone", "mouse", "charge"]
# x.index("screen")
# print(x)


#P. What list method can be used to remove and return an element from a specific index in a list?:
#pop()


#Quiz:
#1.Which method is used to add an element to the end of a list in Python?
#d)appemd()


#2.What is the purpose of the insert() method for lists in Python?:
#c)Add an element at a spesific index in the list.


#3. Which list method is used to remove and return the last element of a list?:
#a)pop()


#4.What does the extend() method do when used on a list in Python?:
#b)Adds a new list as elements to the existing list.


#5. Which list method is used to reverse the order of elements in a list in Python?:
#a)reverse()


#6.What does the sort() method do when used on a list in Python?:
# c) Sorts the list in ascending order.


#7. Which method is used to find the index of the first occurrence of an element in a list?:
#a)index()


#8. What is the purpose of the pop() method when used on a list in Python?:
#b)Removes and returns the last element of the list.


#9.How can you count the number of occurrences of a specific element in a list?
#a)Use the count() method.


#10.How can you check if a list is empty in Python?
#c)Use the len() function and check if it's equal to zero.


#11.Which method is used to copy the elements of one list to another in Python?
#a)copy()


#12.How do you remove an element by index from a list in Python?:
#b)Use the pop() method with the index as an argument.


#13. What does the len() method do when applied to a list?:
#c)Returns the number of elements in the list.


#14.Given the following list, what is the output of min(my_list)?
# my_list = [0, 2, 4, 1, 5]
# result = min(my_list)
# print(result)
#a)0


#15.Given the following list, what is the output of max(my_list)?:
# my_list = [0,2,4,1,5]
# result = max(my_list)
# print(result)
#d)5


#16. Which list method can be used to find the number of occurrences 
# of a specific element in a list?:
#a)count()


#17.What is the output of the following code snippet?:
# my_list = [1,2,3,4,5]
# my_list.reverse()
# print(my_list)
#b)[5,4,3,2,1]


#18. What is the output of the following code snippet? 
# my_list = [1, 2, 3] 
# my_list.insert(1, 4) 
# print(my_list)
#b)[1,4,2,3]


#19. Which method is used to remove all elements from a list? :
#a)clear()


#20.What is the output of the following code snippet? 
# my_list = [1, 2, 3, 4, 5] 
# result = sum(my_list) 
# print(result)
#a)15


#21. What is the output of the following code snippet? 
# my_list = [1, 2, 3, 4, 5] 
# result = my_list.index(3) 
# print(result)
#c)2



#List-Part2:
#A.Create a list containing minimum seven different colors:
# colors = ["purple", "pink", "white", "black", "blue", "gray", "orange"]
# print(colors)

#B. Create a list containing minimum five different countries.:
# countries = ["Azerbaijan", "Turkey", "Germany", "America", "Bulgaria"]
# print(countries)


#C. Create a list containing three string values and two integer values.:
# string = ["Hello", "world", "Train", 10,20]
# print(string)


#D.. Create a list containing all continents of the world.:
# continents = ["Asia", "Africa", "North America", "South America", "Antarctica", "Australia", "Europe"]
# print(continents)


#E. Create a list containing minimum four car brands.:
# car_brand = ["Bmw", "Mercedes", "Opel", "Toyota"]
# print(car_brand)


#F.Create a list containing four different data types of Python:
# data = ["Hello", 2, 3.1, True]
# print(data)


#G. Create a list containing only negative even numbers from -2 to -12.
# negative_number = [-2,-4,-6,-8,-10,-12]
# print(negative_number)
#H. Create a list containing only positive even numbers from 0 to 12.:
# positive_number = [0,2,4,6,8,10,12]
# print(positive_number)
#I.Combine lists from Task G and H:
# print(negative_number+positive_number)


#J. Create a list containing minimum six students' names. Print the first
# student's name.:
# students = ["John", "Alex", "Alexsandra", "Bob", "Coni", "Tom"]
# print(students[0])


#K. Create a list containing three different integers. Print the integer
# at position two.:
# continets = [10,55,21]
# print(continets[1])


#L. Print the last element of Task D's list.:
# continets = [10,55,21]
# print(continets[-1])


#M. Print the last 2 elements of Task A's list. You can use slicing
# method only once. Separately printing those elements will not be accepted.:
# colors = ["purple", "pink", "white", "black", "blue", "gray", "orange"]
# print(colors[5:7])


#N. Given the following list:
# three = [3, 3, 3]
# Create a new list containing the triple value of that list.
# x = []
# x.append(three)
# print(three)
# print(x)


#O.Create any nested list. Print any value from the inner list and the whole
# inner list.
# food = [["Apple", "banana", "break", "milk"]]
# print(food)


#P. Change the value of the color at position six of the list from Task A.:
# colors = ["purple", "pink", "white", "black", "blue", "gray", "orange"]
# colors[6] = "green"
# print(colors)


#Q. From Task B's list print all countries except the first two.:
# countries = ["Azerbaijan", "Turkey", "Germany", "America", "Bulgaria"]
# countries.remove("Azerbaijan")
# countries.remove("Turkey")
# print(countries)


# R. Create two new lists containing the double value of the list from Task F 
# using 2 different mathematical operations (methods).:
#?


#S. From the following list change the value of the last element to "Bob":
# friends = ["Kevin", "Karen", "Jim", "Carry"]
# friends.pop()
# friends.append("Bob")
# print(friends)


#T.Create an empty list.:
# string = []
# print(string)



#Interview Question:
#A.Reverse a list with slicing method:
# phone = ["apple","Nokia", "Samsung"]
# print(phone[::-1])


#Bonus:
# B. Print the length of any list from previous tasks.
# phone = ["apple","Nokia", "Samsung"]
# print(len(phone))



#Note. Add the following list at the top of your code. You will use this list
# during the homework in certain tasks:
# fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
#Also print the list's modification versions to see the difference.


#List Methods:
#A.Make up a formula with built-in python "len" method that finds helps to get the last element from the 'fruits' list.:
# food = ["apple", "banana" , "cherry", "pear"]
# food.pop()
# print(food)
# print(len(food))


#B.Add any two fruits to the 'fruits' list.:
# fruit= ["apple", "banana" , "cherry", "pear", "Grape"]
# fruit.append("pineapple")
# fruit.append("watermelon")
# print(fruit)



#C.Remove third fruit so you can assign it to a variable.:
# fruit= ["apple", "banana" , "cherry", "pear", "Grape"]
# fruit.pop(3)
# print(fruit)



#D.Add a fruit to the 'fruits' list twice, and then print the amount of 
# this fruit
# in the 'fruits' list.:
# fruit= ["apple", "banana" , "cherry", "pear", "Grape"]
# print(fruit*2)


#E. Find the index of 'Grape' object in the 'fruits' list.:
# fruit= ["apple", "banana" , "cherry", "pear", "Grape"]

# print(fruit.index("Grape"))



#F. Add 'Avocado' to the 'fruits' list at position four. :
# fruit= ["apple", "banana" , "cherry", "pear", "Grape"]
# fruit.insert(4, "Avocado")
# print(fruit)


#G. Remove third fruit without getting the removed fruit.:
# fruit= ["apple", "banana" , "cherry", "pear", "Grape"]
# fruit.remove("banana")
# print(fruit)



#H. Remove a fruit at position one.:
# fruit= ["apple", "banana" , "cherry", "pear", "Grape"]
# fruit.remove("banana")
# print(fruit)


#I. Add 'Blackberry' to the end of the 'fruits' list. Remove it using 'pop' 
# method
# by finding its positive index.:
# fruit= ["apple", "banana" , "cherry", "pear", "Grape"]
# fruit.append("Blackberry")
# print(fruit)
# fruit.pop()
# print(fruit)




#J. Reverse the 'fruits' list with two different methods. Each time print 
# the reversed
# list.:
# fruit= ["apple", "banana" , "cherry", "pear", "Grape"]
# fruit.reverse()
# print(fruit)
# print(fruit[::-1])



# K. Sort alphabetically the 'fruits' list. Print the sorted version of the 
# list.
# fruit = ["banana", "apple", "cherry", "Grape", "pear"]
# fruit.sort()
# print(fruit)



#L. Suppose you have the following list:
# new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]
# fruit = ["banana", "apple", "cherry", "Grape", "pear"]
# print(new_fruits+fruit)
# Extend the 'fruits' list with the new list.


# M. Make a copy of the 'fruits' list. Remove the last three fruits. Print 
# both of the
# lists ('fruits' and the modified copied version).
# fruit = ["banana", "apple", "cherry", "Grape", "pear"]
# print(fruit.copy())
# fruit.remove("banana")
# fruit.remove("apple")
# fruit.remove("cherry")
# print(fruit)


#N. Create a variable named 'occurrence'. Make it equal True if the 
# 'Papaya' is in the
# 'fruits' list, otherwise False.:
 
# fruit = ["banana", "apple", "cherry", "Grape", "pear"]
# occurence = fruit 
# if "Papaya" in occurence:
#     print(fruit)
# else:
#     print("False")


#Variables:
#A.Suppose you have the following variables:
# x = 60
# y = 70
# x,y = y,x
# print(f"x={x}")
# print(f"y={y}")


#- ChatGPT's homework (List Methods) -
#1.Append and Extend:
#A.Write a Python program that creates an empty list and then appends 
# the following elements to it: 10, 20, 30, 40, and 50. Print the list 
# after each append operation.

# number = []
# number.append(10)
# number.append(20)
# number.append(30)
# number.append(40)
# number.append(50)
# print(number)


#B.Create a second list containing elements [60, 70, 80]. Extend the 
# first list using this second list and print the updated list.
# number = []
# number.append(10)
# number.append(20)
# number.append(30)
# number.append(40)
# number.append(50)
# print(number)

# num = [60, 70,80]
# number.extend(num)
# print(number)


#2. Insert and Remove:
#a. Write a Python program that creates a list containing the following :
# elements  = ['apple', 'banana', 'orange', 'apple', 'kiwi']
# print(elements)


#B. Use the 'insert' method to add 'pear' between 'banana' and 'orange' 
# in the list. Print the updated list.:
# elements.insert(1, "pear")
# print(elements)



#C.Use the 'remove' method to remove the first occurrence of 'apple' from 
# the list. Print the updated list.
# elements.remove("apple")
# print(elements)



#3.Count and Index:
#A. Create a list containing the following elements: 2, 4, 6, 8, 4, 10, 4, 
# 12, 14.
# number = [2,4,6,8,10,4,12,14]
# print(number)

#B. Use the 'count' method to find how many times the number 4 appears in the 
# list and print the count.
# print(number.count(4))



#C.Use the 'index' method to find the index of the first occurrence of 4 in 
# the list and print the index.
# print(number.index(4))




#4.Sort and Reverse:
#A.Create a list containing the following integers in random order: 45, 23, 
# 78, 12, 98, 56.

# following = [45,23,78,12,98,56]
# print(following)


#B.Use the 'sort' method to sort the list in ascending order and print the 
# sorted list.
# following.sort()
# print(following)


#C.Use the 'reverse' method to reverse the sorted list and print the reversed 
# list.
# following.reverse()
# print(following)



#5.Slice and Concatenate:
#A.Create a list containing the following elements: 'red', 'blue', 'green', 
# 'yellow', 'orange', 'purple'.
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
# print(colors)


#B.Use slicing to extract a new list that contains only the first three 
# colors. Print the new list.:
# print(colors[3])


#C. Use slicing again to extract a new list that contains the last three 
# colors. Print the new list.:
# print(colors[0:4])


#D. Concatenate the two sliced lists and print the final combined list.:
# print([colors[3],colors[0:4] ])



#Dictionaries:
#A.Create a dictionary with you personal data (firstname, lastname, age, gender).:
# personal_data = {
#     "firstname": "Eldar",
#     "lastname": "Eliyev",
#     "age": 19,
#     "gender": "Male"
# }
# print(personal_data)


#B.Create a dictionary with stock data of fruits (fruit name, amount in stock).:
# stock_data = {
#     "fruit_name": "Apple",
#     "amount": 5
# }
# print(stock_data)


#C. Change any value of the dictionary from Task B.:
# stock_data['amount'] = 8
# print(stock_data)



#D.Create a dictionary about five students and their math grades.:
# grades = {
#     "Alex": 99,
#     "Bob": 56 ,
#     "John": 12,
#     "Alexsandra": 20,
#     "Con": 0
# }
# print(grades)


#E.Add some points to any student from Task D's dictionary:
# grades['Con'] = 30
# print(grades)


#F.Create a dictionary about your favorite car model. Describe it as much 
# as you can (brand, manufacturing contry, tires, color, year).
# favorite_car_model = {
#     "brand": "Toyota",
#     "manufacturing": "Prius",
#     "country": "Japonia",
#     "tires": 4,
#     "color": "black",
#     "year": 1997
# }
# print(favorite_car_model)


#G.Create a dictionary with all continents of the world with minimum 3 
# countries (if possible) as its value.:
# countries = {
#     "Asia": "China, India, Japan, Turkey, Saudi Arabia, Iran, Pakistan, South Korea, Indonessia",
#     "Africa": "Nigeria, Egypt, South Africa, Kenya, Algeria, Morocco, Ethiopia, Ghana, Tanzania",
#     "Europe": "Germany, France, United Kingdom, Italy, Spain, Poland, Netherlands,Sweden,Norway"
# }
# print(countries)


#H.Create a dictionary with minimum 5 key-value pairs. Use any english word as keys, 
# and definition of those words as values. Print dictionary and its length.:
# definition = {
#     "Book": "A collection of written or printed pages bound together, used for reading or study",
#     "Water": "A transparent , tasteless, and odorless liquid essential for life.",
#     "House": "A building where people live, often a family residence.",
#     "Sun": "The star at the center of our solar system, providing light and heat to the Earth.",
#     "Friend": "A person you know well and trust, sharing a bond of mutual affection"
# }
# print(len(definition))



#I.Create a dictionary with minimum 5 key-value pairs. Use any english word as keys, 
# and translation to russian language of those words as values.
# definition = {
#     "«Книга»: «Сборник письменных или печатных страниц, связанных вместе, используемых для чтения или изучения».",
#     "«Вода»: «Прозрачная жидкость без вкуса и запаха, необходимая для жизни».",
#     "«Дом»: «Здание, в котором живут люди, часто семейное жилище.»",
#     "«Солнце»: «Звезда в центре нашей солнечной системы, обеспечивающая Землю светом и теплом».",
#     "«Друг»: «Человек, которого вы хорошо знаете и которому доверяете, разделяющий узы взаимной привязанности»"
# }
# print(len(definition))



#J. Fill in the blank:
#As of Python version 3.7, dictionaries are ordered. In Python 2.6 and earlier, dictionaries are unordered.


#K. Describe dictionaries' main 3 characteristics:
#key, value , ordered



#L. Fill in the blank:
#Only key, value objects or data types can be represented as keys in dictionaries.


#M Print all keys of dictionary from Task D.:
# grades = {
#     "Alex": 99,
#     "Bob": 56 ,
#     "John": 12,
#     "Alexsandra": 20,
#     "Con": 0
# }
# for key in grades:
#     print(key)


#N. Print all values of dictionary from Task D.:
# x = grades.values()
# print(x)


#O. Print all keys and values together of dictionary from Task D.:
# grades.keys()
# grades.values()
# print(grades)



#P.Suppose you have the following code snippet:
# car = {
#     "model": "Camaro",
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "brand": "Chevrolet",
#     "color": "red",
# }
# print(car)
#Because values are assigned to keys


#Q.Change 'color' of 'car' dictionary to 'blue'.:
# car['color'] = "blue"
# print(car)

#S.Use the whole dictionary from Task A in a string formatted with:
# 1. f-strings
# 2. format
 # 3. %s




# personal_data = {
#     "firstname": "Eldar",
#     "lastname": "Eliyev",
#     "age": 19,
#     "gender": "Male"
# }
# f_string = f"My name is {personal_data['firstname']}. My lastname is {personal_data['lastname']}. I am {personal_data['age']} years old. I am gender is {personal_data['gender']}"
# print(f_string)

# format_str = "My name is {firstname}. My lastname is {lastname}. I am {age} years old. My gender is {gender}.".format(**personal_data)
# print(format_str)



# formatted = "My name is %s and My lastname is %s. I am %d years old. My gender is %s. " %(personal_data['firstname'], personal_data['lastname'], personal_data['age'], personal_data['gender'])
# print(formatted)



# T. Create an empty dictionary. Print its length.:
# dect = {

# }
# print(len(dect))


#U. You have the following dictionary:
# grades = {
#     'Alice': 85,
#     'Bob': 90,
#     'Charlie': 78,
#     'David': 92,
#     'Emily': 88
# }
# Ask user for a student name to add 7 points to the grade of that student.:
# grades['Emily'] +=7
# print(grades)



#V.You have the following dictionary:
# word_definitions = {
#     'apple': 'a round fruit with red or green skin and crisp flesh',
#     'computer': 'an electronic device for processing and storing data',
#     'book': 'a written or printed work consisting of pages',
#     'ocean': 'a large body of saltwater that covers most of the Earth\'s surface',
#     'mountain': 'a large natural elevation of the Earth\'s surface'
# }

# Ask user for an item name to to print the length of the definition of that item.
# print(len(word_definitions['apple']))
# print(len(word_definitions['book']))
# print(len(word_definitions['computer']))
# print(len(word_definitions['mountain']))
# print(len(word_definitions['ocean']))


#ChatGpt's homework(Dictionaries)-:
#A.Create a dictionary named student_scores with the following key-va;ue pairs:
# student_scores = {
#     "Alice": 85,
#     "Bob":92,
#     "Eve": 78,
#     "Charlie":95
# }
# #Print out the dictionary student_scores:
# print(student_scores)


#B.Add a new student "David" with a score of 88 to the dictionary:
# student_scores["David"] = 88
# print(student_scores)


#C.Update Eve's score to 82:
# student_scores['Eve'] = 82
# print(student_scores)


#D.Remove Bob from the dictionary:
# student_scores.pop("Bob")
# print(student_scores)


#E.Create a Python program that asks the user to enter a key, and then prints 
# the corresponding value from the provided dictionary. If the key does not exist, 
# it should print a message saying "Key not found.":
# key = input("Enter your key dictionary")
# my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# if key in my_dict:
#     print(my_dict)
# else:
#     print("Key not found")



#F. Create a Python program that asks the user to enter a key and a value, and then 
# adds this key-value pair to the provided dictionary:
# 1. Ask the user to enter a key and a value.
# 2. Add the entered key-value pair to the provided dictionary my_dict.
# 3. Print the updated dictionary.
# key = input("Please enter your key: ")
# value = input("Enter your value is: ")
# x = {key,value}
# print(x)



#I/O:
#A. Write a program that gets the sides of a rectangle from the user, and
# calculates its perimeter.:
# length = int(input("Enter your rectangle is length: "))
# width = int(input("Enter your rectangle is width: "))
# area = length * width
# print("The area of the rectangle is: ", area)



#B.Write a program that gets the sides of a rectangle from the user, and
# calculates its area.:
# width = int(input("Enter your width is rectangle: "))
# height = int(input("Enter your rectangle is height: "))
# area = width * height
# print("Area of rectangle="+ str(area))


#C.Write a program that gets the sides of a square from the user, and calculates its perimeter:
# side = float(input("Enter the side of the square: "))
# area = side * side
# perimeter = 4 * side
# print("Square perimeter is: ", perimeter)



#D.Write a program that gets the sides of a square from the user, and
# calculates its area.:
# import math
# area = float(input("Enter your sqr area: "))
# side_length = math.sqrt(area)
# print(f"Side length: {side_length}")



#E. Write a program that gets the radius of a circle from the user, and
# calculates its area.:
# from math import pi
# radius = float(input("Input the radius of the circle: "))
# area = pi * radius ** 2
# print("The area of the circle with radius " + str(radius) + "is: " + str(area))



#F.Write a program that gets the diameter of a circle from the user, and
# calculates its length.:
# radius = int(input("Enter the radius of the circle: "))
# print("The Given radius of the circle is:", radius)
# diameter = 2 * radius
# print("The diameter of the circle is:", diameter)


#Quiz:
#1.What is a dictionary in Python?
#b)A collection of key-value pairs

#2.How do you create an empty dictionary in Python?
#a)my_dict = {}


#3.How do you access a value in a dictionary using its key?
#b)my_dict[key]

#4.Can a dictionary have duplicate keys?
#b)No


#5.How do you add a new key-value pair to an existing dictionary?
#b)my_dict[key] = value


#6.How do you remove a key-value pair from a dictionary?
#a)my_dict.remove(key)


#7.Which method returns a list of all the keys in a dictionary?
#d)my_dict.all_keys()


#8.How do you check if a key in a dictionary?
#a)key in my_dict


#9.What happens if you try to access a key in a dictionary that doesn't exist?
#a)It raises a KeyError

#10.Which dictionary method is used to retrieve the value associated with a key, and if the key does not exist, return a default value instead of raising an error?
#a)get(key,default)


#11.Which dictionary method is used to remove all key-value pairs from the dictionary?:
#a)clear()


#12.Which dictionary method returns a new dictionary with keys from the given sequence and 
# values set to a specified value?:
#a)fromkeys(seq, value)


#13. Which dictionary method returns a list of tuples, each tuple containing a key-value pair 
# from the dictionary?:
#a)items()


#14. Which dictionary method returns a list of all the values in the dictionary?:
#a)values()


#15. Which dictionary method returns and removes an element with a specified key?:
#a)pop(key)


#16. Which dictionary method returns a shallow copy of the dictionary?:
#a)copy()


#17.Which dictionary method is used to update the dictionary with key-value pairs 
# from another dictionary or from an iterable of key-value pairs?:
#a)update(iterable)


#18. Which dictionary method returns the value for a specified key and removes the 
# key-value pair from the dictionary?:
#a)popitem()


#19. What will be the output of this code:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.get('b'))
#b)2


#20 What will be the output of this code:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict['d'] = 4
# print(my_dict)

#b){'a': 1, 'b': 2, 'c': 3, 'd': 4}


#21.What will be the output of this code:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict.pop('b')
# print(my_dict)

#a){'a': 1, 'c': 3}


#22. What will be the output of this code:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(list(my_dict.items()))

#a) [('a', 1), ('b', 2), ('c', 3)]



#23.What will be the output of this code:
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict.update({'b': 5, 'd': 4})
# print(my_dict)

#b) {'a': 1, 'b': 5, 'c': 3, 'd': 4}



#24.What is the main difference between the pop() and popitem() methods in Python dictionaries?:
#d) pop() removes and returns a random key-value pair from the dictionary, while popitem() 
# removes and returns the first key-value pair.


#Tuples:
#A.Create a tuple containing minimum seven different colors.
# color = ("green", "black", "white", "blue", "gray", "orange", "yellow")
# print(color)

#B.Create a tuple containing minimum five different countries:
# countries = ("Germany", "Azerbaijan", "Turkey", "India", "America")
# print(countries)


#C.Create a tuple containing three string values and two integer values.:
# different = ("Hello", "Good", "Night", 21,22)
# print(different)


# #D.Create a tuple containing all continents of the world:
# continents = ("Asia:", "China", "Japan", "South Korea", "Turkey", "Indonesia", "Saudi Arabia", "Iran", "Azerbaijan")
# print(continents)


#E.Create a tuple containing minimum four car brands:
# car_brand = ("Toyota", "Bmw", "Audi", "Opel")
# print(car_brand)


#F.Create a tuple containing four different data types of Python:
# different_type = ("Hello", 24, 2.3, True)
# print(different_type)


#G.Create a tuple containing only negative even numbers from -2 to -12:
# negative_even = (-2,-4,-6,-8,-10,-12)
# print(negative_even)


#H.Greate a tuple containing only positive even numbers from 0 to 12:
# positive_even = (2,4,6,8,10,12)
# print(positive_even)


#I.Combine tuples from Task G and H:
# print(negative_even +  positive_even)


#J.Create a tuple containing minimum six students' names. Print the first
# student's name.:
# students = ("Bob", "Alex", "Kenan", "Yusif", "Kamil", "Aleksandra")
# print(students[0])


#K. Create a tuple containing three different integers. Print the integer
# at position two.
# different = (21,24,56)
# print(different[1])


#L.Print the last element of Task D's tuple.:
# continents = ("Asia:", "China", "Japan", "South Korea", "Turkey", "Indonesia", "Saudi Arabia", "Iran", "Azerbaijan")
# print(continents[8])


#M. Print the last two elements of Task A's tuple. You can use slicing
# method only once. Separately printing those elements will not be accepted.
# color = ("green", "black", "white", "blue", "gray", "orange", "yellow")
# print(color[5:7])


# #N. Given the following tuple:
# double_me = (0, 5, 10)
# print(double_me*2)
#Create a new tuple containing the double value of that tuple.


#O. Create any nested tuple. Print any value from the inner tuple and the whole
# inner tuple.
# test = (3,4)
# test2 = (5,6)
# print("The original tuple: " + str(test))
# print("The original tuple 2 :" + str(test2))
# result = test + test2
# print("Tuples after Concatenating: " + str(result))


#P. Change the value of the color at position six of the tuple from Task A.
# color = ("green", "black", "white", "blue", "gray", "orange", "yellow")
# y = list(color)
# y[6] = "purple"
# x = tuple(y)
# print(x)


#Q. From Task B's tuple print all countries except the first two.:
# countries = ("Germany", "Azerbaijan", "Turkey", "India", "America")
# print(countries[2:])


#R. Create two new tuples containing the double value of the tuple from Task F 
# using 2 different mathematical operations.
# different_type = ("Hello", 24, 2.3, True)
# print(different_type*2)


#S.Create an empty tuple:
# my_tuple = ()
# print(my_tuple)


#T.Create a tuple with only the one 'Python' string value. Print its type.:
# language = ("Python")
# print(language)
# print(type(language))


#U. Count how many times the word 'hacking' appears in this tuple:
# black_hat = ('hacking', 'hiding', 'hiking', 'hacking', 'viking', 'horsing', 'black', 'hat', 'hacking')
# print(black_hat.count('hacking'))


#V. Count how many 'True's are in this tuple:
# booleans = (True, True, False, True, False, False, True)
# print(booleans.count(True))


#W.Find the position of the first 'a' character in the following tuple:
# randomized_alphabet = ('b', 'w', 'v', 't', 'n', 'c', 'd', 'a', 'f', 'a')
# print(randomized_alphabet[7])


#X. When should you consider using constant variables with tuples in your Python code? 
# Provide an example scenario.
#?


#Bonus:
#A.Print the wholw tuple from previous tasks using the slicing method:
# car_brand = ("Toyota", "Bmw", "Audi", "Opel")
# print(car_brand[0:])

#B.Print the length of any tuple from previous tasks.
# car_brand = ("Toyota", "Bmw", "Audi", "Opel")
# print(len(car_brand))


#Sets:
#You have the following set:
# ages = {12,14,16,18,20,22,24,26}
#A.Write a Python program to remove an item from the 'ages' set if it is present in the set:
# ages.remove(16)
# print(ages)

#B.Add 28 to 'ages' set:
# ages.add(28)
# print(ages)

#C.Copy this set. Check if this copied set is a subset of the original set.:
# x = ages.copy()
# print(x)


#D.Check if the following set is a subset of the 'ages' set:
# suspected_subset = {12,14}
# print(suspected_subset, ages)


#E.Remove 12 and 14 from the 'ages' set:
# ages.remove(12)
# ages.remove(14)
# print(ages)


#F.You have the following tuple and set:
# names = ('Murad', 'Aysel', 'Gunel')
# students = {'Bob', 'John'}
#Extend the 'students' set with the 'names'.
# x = list(names)
# x.extend(students)
# a = tuple(x)
# print(a)


#G. Find the difference between the following sets:
# fruits = {"apple", "banana", "cherry"}
# items = {"google", "microsoft", "apple"}
# print(fruits-items)


#H. Print the length of the 'ages' set. Then add 12 to the 'ages' set. Print the
# length again.
# ages = {14,16,18,20,22,24,26}
# print(len(ages))
# ages.add(12)
# print(len(ages))

#I.Clear the 'ages' set.Print it and its length:
# ages = {14,16,18,20,22,24,26}
# ages.clear()
# print(len(ages))



#Interview Questions:
#A.Reverse a tuple with slicing method:
# electronic = ("Computer", "Phone", "Television", "tablet")
# print(electronic[::-1])

#B.What's the main difference between Tuples and Lists in Python?
#List: is a collection with is ordered and changeable.Allows duplicate members.
#Tuple: is a collection which is ordered and unchangable.Allows duplicate members.


#C.What's the best practice to use Sets, and not Lists or Tuples?:
#do not repeat the code


#D. What's the difference between Set's 'remove' and 'discard' method?
#The discard() method removes the specified item from the set. This method is different from the remove() method, beacuse the remove() method will raise an error if the specified item does not exist and the discard() method will not


#E. You have the following list of the students of 7th grade class:
# names = ["Murad", "Mike", "Murad", "Elcin", "Vuqar", "Murad", "Nargiz"]
# names = list(set(names))
# print(names)
# How can you remove all duplicate names from this list?


#F.When might you choose to use a set instead of a list or tuple in Python? Provide an example scenario:
# my_list = ["Apple", "banana", "vitamin", "screen"]
# my_list.append("Board")
# print(my_list)
# my_tuple = ("type", "different", "toys", "bicle")
# x = list(my_tuple)
# x.append("word")
# a = tuple(x)
# print(a)


#Chat GPT's Homework:
#A.Create a Python tuple named student_info that contains the following information about a student:
#1.Student's name
#2.Student'age
#3.Student's grade(as a string, e.g., "A" or "B")
# student_info = ("John", 20, "A")
# print(student_info)


#B.Create an empty list called shopping_cart.Then, perform the following operations:
#1.Add three items to the shopping cart.
#2.Remove one item from the shopping cart.
#3.Modify one of the items in the shopping cart.
# shopping_cart = []
# shopping_cart.append("Aksesuar")
# shopping_cart.append("Electronic")
# shopping_cart.append("Phone")
# print(shopping_cart)
# shopping_cart.remove("Aksesuar")
# print(shopping_cart)
# shopping_cart[1] = "Plastic"
# print(shopping_cart)



#C. Create a tuple named coordinates containing latitude and longitude values. 
# Then, use tuple unpacking (*) to assign these values to separate variables called latitude and longitude. 
# Print the values of latitude and longitude.:
#?


#D.Explain in your own words the main differences between tuples and lists in Python.
# Provide examples of situations where you would use one over the other.
#both allow duplicates, but tuples do not change lists


#Quiz:
#1.What is a tuple in Python?
#b)An ordered collection of elements that is immutable


#2.How do you create an empty tuple in Python?
#a)empty_tuple = ()


#3.Which of the following statements is true about sets in Python?
#a)Sets are ordered collections


#4.What is the primary purpose of using sets in Python?
#b)To ensure elements are unique and eliminate duplicates.


#5.Which of the following is true about the elements of a set in Python?
#d)Elements of a set can be of different data types


#6. What is the result of the following code?
# my_set = {1,2,3}
# my_set.add(4)
# my_set.remove(2)
# print(my_set)

#b){1,3,4}


#7.Which of the following set operations returns the elements that are common to two sets?
#a)union()

#8. Can a tuple contain elements of different data types?
#a)Yes


#9.What is the key difference between a tuple and a list in Python?
#b) Lists are ordered and mutable, while tuples are ordered and immutable.


#10. Which of the following is a valid way to create a set in Python?:
#a)my_set = {1, 2, 3}


#11. Which of the following statements is true about tuples in Python?
#d)Tuples are unordered collections.


#12. What is the advantage of using tuples over lists in Python?:
#c) Tuples are faster for accessing elements.


#13. Which of the following list comprehensions creates a tuple of squares of numbers from 1 to 5?
#a)squared_tuple = (x ** 2 for x in range(1, 6))


#14. What is the primary advantage of using sets when dealing with collections of data?:
#a)Sets preserve the order of elements.


#15.. In Python, what would be the result of applying the union() operation on two sets that 
# have some overlapping elements?
#d)The operation will return an empty set.   
    


#16.How can you remove an item from a list without knowing its index?
#a) Using the remove() method.


#17.Which of the following statements is true about list comprehensions?:
#a)List comprehensions can only be used with lists.


#18. What is the difference between the discard() and remove() methods for sets in Python?:
#b) remove() removes an element if it exists; discard() returns the element if found.


#19.. In Python, can a list contain elements of different data types?
#a)Yes


#20. In Python, what is a constant variable?:
#c) A variable whose value should not change after it's initially assigned.


#21.Which data structure in Python is commonly used to define constant variables?
#a)Lists


#22. How do you define a constant variable using a tuple in Python?:
#b)constant_var = [value]


#23.. When defining constant variables using tuples, what is the recommended naming convention?
#b)Use uppercase letters with underscores (e.g., MY_CONSTANT_VAR).


#24.Which of the following operations is valid for a constant variable defined using a tuple?:
#b)Accessing its elements.


#25.Why might you choose to use a constant variable defined with a tuple instead of a regular variable?
#b)To make the code less readable.


#26.Which of the following code examples correctly defines a constant variable using a tuple?:
#b)const_var = [3.14, 'hello', True]


#27.What is the advantage of using constant variables with tuples over hardcoding values directly into your code?:
#b) It improves code readability.


#28. In Python, can you reassign a value to a constant variable defined using a tuple?:
#b)No


#29. What does the asterisk (*) operator do when used with a variable in Python?:
#d)Converts the variable to a string.


#30.In Python, what does the from module_name import * statement do when importing a module?
#a)It imports all functions, classes, and variables from the module.


#31.When might it be appropriate to use the asterisk () in a module import statement?:
#b) When you want to import all contents of the module for convenience.