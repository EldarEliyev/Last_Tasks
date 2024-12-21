#Printing-
#A.Write a simple program that prints "Python is the beast!":
# print("Python is the beast!")

#B.Write a simple program that prints "I love coding":
# print("I love coding.")


#C.Write a simple program that prints "I am going to master Python soon"
# print("I am going to master Python soon")


#D.Write a simple program that prints "I am learning Python, hooray!!":
# print("I am learning Python, hooray!!")


#E.Write a simple program that prints "Python is the most powerful programming language!":
# print("Python is the most powerful programming language!")


#Variables:
#A.Create a variable named "fruit" and assign any fruit-related string to it. Print that variable:
# fruit = "apple, banana"
# print(fruit)


#B.Create a variable named "sentence" and assign any string to it. Print that variable:
# sentence = "I am learning to Python language!!"
# print(sentence)


#C.Create a variable named "name" and assign  any name-related string to it.Print that variable:
# name = "Eldar"
# print(name)


#D.Create a variable named "surname" and assign any name-related string to it. Print that variable:
# surname = "Eliyev"
# print(surname)


#E. Create a variable named "full_name" and assign any name-related string to it. Print that
# variable.
# full_name = "Eldar Eliyev"
# print(full_name)


#F.Create a variable named "colour" and assign any colour-related string to it. Print that
# variable.:
# colour = "Red, White"
# print(colour)


#G.Create a variable named "gender" and assign any gender-related string to it.Print that variable:
# gender = "Male"
# print(gender)

#H.Create a variable named "brand" and assign any brand-related string to it.Print that variable:
# brand = "Toyota Prius"
# print(brand)


#Variables-:
#A.Create a variable which's name consists of 2 words. Assign appropriate String value to it:
# name = "Eldar"
# surname = "Eliyev"
# print(name)
# print(surname)


#B.Create a variable which's name consists of 3 words.Assign appropriate String value to it:
# vegetables = "onion, purple, eggplant"
# fruit = "apple, banana, cherry"
# brand = "Adidas, Nike, Puma"
# print(vegetables)
# print(fruit)
# print(brand)


#C.What's the name of the standard variable naming principle in Python?
#Snake_case


#D.What's the label (name) of any imaginary created box in computer memory?
#Variable


#Strings:
#Create variable with appropriate names according to the following topics:
#A.Genre of music:
# genre = "Uzeyir Hajibeyov"
# print(genre)

#B.Color:
# color = "White, black, red"
# print(color)

#C.Car brand:
# car_brand = "Toyota Prius"
# print(car_brand)


#D.Digit:
# digit = "1299"
# print(digit)


#E.Hobby:
# hobby = "Python learning"
# print(hobby)


#F.Language:
# language = "Python"
# print(language)

#G.Firstname:
# firstname = "Eldar"
# print(firstname)


#H.Lastname:
# lastname = "Eliyev"
# print(lastname)

#I.Address:
# address = "Bine "
# print(address)


#Quiz:
#A.A line of text that Python won't try to run as code:
#a)comment

#B.Which is used to make single line comments?
#b)#


#C.Which Python command(function) is used to output information to the screen(terminal, console) ?:
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
#c)My salary is 17000


#F.What is the output of the print() function call?:
# salary = "17000"
# phrase = "My salary is"
# print(salary, phrase)
#a)it's not pythonic code


#String Formattings:
#A.Create a variable called 'genre'.Give it a string value:
# genre = "narrative"
# f_string = f"My genre is: {genre}"
# print(f_string)


#B.Create a variable called 'producer'.Give it a string value:
# producer = "autotrophs"
# print(f"My producer is: {producer}")


#C.Create a variable called 'song'. Give it a string value.:
# song = "Shazam"
# print(f"My song is: {song}")


#D. Using three Python String Formatting types (f-strings, .format(), %s) 
# create 3 variables accordingly to the formats count, and make it equal 
# to little text (story) using all variables from Task A to C.

# song = "Shazam"
# producer = "autotrophs"
# genre = "narrative"

# print(f"The song name is: {song}")
# print(f"Producer is: {producer}")
# print(f"Genre name is: {genre}")

# string = song
# print("Hey, %s" % string)
# txt = "For only {producer} name."
# print(txt.format(producer="autotrophs"))



#E. Create a variable called 'firstname'. Give it an appropriate value.:
# firstname = "Eldar"
# print(f"My firstname is: {firstname}")


