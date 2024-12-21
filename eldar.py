#1."Hello, World!" metnini ekrana cap edin:
# print("Hello World!")

#2.Istifadeciden adini daxil etmesini isteyin ve onu salamlayin:
# name = input("Enter your name: ") 
# print(f"Hello {name}")

#3.Iki ededi toplayib ekrana cap edin:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# sum_number = first + second
# print(sum_number)


#4.Dairenin radiusunu istifadeciden alin ve sahesini hesablayin:
# from math import pi
# radius = float(input("Enter your circle radius: "))
# area = pi * radius ** 2
# print("The area of the circle with radius "+ str(radius) + "is: " + str(area))



#5.Iki ededin ededi ortasini tapin:
# first = 5
# second = 10
# different = (first + second) / 2
# print(different)



#6.Verilmis siyahi icinde butun cutleri tapib cap edin:
# number = [1,2,3,4,5,6,7,8,9]
# for num in number:
#     if num % 2 == 0:
#         print(num)


#7.Istifadeciden eded alin ve o ededin kvadratini hesablayib cap edin:
# import math
# number = int(input("Enter your number: "))
# sqrt = math.sqrt(number)
# print(f"Sqrt =", sqrt)



#8.0-dan 10 -a qeder butun ededleri ekrana cap edin (for dongusu ile).
# for x in range(11):
#     print(x)


#9.Istifadeciden 3 eded alin ve onlarin en boyuyunu tapib cap edin:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# third = int(input("Enter your third number: "))

# if first > second:
#     print(f"First number is the biggest =", first)
# elif second > third:
#     print(f"Second number is the biggest =", second)
# else:
#     print(f"Third number is the biggest= ", third)



#10.Istifadeciden temperaturu Celsius skalasinda daxil etmesini daxil etmesini isteyin ve onu Fahreneit skalasina cevirib cap edin:
# celsius = float(input("Enter your celsius: "))
# fahreneit = celsius * (9/5) + 32
# print(f"Fahreneit is=", fahreneit)



#11.Istifadeciden bir eded alin ve onun musbet, menfi , yoxsa sifir oldugunu cap edin:
# number = int(input("Enter your number: "))
# if number > 0:
#     print(f"Positive number=", number)
# elif number < 0:
#     print(f"Negative number is=", number)
# else:
#     print(f"Zero is equal=", number)



#12.1-den 20 -e qeder olan butun tek ededleri ekrana cap edin:
# for x in range(21):
#     if x % 3 == 0:
#         print(x)


#13.Bir siyahi icindeki butun ededlerin hasilini tapin:
# number = [1,2,3,4]
# print(number * 2)


#14.Istifadeciden iki tarix daxil etmesini isteyin (gun, ay, il) ve bu tarixler arasindaki ferqin nece gun oldugunu tapin:
# day =int(input("Enter your day: "))
# month = int(input("Enter your month: "))
# year = int(input("Enter your year: "))

# day1 = int(input("Day: "))
# month1 = int(input("Month: "))
# year1 = int(input("Year: "))

# difference = day - day1, month- month1, year-year1
# print(difference)

#15.1000-den kicik olan 3 ve ya 5-e bolunen butun ededlerin cemini tapin:
# total = 0
# for x in range(1001): 
#     if x % 3 == 0 or x % 5 == 0:
#       total +=x

# print(total)
# print(x)



#16.Ededi reqemlere ayiraraq cap edin (meselen: 12345 -> 1 2 3 4 5):
# number = 12345
# digits = [int(digit) for digit in str(number)]
# print(digits) 


#17.1-den 10-a qeder olan ededlerin kvadratlarini bir siyahi icinde saxlayin ve siyahini cap edin:
# import math
# result = []
# for x in range(11):
#     a = math.sqrt(x)
#     result.append(a)
#     print(result)



#18.Istifadeciden bir metn daxil etmesini isteyin ve icindeki boyuk herflerin sayini tapin:
# sentence = input("Enter your sentence: ")
# count = sum(1 for x in sentence if x.isupper())
# print(count)



#19.Iki ededi muqayise ederek onlarin beraber olub-olmadigini cap edin:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# if first > second:
#     print(f"First number is the biggest=", first)
# elif second> first:
#     print(f"Second number is the biggest=", second)
# else:
#     print("First number and Second number is equal")



#20.Ededin tek ve ya cut oldugunu yoxlayan funksiya yazin:
# number = int(input("Enter your number: "))
# if number % 2 == 0:
#     print(f"Even number=", number)
# else:
#     print(f"Odd number=", number)



#21.Istifadeciden bir eded alin ve onun reqemlerinin cemini tapin:
# num = int(input("Enter your number: "))
# sum_number = num + num
# print(sum_number)


#22.Istifadeciden bir metn daxil etmesini isteyin ve ondaki bosluqlarin sayini tapin:
# sentence = input("Enter your sentence: ")
# spice = sentence.count(" ")
# print(spice)