#F.Create a variable called "lastname". Give it an appropriate value:
# lastname = "Eliyev"
# print(f"My lastname is: {lastname}")


#G.Create a variable called 'age'. Give it an appropriate value.:
# age = 19
# print(f"My age is: {age}")


#H. Create a variable called 'gender'. Give it an appropriate value.:
# gender = "Male"
# print(f"My gender is: {gender}")


#I. Using all of string formatting methods and variables from Task E to H, 
# print as the following:
# My name is John Smith, and I am 27 years old. My gender is - Male.

# gender = "Male"
# age = 19
# lastname = "Eliyev"
# firstname = "Eldar"
# txt = "My name is {}, I am {} years old. My gender is {}".format(firstname, age, lastname, gender)
# print(txt)


#J. Create a variable called 'language'. Make it equal 'Python'. Using f-strings
# print 'I love Python. I will repeat this word 5 times: PythonPythonPythonPythonPython.':
# language = "Python"
# print(f"I love {language}")
# print(language*5)


#K. Create a variable called 'hello'. Make it equal 'Hello'.
# Create a variable called 'world'. Make it equal 'World'. 
# Using math operations and '.format' string-formatting method print 'Hello World!'.:
# hello = "Hello"
# world = "World"
# formatting = "{} {}".format(hello, world)
# print(formatting)

# print(hello+world)


# L. Create a variable called 'hello'. Make it equal the date of your birthday in
# the following format => "01.01.2001". Using '%s' string-formatting method print
# the following:
# My birth date is 01.01.2001.:

# hello = "02.12.2005"
# print("My birth date is %s" % hello)


#M. Create a text-story using all variables created through all tasks in this
# homework file. You should use multi-line strings.:
# genre = "Uzeyir Hajibeyov"
# producer = "Film producer"
# song = "Yasa Azerbaycan"
# firstname = "Eldar"
# lastname = "Eliyev"
# age = 19
# gender = "Male"
# language = "Python"
# f_string = f"My genre is {genre}. My producer is {producer}. My favorite song is {song}. My name is {firstname} {lastname}. I am {age} years old. Gender is {gender}. Make it equal {language} "
# print(f_string)


#N. Create a variable with a string value that will contain 4 curly brackets 
# (you will fill them soon). Additionally, create 4 different variables of any type 
# on your own. Using '.format' string-formatting method and those 4 variables fill 
# the previous string with 4 curly brackets. Print it.:
# name = "Eldar"
# age = 19
# f_format = "My name is {}, I'm {} years old".format(name, age)
# print(f_format)
# favorite_color = "white, black"
# f_color = "My favorite color is {}".format(favorite_color)
# print(f_color)


# favorite_language = "Python"
# language = "My favorite language is {}".format(favorite_language)
# print(language)


#O. Perform math operations with strings in a 'f-string' string-formatting method.:
# num1 = 10
# num2 = 31
# answer = f"My answer is {num1+num2}"
# print(answer)


#P. Create a variable called 'expression'. Give it any string value.
# Using a variable which you have created previously and contains 4 curly brackets
# print the 'expression's value 4 times using '.format' string-formatting method.:

# expressions = "Hello"
# expressions_color = "White"
# expressions_age = 19
# expressions_course = "Jed Academy"
# f_string = "My expressions is {}. My favorite color is{}. I am {} years old. I am go {} to course ".format(expressions, expressions_color,expressions_age, expressions_course )
# print(f_string)


#Quiz:
#A.In the following code "Hello" is a string literal.True or false?
# s = 'Hello'
#a)True


#B.The two strings 'Hello' and "Hello" are identical to each other. Yes or no?
#a)Yes


#C.Is there a problem in the code below? If yes, then how can we rectify it?:
# s = 'Python's call!'  
#c)Yes, bu using a multiline string


#D.How to denote a multiline string in Python?:
#c) Using either (b) and (c)


#E.When used on strings, what does the * operator do?:
#a)Replicates them


#Strings:
#A.Create a variable called 'long_sentence'.Make it equal a sentence minimum.Print  'long_sentence's length:
# long_sentence = "Hello. My name is Eldar. I am 19 years old. I am learning Python language."
# print(long_sentence)
# print(len(long_sentence))


#B. Replace Print function's 'end' parameter from default '\n' to '\t'.
# Write 2 Print functions with it.:

# print("\nHello my name is Eldar", end="")
# print("\tI am learning language is Python", end="")

#C.Change Print function's 'end' parameter, so that it links values with
# stars. Example:
# sentence = "Today is a good day"
# word = "*".join(sentence)
# print(word)


#D. Write 3 different Print functions with according string ("He", "is", "cool.")
# in such way so you can see this on your console (you can use any method):
# He is cool.
# sentence = ("He", "is", "cool")
# word = " ".join(sentence)
# print(word)


#E. The same task as previous (D), but now make it look like:
# He#is#cool.
# world = "He is cool"
# print("#".join(world))


#F. Create a variable named 'color'. Give it a string 'Python' value.:
# color = "Python"
# print(color)


#G. Create a variable named 'item'. Give it a string 'Developer' value.:
# item = "Developer"
# print(item)


#H. Use all methods you know about string-formattings and Print function
# to concatenate these two variables, so you can see 'Python Developer' on your
# console (terminal).

# color = "Python"
# item = "Developer"
# string = f"{color} {item}"
# print(string)


#I. Replace Print function's 'end' parameter from default value to '...'.
# Write 3 Print functions with it.:
# print("Hello, my name is John", end='....')
# print("My country is England", end='......')
# print("I am 19 years old", end='...........')


#J.Suppose you have the following variable:
# word = "Hello.I am Taylor"

#Using slicing method:
#1.Create a variable called 'prefix'. Make it equal to 'Hello.' part of 'word' variable.:
# prefix = word[0:6]
# print(prefix)

#2.Create a variable called 'middle_part'. Make it equal to ' I am ' part of 'word' variable.:
# middle_part = word[6:10]
# print(middle_part)


#3.Create a variable called 'name'. Make it equal to 'Taylor.' part of 'word' variable.
# Create a variable named 'recreated_word' or 'result' and use all previous variables 
# (prefix, middle_part, name) to recreate the 'word' phrase.
# name = word[11:17]
# # print(name)
# print(prefix,middle_part, name)


#K.Suppose you have the following value:
# word = "abababababa"

# Using slicing method, get all 'a' characters from the value and assign it to a
# variable, then print that variable.
# perfect = word[0:11:2]
# print(perfect)

#L. Create a formula that finds the last index of a string.:
# word = input("Enter your word: ")
# print(word[-1])


#M. What is the difference between 1 and "1"? Are they equal values, why?:
#Not equal .Because one is a string.One is an integer.Unable to add integer string.


#N. Using all your Python knowledge, find the amount of words the following sentence:
# word = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language,and to support and facilitate the growth of a diverse and iternational community of Python programmers. "
# print(len(word))
# length = len(word[:])
# print(length)


#String Methods:
#A.Use all these string methods and test it in your code:
#1.title:
# word = "uzeyir hacibeyov"
# print(word.title())

#2.capitalize:
# name = "eldar eliyev"
# print(name.capitalize())


#3.count:
# sentence = "python my language is python"
# print(sentence.count("python"))


#4.endswith:
# txt = "Hello, welcome to my world."
# print(txt.endswith("."))


#5.find:
# text = "Hello, my name is eldar"
# print(text.find("eldar"))


#6.index:
# fruit = "apple, banana, cherry"
# x = fruit.index("banana")
# print(x)


#7.isalpha:
# word = "TeslaX"
# x = word.isalpha()
# print(x)


#8.isdigit:
# word = "birthday2005"
# a = word.isdigit()
# print(a)


#9.islower:
# word = "apple, banana,computer"
# print(word.islower())


#10.isupper:
# country = "QARABAG, AZERBAYCAN"
# print(country.isupper())


#11.lower:
# electronic = "COMPUTER, PHONE, TELEVISION"
# print(electronic.lower())


#12.upper:
# web = "trendyol, tap.az, lalafo"
# print(web.upper())


#13.replace:
# word = "apple, banana"
# print(word.replace("a", "o"))


#14.split:
# test = "Hello my name is eldar"
# x = test.split()
# print(x)


#15.strip:
# language = "       Python      C#"
# print(language.strip())


#16.starstwith:
# sentence = "Hello, my welcome world"
# print(sentence.startswith("Hello"))

#17.join:
# word = ("He", "is", "cool")
# sentence = "@".join(word)
# print(sentence)

#B.Combine several string methods at once:
# combine = "     hello  I am 20   years   old"
# print(combine.strip())