#23.Bir siyahidaki minimal ve maksimal ededleri tapin:
# number = [4,1,9,2,6,5]
# print(max(number))
# print(min(number))



#24.1-den 100-e qeder olan ededlerden yalniz 3-e bolunen ededleri cap edin:
# for x in range(101):
#     if x % 3 == 0:
#         print(x)



#25.Bir siyahi icinde tekrar olan ededleri tapin:
# import collections

# list_number = [1,2,3,2,3,4,5,6,7]
# counter = collections.Counter(list_number)
# print(counter)



#26.Istifadeciden 3 eded alin ve onlarin ededi ortasini tapin:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# third = int(input("Enter your third number: "))
# different = (first+ second+third) /3 
# print(different)



#27.1-den 10-a qeder olan ededleri azalan sira ile cap edin:
# for x in range(10, 0,-1):
#     print(x)



#28.Verilmis siyahi icindeki butun cut ededlerin sayini tapin:
# even_list = [1,2,3,4,5,6,7,8,9]
# count = 0
# for num in even_list:
#     if num % 2 == 0:
#         count +=1


# print("Even number is:", count)



#29.Istifadeciden bir metn daxil etmesini isteyin ve icindeki kicik herflerin sayini tapin:
# sentence = input("Enter your sentence: ")
# count = sum(1 for x in sentence if x.islower())
# print(count)



#30.1-den 10-e qeder olan ededleri toplayin ve neticeni cap edin:
# count = 0
# for x in range(11):
#     count +=x


# print(count)



#31.Bir sira icindeki butun elementleri cap edin:
# fruit = ["apple", "banana", "cherry"]
# print(fruit)


#32.Istifadeciden bir eded alin ve onun menfi, sifir,yoxsa musbet oldugunu cap edin:
# number = int(input("Enter your number: "))
# if number>0:
#     print("Positive number: ", number)
# elif number<0:
#     print("Negative number:", number)
# else:
#     print("Zero is equal:", number)



#33.Bir siyahidaki butun tek ededleri silin:
# number_list = [1,2,3,4,5,6,7,8,9]
# new_list = []
# for num in number_list:
#     if num % 2== 0:
#         new_list.append(num)


# print(new_list)


#34.1-den 50-ye qeder olan ededlerden yalniz 5-e ve 7-ye bolunen ededleri cap edin:
# for x in range(51):
#     if x % 3 == 0 and x%5 == 0:
#         print(x)



#35.Istifadeciden bir eded alin ve onun kvadrat kokunu tapib cap edin:
# import math
# number = int(input("Enter your number: "))
# square = math.sqrt(number)
# print(square)



#36.Bir siyahidaki tek ededlerin sayini tapin:
# num_list = [1,2,3,4,5,6,7,8,9]
# count = 0
# for num in num_list:
#     if num % 3 == 0:
#         count +=1

# print("Odd number:", count)



#37.Bir sozun icindeki unikal herfleri cap edin:
# word = "anana"
# unical = set(word)
# print(unical)


#38.Ededi reqemlere ayirin ve onlarin en boyuyunu tapin (meselen: 5813 -> 8).
# number = 5813
# if number > 0:
#  digits = [int(digit) for digit in str(number)]
# print(digits) 


#39.Istifadeciden bir eded alin ve onun 4-e bolunub-bolunmediyini yoxlayin:
# number = int(input("Enter your number: "))
# if number % 4== 0:
#     print(number)
# else:
#     print("No number:", number)



#40.Iki ededi muqayise ederek onlardan hansinin boyuk oldugunu cap edin:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# if first>second:
#     print(f"First number is the biggest=", first)
# elif second>first:
#     print(f"Second number is the biggest=", second)
# else:
#     print("No number")


#41.Istifadeciden yasini daxil etmesini isteyin ve onun yetkin olub-olmadigini (18 yas ve yuxari) yoxlayin:
# age = int(input("Enter your age: "))
# if age > 18:
#     print(f"Teenager=",age)
# elif age == 18:
#     print(f"Middle adolescence=", age)
# else:
#     print(f"No teenager=",age)



#42.Istifadeciden bir metn daxil etmesini isteyin ve icindeki simvollarin sayini tapin:
# sentence = input("Enter your sentence: ")
# len_sentence = len(sentence)
# print(len_sentence)


#43.Bir siyahida olan butun ededlerin ortalamasini tapin:
# number = [4,7,8,5,10]
# numerical_average = sum(number) / len(number)
# print("Average:", numerical_average)



#44.1-den 100-e qeder olan butun ededlerin cemini tapin:
# count = 1
# for x in range(101):
#     count+=x


# print(x)


#45.Bir siyahida tekrar olmayan elementleri tapin:
# from collections import Counter
# number = [1,2,3,2,3,4,5,6,7]
# element = Counter(number)
# unical = [elem for elem ,count in element.items() if count == 1]
# print(unical)