#C.Create any string-valued variable. First, call the 'lower' method on it,
# then call 'islower' method. What value will it always give you and why?:
# word = "apple"
# print(word.lower())
# print(word.islower())
#Because two are small 



#D.Suppose you have the following variable:
# my_value =  "Obviously, today is a hot day."
# print(my_value.replace("o", "0"))
#Replace all 'o' characters with 0 (zeros).


#E. Count how many times the word 'likes' occured in the following string:
# word = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
# print(word.count("likes"))


#String Formattings-:
#A. Create a variable 'name' and assign your name to it.
# Create a variable 'age' and assign your age to it.
# Using the f-string method, create a formatted string that displays your name 
# and age in the following format:
# "My name is [name] and I am [age] years old."

# name = "Eldar"
# age = 19
# print(f"My name is {name} and I am {age} years old. ")


#B.B. Create a variable item and assign a string representing an item name.
# Create a variable quantity and assign an integer representing the quantity of the item.
# Create a formatted string using the old-style % formatting that displays the item 
# name and quantity in the following format:
# "I want to buy %d units of %s."


# num = 20
# number = 32
# different = "I want to buy %d units of %s" % (num, number)
# print(different)


# C. Make your best and create a hard task by your own using string formattings.
#?


#Chat GPT's Homework"
#A.Use the len() function to find the length of the following strings:
# 1. "programming"
# word = "programming"
# print(len(word))
# 2. "python is fun"
# language = "python is fun"
# print(len(language))
# 3. "12345"
# string = "12345"
# print(len(string))


#B.Convert the following string to uppercase string:
# word = "hello world"
# print(word.upper())


#C.Check if the string "python" is present in the following sentence:
# sentence = "I enjoy programming in Python"
# print(sentence.find("Python"))


#D.Given the string "programming", access the following elements using positive and negative indexing:
# 1. The first character
# word = "programming"
# index = word[0]
# print(index)
# 2. The last character
# word = "programming"
# print(word[-1])
# 3. The third character
# word = "programming"
# print(word[3])
# 4. The second-to-last character
# word = "programming"
# print(word[2:11])


#E. Using string slicing, extract the word "is" from the string:
# word ="Python is a versatile programming language."
# print(word[7:9])


#F.Retrieve the substring "quick brown" from the following sentence:
# sentence = "The quick brown fox jumps over the lazy dog."
# print(sentence[4:15])


#G.Reverse the following string using slicing:
# word = "redivider"
# print(word[::-1])


#H.Write a program that capitalizes the first letter of each word in the following sentence:
# sentence = "welcome to the world of programming"
# print(sentence.title())


#- Interview Questions -
#A.Reverse any string using slicing method:
# word = "apple"
# print(word[::-1])


#B.Print the whole string using slicing method, not knowing the length of a string:
# sentence = "Python programming language"
# print(sentence[0:])


#Quiz:
#A.What does len("Hello") return?
#a)5

#B.What is the output of the following code snippet:
# sphere =  "Web Development" * 2 + "" * 6
# length = len(sphere)
# print(length)
#d)30


#C.Which of the operator can be used in Strings?:
#c)Both of the above


#D.What is the output of the following code snippet:
# comment = "I like your blue pants"
# pattern = comment[19:4:-3]
# print(pattern, len(pattern))

#a)"n lry",5


#E. Is the following variable named correctly, why?

# myVariable = "Python is best!"

#c) it depends on the code editor you type


#Input:
#A.Write a program that asks user for his/her name. Print the name in capitalized form, so if the user types in 'aysel', we should see 'Aysel' on the console:
# name = input("Enter your name").title()
# print(name)


#B. Ask user for their age. Subtract this age from 50.
# age = int(input("Enter your age: "))
# different = age - 50
# print(different)


#C. Ask user for their address, favorite color, car brand.
# Using multi-line string formatting print this values using it
# in a sentence.

# address = input("Enter your address: ")
# favorite_color = input("Enter your favorite color: ")
# car_brand = input("Enter your car brand: ")

# f_string = f"My address is {address}. I am favorite color is {favorite_color}. My car brand is {car_brand}"
# print(f_string)


# D. Write a calculator that plusses user's inputted numbers.:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# sum_number = first + second
# print(sum_number)


#E.Write a calculator that subtracts user's inputted numbers:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# different = first-second
# print(different)


#F. Write a calculator that multiplies user's inputted numbers.:
# second = int(input("Enter your second number: "))
# third = int(input("Enter your third number: "))
# multiple = second * third
# print(multiple)


#G. Write a calculator that divides user's inputted numbers.:
# num = int(input("Please enter your num: "))
# number = int(input("Enter your number: "))
# divides = num / number
# print(divides)


#H. Ask user for 3 different numbers. Multiply first two numbers
# and then divide the result by the third inputted number.:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# third = int(input("Enter your third number: "))
# different = (first * second) / third
# print(different)


#I. Write a program that prints the length of user's full name.:
# fullname = input("Enter your full name: ")
# print(fullname)
# print(len(fullname))


#J. Write a program that asks user for some Float number. This program
# soon will round this float number. Additionally, we need to ask for
# how many decimal digits user want to round it to. Print its rounded
# value.

# number = float(input("Enter your number: "))
# num = int(input("Enter your num: "))
# rounded = round(number, num)
# print(rounded)



#K. Write a program that asks for 2 numbers. 1st number is the main
# number, and the 2nd number is for the power the user wants the 1st
# number to raise to. So if the 1st number is 16, and the 2nd is 2,
# we should see 256 on the console.:

# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# power =  pow(first, second)
# print(power)


#L. Write a program that asks user for any single word. Then ask for
# any number, because we will call String's 'center' method and give
# it the number user inputted.:

# word = input("Enter your word: ")
# num = int(input("Enter your num: "))
# x = word.center(num)
# print(x)


# M. Write a program that asks 'How many times should the program
# type "Python" word?'. Print the 'Python' word given number times.
# For example, if user gives us the 5 number, we should see on console:
# PythonPythonPythonPythonPython

# num = int(input("Enter your num: "))
# language = input("Enter your language: ")
# print(language*num)


# N. Write a program that asks user for any sentence. The program should
# replace all characters in the sentence with its capitalized form.
# Given "I love the Python", the program should give us:
# I LOVE THE PYTHON

# sentence = input("Enter your sentence: ")
# print(sentence.upper())


#O. Write a program that asks user for any sentence. The program should
# replace all 'a' character in the sentence with 'o'. Given "Today is a
# great day!", the program should give us:
# Todoy is o greot doy!

# sentence = input("Enter your sentence: ")
# print(sentence.replace("a", "o"))


# P. Write a program that asks user for any input. The program should
# print 'True' if all characters in the input are lower characters.
# word = input("Enter your word: ")
# print(bool(word.islower()))


#Q. Write a program that asks user for any input. The program should
# print 'True' if all characters in the input are digits.

# isdigit = input("Enter your isdigit: ")
# print(bool(isdigit.isdigit()))


#R. Write a program that asks user for any phrase. The program should also
# ask for the amount the phrase will be printed. Depending on that amount print
# the user's phrase to terminal output.:

# expression = input("Enter your expression: ")
# number = int(input("Enter your number: "))
# print(expression*number)


# S. Write a program that asks user for any amount. Depending on that amount you
# should print the stars before and after the 'Hello world' phrase. Example:
# (Amount is 3)
# *** Hello world ***
# symbol = input("Enter your symbol: ")
# word = input("Enter your word: ")
# print(symbol+ word+symbol)



#Chat GPT's Homework:
#Task 1. Create a Python program that greets the user and asks for their name. 
# Use the input() function to receive the user's input and then print a personalized greeting.

# name = input("Enter your name: ")
# word = input("Enter your word: ")
# print(word,name)


#Task 2. Extend the program from Task 1 to ask the user for their birth year and 
# calculate their age. Display a message that includes their name and age.

# name = input("Enter your name: ")
# word = input("Enter your word: ")
# birth_day = int(input("Enter your birthday: "))
# now_year = int(input("Enter your now year"))
# different = now_year - birth_day
# print(f"My name is {name} I am word {word}. I am {different} years old")



#Task 3. Write a program that takes two numbers as input from the user and performs 
# the following math operations:
# A. Addition
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# addition = first + second
# print(addition)

# B. Subtraction
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# subtraction = first - second
# print(subtraction)
# C. Multiplication
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# multiplication = first * second
# print(multiplication)

# D. Division
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# division = first / second
# print(division)



#Task 4. Create a program that calculates the area of a triangle.
# Ask the user for the necessary inputs for calculations. 