#46.Istifadeciden bir eded alin ve onun faktorialini hesablayin:
# number = int(input("Enter your number: "))
# fact = int(input("Enter your factorial number: "))
# for i in range(1, number+1):
#     fact = fact * i
#     print("The factorial number is:", end="")
#     print(fact)



#47.1-den 10 a qeder olan ededlerin hasilini tapin:
# n = 10
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         print(f"{i *j:3}", end=" ")
#         print()



#48.Istifadeciden bir setir tipli reqemler daxil etmesini isteyin (meselen, "1 3 5") ve onlarin ortalamasini tapin:
# num = "1 3 5"
# numbers = [int(n) for n  in num.split()]
# total = sum(numbers)
# count = len(numbers)
# average = total/count
# print("Average:", average)



#49.Istifadeciden bir metn ve bir herf daxil etmesini isteyin ve bu herfin metnde nece defe tekrarlandigini tapin:
# sentence = input("Enter your sentence: ")
# letter = input("Enter your letter: ")
# print(sentence.count(letter))


#50.0-dan 100 -e qeder olan butun cut ededleri cap edin:
# for num in range(101):
#     if num % 2 == 0:
#         print(num)



#51.Bir siyahi icindeki ededleri azalan sira ile cap edin:
# number = [1,3,4,5,2]
# sort = sorted(number, reverse=True)
# print(sort)



#52.Bir siyahinin icindeki tekrar olan elementleri silin:
# lst = [1,2,2,3,4,5,6,7]
# x = set(lst)
# print(x)


#53.1-den 100-e qeder olan ededlerden yalniz 4-e ve 6-ya bolunen ededleri cap edin:
# for number in range(101):
#     if number % 4 == 0 and number % 6 == 0:
#         print(number)


#54.Istifadeciden bir metn daxil etmesini isteyin ve icindeki sait herflerin sayini tapin:
# sentence = input("Enter your sentence: ")
# viwel = input("Enter your viwel: ")
# print(sentence.count(viwel))


#55.Bir siyahi icindeki maksimal ve minimal ededin ferqini tapin: 
# number = [4,1,9,2,6,5]
# print(max(number)- min(number))


#56.Istifadeciden bir eded alin ve onun murekkeb olub olmadigini yoxlayin:?


#64.Bir siyahida olan butun cut ededleri silin:
# even = [2,4,5,6,1,2,8,9]
# for num in even:
#     if num % 3 == 0:
#         print(num)



#65.Istifadeciden bir eded alin ve onun murekkeb eded olub-olmadigini yoxlayin:?



#66.Istifadeciden iki eded alin ve onlarin boyuk ortaqlarini tapin:
# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))

# while second !=0:
#     r = first % second
#     first = second
#     second = r

# print(f"The greatest common divisor of {first} and {second} is: {first}")



#67.1-den 20-ye qeder olan ededlerin kvadrat kokunu cap edin:
# import math
# for x in range(21):
#     print(x)
#     sqrt = math.sqrt(x)

# print(f"The square root of {x} is: {sqrt}")



#68.Istifadeciden bir eded alin ve onun 10-a qeder olan butun boyuklerini cap edin:
# number = int(input("Enter your number: "))
# for x in range(number, 10):
#     print(x)



#69.Iki ededin en kicik ortagini tapin:
# first  = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# a, b = first, second
# while b !=0:
#     a,b = b,a % b
#     lcm = (first * second) //a


# print(f"The least common multiple of {first} and {second} is: {lcm}")



#70.Istifadeciden bir metn daxil etmesini isteyin ve onu tam boyuk herflerle cap edin:
# sentence = input("Enter your sentence: ")
# print(sentence)
# print(sentence.upper())



#71.Bir siyahidaki tek indekslerde yerlesen elementleri cap edin:
# letter = ["a", "b", "c", "d", "e"]
# print(letter[1])
# print(letter[3])



#72.Istifadeciden bir eded alin ve onun musbet tek bolenlerini cap edin:?


#73.0-dan 100-e qeder olan ededlerden yalniz 2-e ve 3-e bolunen ededleri cap edin:
# for x in range(101):
#     if x % 2 == 0 and x % 3 == 0:
#         print(x)



#74.Bir siyahinin icindeki tekrar olan elementlerin sayini tapin:
# my_list = [1,2,3,2,4,5,5,6,1]
# duplicates = [item for item in set(my_list) if my_list.count(item) > 1]
# print("Duplicates:", duplicates)



#75.Istifadeciden bir metn daxil etmesini isteyin ve icindeki reqemleri cap edin:
# text = input("Enter your text: ")
# numbers = [char for char in text if char.isdigit()]
# print("The digits in the entered text are:", ''.join(numbers))



#76.1-den 20-e qeder olan ededlerin kublarini cap edin:
# for x in range(21):
#     cube = x ** 3

# print(f"{x} number cube: {cube}")



#77.?