# a = 2
# b = 3
# c = 4

# sum_triagle = (a+b+c) / 2
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))
# area = (sum_triagle*(sum_triagle-a)* (sum_triagle-b)* (sum_triagle-c)) ** 0.5
# print("Triangle area is:", area)



#Task 5. Create a program that calculates the area of a rectangle.
# Ask the user for the necessary inputs for calculations. 
# width = float(input("Enter width: "))
# height = float(input("Enter height: "))
# area = width * height
# print("Area of rectangle=", area)



#Task 6. Create a program that calculates the area of a square.
# Ask the user for the necessary inputs for calculations. 
# num = int(input("Enter your number: "))
# second = int(input("Second: "))
# square = num ** second
# print(square)


#Task 7 (Extra!). For an extra challenge, implement a unit conversion feature. 
# Ask the user for a distance in meters and convert it to feet and inches. 
# There are approximately 3.28084 feet in a meter and 39.3701 inches in a meter. 
# Display the converted distances.
# print("This program will convert a height given meters to a height given in feet and inches. ")
# meter = float(input("Enter height in meter: "))
# meters = meter // .3048
# meters_in = meters % 12
# print("The height is", meters_in, "feet and", meters_in, "inches")



#Quiz:
#1.Which of the following functions is used to convert a value to an integer in Python?
#a)int()


#2.When using the input() function in Python, what data type is the input value 
# stored as by default?
#c)str


#3.You want to find out how many characters are in a user-inputted sentence. 
# Which Python function would you use?
#c)len()



#4.If a user enters "3.14159" as input using the input() function, how can you 
# convert it to a floating-point number?
#a)float(input())



#5.If a user enters "5.7" as input using the input() function and you use 
# int(input()) for conversion, what will happen?
#a)An error will occur since int() cannot handle decimal values.


#6.You want to display the length of a user-inputted string "Hello, World!" with a 
# descriptive message. Which option achieves this?
#a)print("The length of the input is:", len(input()))



#7.What happens if a user enters "42" as input and you use float(input()) for 
# conversion?:
#b)The value is converted to the floating-point number 42.0.


#8.To style the user prompt and concatenate it with a variable, which option is correct?:
#c)input("Enter your name: ") .format(name)



#Integers :
#A.Create a variable called 'speed'.Assign any integer value between 60 and 80 to it:
# speed = 80
#B.Create a variable called 'limit'.Assign any integer value between 90 and 100 to it:
# limit = 109
#C.Create a variable 'difference'.Make it equal the difference between the 'limit' and the 'speed' variable.Print the 'difference' variable:
# difference = limit - speed
# print(difference)


#D. Create a variable called 'amount'. Assign any integer value between 5 and 20 to it.
# amount = 20
#E.Create a variable called 'double_amount'.Make it equal the double value of the 'amount' variable:
# double_amount = amount * 2
# print(double_amount)


#F. Create a varaible called 'triple_amount'. Make it equal the triple value of the 'amount'
# variable. Print these variables (amount, double_amount, triple_amount) separately.
# triple = amount * 3
# print(amount, double_amount, triple)



#G. Create a variable called 'distance'. Assign any integer value between 500 and 2000 to it.:
# distance = 2000
#H.Create a variable called 'passed_distance'.Assign an integer value between 100 and 500 to it:
# passed_distance = 500
#I.Print the difference between the 'distance' variable and the 'passed_distance'variable:
# different = distance - passed_distance
# print(different)


#J. Create a variable called 'number_one'. Give it any integer value.:

# number_one = 5
#K.Create a variable called 'number_two'. Give it any integer value.:
# number_two = 10
#L. Create a variable called 'number_three'. Make it equal to the sum of 'number_one' and 'number_two'.:
# number_three = number_one + number_two
# print(number_three)


#M.Create a variable called 'a' Make it equal 15:
# a = 15
#N.Create a variable called 'b'. Make it equal 35:
# b = 35

#O.Create a variable called 'c'.Make it equal 20:
# c = 20
#P.Create a variable called 'result'.Make it equal the sum of 'a' and 'b' minus 'c'. Print its value:
# result = a + b + c
# print(result)


#Q. Create a variable called 'my_number'. Make it equal 4.:
# my_number = 4
#R.Print 'my_number's raised to the third power value:
# print(pow(my_number, 3))


#Floats:
#A.Create a variable called 'temperature'. Make it equal any float number:
# temperature = 20.5

#B.Create a variable called 'weight'.Make it equal any float number:
# weight = 50.5

#C.Create a variable called 'length'.Make it equal any float number:
# length = 30.5

#D.Create a variable on your own.(name it appropriately).Make it equal any float number:
# height = 40.5

#E.Print all those variables from Task A to D:
# print(temperature)
# print(weight)
# print(length)
# print(height)


#F.Create a variable called 'x'.Make it equal any float number between 1 and 2 with 2 decimal points:
# x = 1.50

#G.Create a variable called 'double_x'. Make it equal double-value of 'x':
# double_x = x * 2
# print(double_x)

#H.Print all those variables from Task F to G:
# print(x)
# print(double_x)


#I.Make your best and create a hard task by your own using floats:
# try:
#     number = float(input("Enter your number: "))
#     num = float(input("Enter your num: "))
#     device = number / num
#     print(device)
# except ZeroDivisionError:
#     print("No zero division")



#Built-in functions:
#A.Create a variable called 'long_sentence'.Make it equal a long sentence. Print 'long_sentence's length:
# long_sentences = "Hello. My name is eldar"
# print(len(long_sentences))


#B. Create a variable called 'accurate_number'.
# Make it equal any float number between 10 and 11 with 5 decimal points
# Print this variable.
# number = 10.12345
# print(number)


#C. Create a variable called 'rounded_accurate_number'.
# Make it equal the 'accurate_number's value rounded to 2 decimal points.
# Print this variable.
# rounded = round(number, 2)
# print(rounded)


#D. Override 'rounded_accurate_number' variable.
# Make it equal the 'accurate_number's value rounded to 3 decimal points.
# Print this variable.

# rounded_accurate_number = round(12.1234, 3)
# print(rounded_accurate_number)


#E. Using 'round' method round 175233, so it gives us 175000.
# number = 175233
# rounded = round(number, -3)
# print(rounded)


#Math module:
#A.Find the 'math' module's method by its definition:
#1.The _sqrt__ method returns the square root of a number
#2.The pow method returns the value of x raised to power y
#3.The floor method rounds a number UP to the nearest integer , if necessary, and returns the result
#4.The ceil method rounds a number Down to the nearest integer, if necessary and returns the result:


#B. Round π (Pi) to two decimal places.:
# import math
# print(round(math.pi, 2))


#C.The area of a square is 700 square units. Find the side of that square:
# area = 700
# side = area ** 2
# print(side)


#D.One side of a rectangle is 5 units longer than other side.Find the area of rectangle, if the perimeter is 100 units:
# perimeter = 100
# side = 5
# device_perimeter = perimeter / side
# print(device_perimeter)


#E. Round 5.7 down to the nearest integer.
# print(round(5.7, -1))

#F.Round 5.7 up to the nearest integer:
# print(round(5.7))


#Expressions:
#Simplify these expressions:
# A. (5 * 5 + 5 // (5 + 5 % 5) // 5) + 5**5 + 5 - 5**0
# B. (20 + 30 * (15 - 7) // (3 + 4 % 2) + 10**2 // 5) + 2**6 + 50 - 3**1
# C. (70 - 25 + 3 * (8 + 4) // (6 + 9 % 3) + 15**2 // 7) + 4**3 + 90 - 2**4

# A = (5*5+5) // (5+5%5) // 5+5**5-5**0
# print(A)

# B = 20+30*(15-7) // (3+4%2) + 10**2 // 5+(2**6) + (50-3**1)
# print(B)

# C = 70-25+3*(8+4) // (6+9%3) + 15**2//7 + 4**3 + (90-2**4)
# print(C)




#- Chat GPT's Homework - 
# Task 1. Mixed Operations and Variable Naming
# Solve the following mixed arithmetic expressions, using appropriate variable names:
# a) Calculate the perimeter of a square with side length 6 units.
# square = 6 ** 2
# print(square)
# b) You have $150. If you spend $47.25 and then receive $30.50, how much money do you have left?
# dollar = 150-47.25+30,50
# print("$", dollar)
# c) A train is moving at a speed of 80 km/h. How far will it travel in 1.5 hours?
# train = 80-1.5
# print(train)




#Task 2. Float Operations
# Perform the following floating-point operations and round the answers to two decimal places:
# a. 4.25 + 2.68
# a = 4.25+2.68
# print(round(a, 2))
# b. 9.75 - 3.85
# b = 9.75 - 3.85
# print(round(b, 2))
# c. 3.5 x 1.2
# c = 3.5 * 1.2
# print(round(c, 2))
# d. 7.8 / 2.5
# d = 7.8 / 2.5
# print(round(d, 2))



#Task 3. Accessing the Value of π (Pi)
# A. Use the math.pi attribute to access the value of π (Pi) and store it in a variable.:
# import math
# pi = math.pi
# print(pi)
# B. Calculate and print the circumference of a circle with a radius of 7 units using 
# the π value from the math.pi attribute.
# print(round(pi, 7))



#Task 4. Using 'sqrt' Method
# A. Calculate and print the square root of 16 using the math.sqrt() method.
# import math
# print(math.sqrt(16))
# B. Calculate and print the square root of 25 using the math.sqrt() method.
# import math
# print(math.sqrt(25))
# C. Calculate and print the square root of 10 using the math.sqrt() method.
# import math
# print(math.sqrt(10))


# Task 5. Using 'pow' Method
# A. Calculate and print the result of raising 2 to the power of 5 using the math.pow() method.
# print(pow(5,2))
# B. Calculate and print the result of raising 3 to the power of 4 using the math.pow() method.
# print(pow(3,4))


# Task 6. Use the math.ceil() method to round the following numbers up to the nearest integer:
# a. 6.1
# import math
# a = 6.1
# print(math.ceil(a))
# b = 10.9
# print(math.ceil(b))
# c. -2.3
# c = -2.3
# print(math.ceil(c))



#Task 7. Use the math.floor() method to round the following numbers down to the nearest integer:
# a. 4.7
# import math
# a = 4.7
# print(math.floor(a))
# b. 9.2
# b = 9.2
# print(math.floor(b))
# c. -3.8
# c = -3.8
# print(math.floor(c))



#Quiz:
#1. Which of the following is a comparison operator in Python?:
#c)==


#2. What is the result of 15.5 - 7.2 rounded to two decimal places?:
#a)8.3


#3. What is the result of 1.5 - 1.0 rounded to two decimal places?:
#d)-0.5


#4.If 'a = 12' and 'b = 7', which expressions are True?:
#b) a > b


#5.What is the value of 20/4?:
#d)5.0


#6.Which of the following are integers?:
#b)-15


# 7.What is the absolute value of -25?
#a)25


#8. If 'x = 5' and 'y = 8', what is the value of x^y (x raised to power of y)?:
#a)13


#9.What does the math module in Python provide?:
#b) Functions for working with complex numbers.



#10.Given the equation 3 x 8 - 5, what is the correct result?:
#a)19


#11.What is the result of 17 + 23?:
#b)40


#12.What is the result of "17" + "23"?:
#d)"1723"


# Note. All tasks should be written as in the following example (you can
# use variable naming method or adding a comment after the expression):
#A.
# expression = True and False or True
# step_one = (True and False) or (True)
# step_two = (False) or (True)
# step_three = True
# print(step_three == expression)


#At the end, your program should only print 'True's, so that will mean
# you have accomplished and simplified all expressions correctly.


#Booleans-:
#Simplify these expressions:
#A.True or False and True -> True
#B.False and False or False -> False
#C.(True or False) and True -> True
#D.True or(True or False and True) and True -> True
#E.False or False and False and not False->False
#F.(True or True or False) and True -> True
#G.False or (True and False) -> False
#H.False and False and False and False and False or True and False ->False
#I.True or False or True->True
#J.False or(not False) -> True
#K.not True or not False->True
#L.False and not False or not False->True
#M.True or not False and True or not not True->True
#N.not not not  False->True
#O. not N(previous task N's value)->False

#P. True or False and not True or (not True and False) and not True or False->True
#Q. True or not False or not True or True->True
#R. False and (not True or False or (False or not True and True or False)) and True->False
#S. False and not not not True and (False or True or not False) and True or False->False
#T.not(True or False) or not False or(True and False or False) ->True
#U.(True or not not False) and (True or(True or(False)))->True
#V. False and False or (not False and (not False))->True
#W. (not True or not False) and (not True or (not False))->True
#X. False or False and not True or not False and (not True and False)->False
#Y. True and True and True and True and not True and True and True or False->False
#Z.False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True)->False
