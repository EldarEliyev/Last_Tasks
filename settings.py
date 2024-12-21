# Python Basic(Part-1) [150 Exercises with Solution]
#150. Odd Product Pair Checker:
# def odd_product(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
# #             if i != j:
#                 product = nums[i] * nums[j]
#                 if product & 1:
#                     return True
#                 return False

# dt1 = [2,4,6,8]
# dt2 = [1,6,4,7,8]
# dt3 = [1,3,5,7,9]
# print(dt1, odd_product(dt1))
# print(dt2, odd_product(dt2))
# print(dt3, odd_product(dt3))




#149.Cube Sum of Smaller Integers:
# def sum_of_cubes(n):
#     n -=1
#     total = 0
#     while n>0:
#         total += n*n*n
#         n-=1
#         return total
   
# print("Sum of cubes smaller than the specified number:", sum_of_cubes(3))




#148.Max and Min Without Built-ins:
# def max_min(data):
#     l = data[0]
#     s = data[0]
    
#     for num in data:
#         if num > l:
#             l = num
#         elif num < s:
#             s = num
            
#             return l,s
        
# print(max_min([0,10,15,40,-5,42,17,28,75]))



#147. Divisibility Tester:
# def multiple(m,n):
#     return True if m % n == 0 else False

# print(multiple(20,5))
# print(multiple(7,2))



#145.Check List, Tuple, or Set:
# x = ('tuple', False, 3.2,1)
# if type(x) is list:
#     print('x is a list')
# elif type(x) is set:
#     print('x is a set')
# elif type(x) is tuple:
#     print('x is a tuple')
# else:
#     print('Neither a list nor a set nor a tuple.')
    


#144.Variable Type Checker:
# print(isinstance(25, int) or isinstance(25,str))
# print(isinstance([25], int) or isinstance([25], str))
# print(isinstance("25", int) or isinstance("25", str))


#143. Shell Bit Mode Detector:
# import struct
# print(struct.calcsize("P")*8)



#142. Consecutive Zero-One Checker:
# def test(str1):
#     while '01' in str1:
#         str1 = str1.replace('01', '')
#         return len(str1) == 0
    
# str1 = "01010101"
# print("Oroginal sequence:", str1)
# print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
# print(test(str1))

# # Repeat the same process for other test cases.
# str1 = "00"
# print("\nOriginal sequence:", str1)
# print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
# print(test(str1))
# str1 = "000111000111"
# print("\nOriginal sequence:", str1)
# print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
# print(test(str1))
# str1 = "00011100011"
# print("\nOriginal sequence:", str1)
# print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
# print(test(str1))



#141. Decimal to Hexadecimal:
# x = 30
# print(format(x, '02x'))
# x = 4
# print(format(x, '02x'))



#140. Binary with Leading Zeroes:
# x = 12
# print(format(x, '08b'))
# print(format(x, '010b'))



#139.IP Address Validator:
# import socket
# addr = '127.0.0.2561'
# try:
#     socket.inet_aton(addr)
#     print("Valid IP")
# except socket.error:
#     print('Invalid IP')

    
    
#138. Boolean to Integer Converter:
# x = 'true'
# x = int(x == 'true')
# print(x)
# x = 'abcd'
# x = int(x == 'true')
# print(x)



#137.Extract Dictionary Pair:
# d = {'Red': 'Green'}
# (c1, c2), = d.items()
# print(c1)
# print(c2)



#135.Print Variable Without Spaces:
# x = 30
# formatted_string = 'Value of x is "{}"'.format(x)
# print(formatted_string)



#134.Input Two Integers:
# print("Inpit the value of x & y")
# x, y = map(int, input().split())
# print("The value of x & y are:", x,y)

# a,b = [int(a) for a in input("Input the value of a & b:").split()]
# print("The value of a & b are:", a,b)



#133.Program Runtime Calculator:
# from timeit import default_timer
# def timer(n):
#     start = default_timer()
    
#     for row in range(0,n):
#         print(row)
        
#         print(default_timer()- start)
        
# timer(5)
# timer(15)



#132.List Home Directory:
# import os.path
# print(os.path.expanduser('~'))



#131. Split Variable Length String:
# var_list = ['a', 'b', 'c']
# x,y,z = (var_list+ [None]*3 )[:3]
# print(x,y,z)
# var_list = [100,20.25]
# x,y = (var_list+ [None]*2)[:2]
# print(x,y)



#130.Double Quotes String Display:
# import json
# data = {'Alex': 1, 'Suresh': 2, 'Agnessa': 3}
# json_string = json.dumps(data)
# print(json_string)


#129.Add Leading Zeroes:
# str1 = '122.22'
# print("Original String:", str1)
# print("\nAdded trailing zeros:")
# str1 = str1.ljust(8, '0')
# print(str1)
# str1 = str1.ljust(10, '0')
# print(str1)

# print("\nAdded leading zeros:")
# str1 = '122.22'
# str1 = str1.rjust(10,'0')
# print(str1)



#128.Lowercase Letters Checker:
# str1 = 'A8238i823acdeOUEI'
# print(any(c.islower() for c in str1))


#127.Integer Fits in 64 Bits:
# int_val = 30
# if int_val.bit_length() <= 63:
#     print((-2**63).bit_length())



#126.Get Module Object:
# from inspect import getmodule
# from math import sqrt
# print(getmodule(sqrt))



#125.Sum Collection Counts:
# import collections
# num = [2,2,4,6,6,8,6,10,4]
# result = sum(collections.Counter(num).values())
# print(result)



#124.Variable Equality Checker:
# x = 20
# y = 20
# z = 20
# if x == y == z == 20:
#     print("All variables have the same value!")



#123.Max and Min of Number Types:
# import sys
# print("Float value information:", sys.float_info)
# print("\nInteger value information:", sys.int_info)
# print("\nMaximum size of an integer:", sys.maxsize)



#122.Empty Variable Without Deletion:
# n = 20
# d = {"x": 200}
# l = [1,3,5]
# t = (5,7,8)
# print(type(n)())

# print(type(d)())
# print(type(l)())
# print(type(t)())



#121.Variable Defined Checker:
# try:
#     x = 1
# except NameError:
#     print("Variable is not defined.....!")
# else:
#     print("Variable is defined.")
    

# try:
#     y
# except NameError:
#     print('Variable is not defined....!')
# else:
#     print('Variable is defined.')



#120.String Formatter with Length Limit:
# str_num = "1234567890"
# print("Original string:", str_num)
# print('%6s' % str_num)
# print('%9s' % str_num)
# print('%10s' % str_num)



#119. Round Float to Decimals:
# order_amt = 212.374
# print('\nThe total order amount comes to %f' % order_amt)
# print('The total order amount comes to %.2f' % order_amt)
# print()



#118.Create Bytearray from List:
# print()
# nums = [10,20,56,35,17,99]
# values = bytearray(nums)
# for x in values:
#     print(x)
    
# print()



#117.String Memory Location Test:
# str1 = "Python"
# str2 = "Python"
# print("\nMemory location of str1 =", hex(id(str1)))
# print("\nMemory location of str2 =", hex(id(str2)))



#116.Print Unicode Characters:
# str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
# print()
# print(str)
# print()



#115. List Product Calculator:
# from functools import reduce
# nums = [10,20,30]
# print("Original list numbers:")
# print(nums)
# nums_product = reduce((lambda x, y: x * y), nums)
# print("\nProduct of the said numbers (without using a for loop):", nums_product)



#114. Filter Positive Numbers:
# nums = [34,1,0,-23,12,-88]
# print("Original numbers in the list:", nums)
# new_nums = list(filter(lambda x: x>0, nums))
# print("Positive numbers in the said list:", new_nums)


#113.Number Input Validator:
# while True:
#     try:
#         a = int(input("Input a number: "))
#         break
#     except ValueError:
#         print("\nThis is not a number.Try again...")
#         print()



#112.Remove First List Item:
# color = ["Red", "Black", "Green", "White", "Orange"]
# print("Original list elements:")
# print(color)
# del color[0]
# print("After removing the first color: ")
# print(color)
# print()


#111.Wildcard File Lister:
# import glob
# file_list = glob.glob('*.*')
# print(file_list)
# print(glob.glob('*.py'))
# print(glob.glob('./[0-9].*'))



#110.Divisible by 15 Finder:
# num_list = [45,55,60,37,100,105,220]
# result = list(filter(lambda x: (x % 15 == 0), num_list))
# print("Numbers divisible by 15 are", result)



#109.Resolve Path Name:
# num = float(input("Input a number: "))
# if num > 0:
#     print("It is a positive number")
# elif num == 0:
#     print("It is zero")
# else:
#     print("It is a negative number")
    
    
    
#108.File or Directory Path Finder:
# import os.path
# for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
#     print('File           :', file)

# print('Absolute       :', os.path.isabs(file))
# print('Is File?     :', os.path.isfile(file))
# print('Is Link?     :', os.path.islink(file))
# print('Exists?    :', os.path.exists(file))
# print('Link Exists?:', os.path.lexists(file))



#107.File Properties Retriever:
# import os.path
# import time
# print('File      :', __file__)
# print('Access time :', time.ctime(os.path.getatime(__file__)))
# print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# print('Change time   :', time.ctime(os.path.getctime(__file__)))
# print('Size         :', os.path.getsize(__file__))



#106.Path Extension Splitter:
# import os.path
# for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
#     print('"%s" :' % path, os.path.splitext(path))



#105. User Environment Retriever:
# import os
# print()
# print(os.environ)
# print()



#103.Extract Filename:
# import os
# print()
# print(os.path.basename('/users/system1/student1/homework-1.py'))
# print()



#102.System Command Output:
# import subprocess
# returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
# print('dir command to list files and directories')
# print(returned_text)



#101.URL Content Printer:
# from http.client import HTTPConnection
# conn = HTTPConnection("example.com")
# conn.request("GET", "/")
# result = conn.getresponse()
# contents = result.read()
# print(contents)




#100.Get Host Name:
# import platform
# host_name = platform.uname()[1]
# print("Host name:", host_name)



#99.Clear Terminal:
# import os
# import time
# os.system('ls')
# time.sleep(2)
# os.system('clear')



#98.Get System Time:
# import time
# print()
# print(time.ctime())
# print()



#97.List Special Variables:
# s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
# print()
# print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
# print()



#96.Print Call Stack:
# import traceback
# print()

# def f1():
#     return abc()


# def abc():
#     traceback.print_stack()
    
    
    
# f1()
# print()



#95.Check if String is Numeric:
# str = 'a123'
# try:
#     i = float(str)
# except (ValueError,TypeError):
#     print('\nNot numeric')
    

# print()



#94.String Bytes To Integers:
# x = b'Abc'
# print()
# print("Convert bytes of the said string to a list of integers:")
# print(list(x))
# print()



#93. Object Identity and Type:
# x = 34
# print("\nIdentity: ", x)
# print("\nType: ", type(x))
# print("\nValue: ", id(x))



#92.Special Characters in String:
# print()
# print("\#{'}${\"}@/")

# print(r"""\#{'}${"}@/""")
# print('\#{\'}${"}@/')
# print('\#{'"'"'}${"}@/')
# print(r'''\#{'}${"}@/''')
# print()



#91.Swap Variables:
# a = 30
# b = 20
# print("\nBefore swap a = %d and b = %d" %(a,b))
# a,b = b,a
# print("\nAfter swaping a = %d and b = %d" % (a,b))


#89.Conditional Action:
# n = 1
# if n == 1:
#     print("\nFirst day of a Month!")       
# print()


# n = float(input("Input a number: "))
# if (n == 1):
#     print("First day of a Month!")
# else:
#     print()



#88. Sum Expression Printer:
# x = 30
# y = 20
# print("\n%d+%d=%d" % (x,y, x+y))



#87.File Size Finder:
# import os
# file_size = os.path.getsize("abc.txt")
# print("\nThe size of abc.txt is:", file_size, "Bytes")
# print()



#86.Character ASCII Value:
# print()
# print(ord('a'))
# print(ord('A'))
# print(ord('1'))
# print(ord('@'))
# print()



#85.File or Directory Checker:
# import os
# path = "abc.txt"

# if os.path.isdir(path):
#     print("\nIt is a directory")
    
# elif os.path.isfile(path):
#     print("\nIt is a normal file")
    
# else:
#     print("It is a special file (socket, FIFO, device file)")
    

# print()



#84.Character Frequency Counter:
# s = "The quick brown fox jumps over the lazy dog."
# print("Original string:")
# print(s)
# print("Number of occurrences of 'o' in the said string:")
# print(s.count("o"))


# s = "The quick brown fox jumps over the lazy dog."
# print("Original string:")
# print(s)
# print("Number of occurrences of 'o' in the said string:")
# ctr = 0
# for c in s:
#     if c == 'o':
#         ctr = ctr+1
        

# print(ctr)




#83.List Greater-Than Test:
# num = [2,3,4,5]
# print()
# print(all(x>1 for x in num))
# print(all(x>4 for x in num))
# print()


#82. Sum of Container Items:
# s = sum([10,20,30])
# print("\nSum of the container: ", s)
# print()


# nums = [10,20,30]
# print("Original container:")
# print(nums)
# print(type(nums))
# print("Sum of all items of the said container:", sum(nums))


#81.Concatenate Strings:
# list_of_colors = ['Red', 'White', 'Black']
# colors = '-'.join(list_of_colors)
# print()
# print("All Colors: " + colors)
# print()


#80.Current Recursion Limit:
# import sys
# print()
# print("Current value of the recursion limit:")
# print(sys.getrecursionlimit())
# print()



#79.Object Size Finder:
# import sys
# str1 = "one"
# str2 = "four"
# str3 = "three"
# x = 0
# y  = 112
# z = 122.56
# print("Size of", str1, "=", str(sys.getsizeof(str1))+ "bytes")
# print("Size of ", str2, "=", str(sys.getsizeof(str2))+ "bytes")
# print("Size of ", str3, "=", str(sys.getsizeof(str3))+ "bytes")
# print("Size of", x, "=", str(sys.getsizeof(x))+ "bytes")
# print("Size of", y, "=", str(sys.getsizeof(y))+ "bytes")
# L = [1,2,3, 'Red', 'Black']
# print("Size of ", L, "=", sys.getsizeof(L), "bytes")
# T = ("Red", [8,4,6], (1,2,3))
# print("Size of", T, "=", sys.getsizeof(T), "bytes")
# S = {'apple', 'orange', 'apple', 'pear'}
# print("Size of", S, "=", sys.getsizeof(S), "bytes")
# D = {'Name': 'David', 'Age': 6, 'Class': 'First'}
# print("Size of", D, "=", sys.getsizeof(S), "bytes")



#78.List Built-in Modules:
# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(textwrap.fill(module_name, width=70))



#77. Endianness Checker:
# import sys
# print()
# if sys.byteorder == "little":
#     print("Little-endian platform.")
# else:
#     print("Big-endian platform.")
    
    
# print()


#76.Command-line Arguments:
# import sys
# print("This is the name/path of the script:"), sys.argv[0]
# print("Number of arguments:", len(sys.argv))
# print("Argument List:", str(sys.argv))



#75.Copyright Information:
# import sys
# print("\nPython Copyright Information")
# print(sys.copyright)
# print()


#74. Word Hasher:
# soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]
# word = input("Input the word to be hashed: ")
# word = word.upper()
# coded = word[0]
# for a in word[1:len(word)]:
#     i = 65 - ord(a)
#     coded = coded + str(soundex[i])
    

# print()
# print("The coded word is:" + coded)
# print()



#73.Line Midpoint Calculator:
# print('\nCalculate the midpoint of a line:')
# x1 = float(input("The vale of x (the first endpoint)"))
# y1 = float(input('The value of y (the first endpoint)'))

# x2 = float(input('The value of x (the first endpoint)'))
# y2 = float(input('The value of y (the first endpoint)'))
# x_m_point = (x1+x2)/ 2
# y_m_point = (y1+y2)/2
# print()
# print("The midpoint of the line is :")
# print("The midpoint's value is: ", x_m_point)
# print("The midpoint's value is:", y_m_point)



#72. Math Module Details:
# import math
# math_ls = dir(math)
# print(math_ls)



#71.Directory Listing by Creation Date:
# from stat import S_ISREG, ST_CTIME, ST_MODE
# import os, sys,time
# dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
# data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
# data = ((os.stat(path), path) for path in data)
# data = ((stat[ST_CTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))
# for cdate, path in sorted(data):
#     print(time.ctime(cdate), os.path.basename(path))



#70.Sort Files by Date:
# import glob
# import os
# files = glob.glob("*.txt")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))




#69.Sort Three Numbers:
# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# z = int(input("Input third number: "))

# a1 = min(x,y,z)
# a3 = max(x,y,z)
# a2 = (x+y+z) - a1-a3
# print("Numbers in sorted order: ", a1,a2,a3)



#68.Sum of Digits:
# num = int(input("Input a four-digit number:"))
# x = num // 1000
# x1 = (num- x * 1000) // 100
# x2 = (num-x*1000-x1*100) // 10
# x3 = num - x * 1000 - x1*100-x2*10
# print("The sum of digits in the number is", x+x1+x2+x3)



#67.Pressure Unit Converter:
# kpa = float(input("Input pressure in kilopascals: "))
# psi = kpa / 6.89475729
# mmhg = kpa * 760 / 101.325
# atm = kpa / 101.325
# print("The pressure in pounds per square inch: %.2f psi" % (psi))
# print("The pressure in millimeters of mercury: %.2f mmHg" % (mmhg))
# print("Atmosphere pressure: %.2f atm." % (atm))



#66. BMI Calculator:
# height = float(input("Input your height in Feet: "))
# weight = float(input("Input your weight in Kilograms:"))
# bmi = weight / (height * height)
# rounded_bmi = round(bmi,2)
# print("Your body mass index is:", rounded_bmi)



#65.Seconds to DHMS Converter:
# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# print("d:h:m:s -> %d:%d:%d:%d" % (day, hour, minutes, seconds))



#64. File Timestamps:
# import os.path, time
# print("Last modified: %s " % time.ctime(os.path.getmtime("test.txt")))
# print("Created: %s" % time.ctime(os.path.getctime("test.txt")))



#63.Absolute File Path Finder:
# def absolute_file_path(path_fname):
#     import os
#     return os.path.abspath(path_fname)

# print("Absolute file path: ", absolute_file_path("test.txt"))



#62.Time to Seconds Converter:
# days = int(input("Input days: ")) * 3600 * 24
# hours = int(input("Input hours: ")) * 3600
# minutes = int(input("Input minutes: ")) * 60
# seconds = int(input("Input seconds: "))
# time = days+ hours + minutes + seconds
# print("The amount of seconds: ", time)


#61.Feet to Other Units:
# d_ft = int(input("Input distance in feet: "))

# # Convert the distance in feet to inches and store it in the variable 'd_inches'.
# d_inches = d_ft * 12

# # Convert the distance in feet to yards and store it in the variable 'd_yards'.
# d_yards = d_ft / 3.0

# # Convert the distance in feet to miles and store it in the variable 'd_miles'.
# d_miles = d_ft / 5280.0

# # Print the calculated distances in inches, yards, and miles.
# print("The distance in inches is %i inches." % d_inches)
# print("The distance in yards is %.2f yards." % d_yards)
# print("The distance in miles is %.2f miles." % d_miles)



#60.Triangle Hypotenuse Calculator:
# from math import sqrt
# print("Input lengths of shorter triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))
# c = sqrt(a**2+b**2)
# print("The length of the hypotenuse is:", c)



#59.Height to Centimeters:
# print("Input your height: ")
# h_ft = int(input("Feet: "))
# h_inch = int(input("Inches: "))
# h_inch += h_ft * 12
# h_cm = round(h_inch * 2.54, 1)
# print("Your heigth is: %d cm. " % h_cm)



#58.Sum of First n Positives:
# n = int(input("Input a number: "))
# sum_num = (n * (n+1)) / 2
# print("Sum of the first", n, "positive integers:", sum_num)



#57.Method Execution Time:
# import time

# def sum_of_n_numbers(n):
#     start_time = time.time()   
#     s = 0
#     for i in range(1, n+1):
#         s = s + i
        
#         end_time = time.time()
#         return s, end_time - start_time
    
# n = 5
# print("\nTime to sum of 1 to", n, "and required time to calculate is:", sum_of_n_numbers(n))

    
    
#56.Console Dimensions:
# import fcntl
# import termios
# import struct

# def terminal_size():
#         th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, )))
#         return tw, th
    
# print("Number of columns and Rows: ", terminal_size())

    

#55.Find Local IPs:
# import socket
# local_hostname = socket.gethostname()
# ip_addresses = socket.gethostbyname_ex(local_hostname)[2]
# filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]
# first_ip = filtered_ips[:1]
# print(first_ip[0])



#54.Get Current Username:
# import getpass
# print(getpass.getuser())


#53.Access Environment Variables:
# import os
# print('*-----------------------------*')
# print(os.environ)
# print('*------------------------------------*')
# print(os.environ['HOME'])
# print('*-----------------------------------------*')
# print(os.environ['PATH'])
# print('*----------------------------------*')



#52.Print to STDERR:
# from __future__ import print_function
# import sys
# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)
    
# eprint("abc", "efg", "xyz", sep="--")



#51.Program Profiler:
# import cProfile
# def sum():
#     print(1+2)
    
# cProfile.run('sum()')


#50.Print Without Newline:
# for i in range(0,10):
#     print('*', end="")
    
# print("\n")


#49. Directory Files Lister:
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
# print(files_list)


#48. String to Numeric Parser:
# n = "246.2458"
# print(float(n))
# print(int(float(n)))


#47.CPU Count Finder:
# import multiprocessing
# cpu_count = multiprocessing.cpu_count()
# print(cpu_count)


#46. File Path and Name Finder:
# import os
# print("Current File Name: ", os.path.realpath(__file__))


#45.External Command Runner:
# from subprocess import call
# call(["ls", "-l"])


#44.Python Site Packages Locator:
# import site
# print(site.getsitepackages())


#43.OS and Platform Info:
# import platform
# import os
# print("Name of the OS system:  ", platform.system())
# print("\nVersion of the operating system: ", platform.release())



#42.Shell Mode Detector:
# import struct
# print(struct.calcsize("P")*8)



#41. File Existence Checker:
# import os.path
# print(os.path.isfile('main.txt'))
# print(os.path.isfile('main.py'))



#40.Distance Between Points:
# import math
# p1 = [4,0]
# p2 = [6,6]
# distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
# print(distance)



#39.Future Value Calculator:
# amt = 10000
# int = 3.5
# years = 7
# future_value = amt * ((1+ (0.01 * int))** years)
# print(round(future_value, 2))



#38. Expression Solver:
# x, y = 4,3
# result = x * x +2 *x * y + y*y
# print("({} + {}) ^ 2) = {}".format(x, y, result))


#37.Personal Info Formatter:
# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

# personal_details()


#36.Add Integers Validator:
# def add_numbers(a,b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         return "Inputs must be integers!"
    
#     return a + b

# print(add_numbers(10,20))
# print(add_numbers(10,20.23))
# print(add_numbers('5', 6))
# print(add_numbers('5', '6'))


#35. Equality or 5 Rule Checker:
# def test_number5(x,y):
#     if x == y or abs (x-y) == 5 or (x+y) == 5:
#         return True
#     else:
#         return False
    
# print(test_number5(7,2))
# print(test_number5(3,2))
# print(test_number5(2,2))
# print(test_number5(7,3))
# print(test_number5(27,53))


#34.Conditional Sum to 20:
# def sum(x,y):
#     sum = x + y
#     if sum in range(15,20):
#         return 20
#     else:
#         return sum
    
# print(sum(10,6))
# print(sum(10,2))
# print(sum(10,12))


#33.Triple Sum with Equality Rule:
# def sum_three(x,y,z):
#     if x == y or y == z or x == z:
#         sum = 0
#     else:
#         sum = x + y +z
#         return sum
    
# print(sum_three(2,1,2))
# print(sum_three(3,2,2))
# print(sum_three(2,2,2))
# print(sum_three(1,2,3))



#32.LCM Calculator:
# def lcm(x, y):
#     if x > y:
#         z = x
#     else:
#         z = y
    
#     while True:
#         if (z % x == 0) and (z % y == 0):
#             lcm = z
#             break
#         z += 1
    
#     return lcm

# print(lcm(4, 6))
# print(lcm(15, 17))



#31. GCD Calculator:
# def gcd(x,y):
#     gcd = 1
#     if x % y == 0:
#         return y
    
#     for k in range(int(y / 2), 0, -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break
#         return gcd

# print("GCD of 12 & 17 =", gcd(12,17))
# print("GCD of 4 & 6 =", gcd(4, 6))
# print("GCD of 336 & 360 =", gcd(336, 360))




#30.Triangle Area Calculator:
# b = int(input("Input the base: "))
# h = int(input("Input the height: "))
# area = b * h /2
# print("area =", area)



#29.Unique Colors Finder:
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print("Original set elements: ")
# print(color_list_1)
# print(color_list_2)

# print("\nDifference of color_list1 and color_list_2:")
# print(color_list_1.difference(color_list_2))
# print("\nDifference of color_list_2 and color_list_1:")
# print(color_list_2.difference(color_list_1))



#28.Even Numbers Until 237:
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
# ]

# for x in numbers:
#     if x == 237:
#         print(x)
#         break
#     elif x % 2 == 0:
#         print(x)



#27.List to String Concatenator:
# def concatenate_list_data(lst):
#     result = ''

#     for element in lst:
#         result += str(element)
#         return result
    
# print(concatenate_list_data([1,5,12,2]))



#26.List Histogram:
# def histogram(items):
#     for n in items:
#         output = ''
#         times = n
#         while times > 0:
#             output += '*'
#             times = times -1
#             print(output)


# histogram([2,3,6,5])



#25.Value in Group Tester:
# def is_group_member(group_data, n):
#     for value in group_data:
#         if n == value:
#             return True
#         return False
    
# print(is_group_member([1,5,8,3], 3))
# print(is_group_member([5,8,3], -1))



#24.Vowel Tester:
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels

# print(is_vowel('c'))
# print(is_vowel('e'))



#23.String Prefix Copies:
# def substring_copy(text, n):
#     flen = 2
#     if flen > len(text):
#         flen = len(text)
#         substr = text[:flen]
#         result = ""
#         for i in range(n):
#             result = result + substr

#             return result
        
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3))



#22.Count 4 in List:
# def list_count_4(nums):
#     count = 0
#     for num in nums:
#         if num == 4:
#             count = count + 1
#             return count

# print(list_count_4([1,4,6,7,4]))
# print(list_count_4([1,4,6,4,7,4]))



#21.Even or Odd Checker:
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")



#20. String Copy Generator:
# def larger_string(text, n):
#     result = ""
#     for i in range(n):
#         result = result + text
#         return result

# print(larger_string('abc', 2))
# print(larger_string('.py', 3))



#19.Prefix "Is" String Modifier:
# def new_string(text):
#     if len(text) >= 2 and text[:2] == "Is":
#         return text
#     else:
#         return "Is" + text

# print(new_string("Array"))
# print(new_string("IsEmpty"))



#18.Triple Sum Calculator:
# def sum_thrice(x,y,z):
#     sum = x+y+z
#     if x == y == z:
#         sum = sum * 3
#         return sum

# print(sum_thrice(1,2,3))
# print(sum_thrice(3,3,3))


#17.Number Range Tester:
# def near_thousand(n):
#         return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))



#16.Difference from 17:
# def difference(n):
#     if n <=17:
#         return 17-n
#     else:
#         return (n-17) * 2

# print(difference(22))
# print(difference(14))



#15.Sphere Volume Calculator:
# pi = 3.1415926535897931
# r = 6.0
# V = 4.0/3.0 * pi * r**3
# print('The volume of the sphere is:', V)


#14.Days Between Dates:
# from datetime import date
# f_date = date(2014, 7,2)
# l_date = date(2014,7,11)
# delta = l_date - f_date
# print(delta.days)



#13.Multi-line Here Document:
# print("""""
# a string that you "don't " have to escape
# This
# is a ........ multi-line
# heredoc string -----------> example
# """"")



#12.Monthly Calendar Display:
# import calendar
# y = int(input("Input the year: "))
# m = int(input("Input the mont: "))
# print(calendar.month(y,m))



#11.Function Documentation Printer:
# print(abs.__doc__)
# print(len.__doc__)
# print(sorted.__doc__)
# print(sum.__doc__)
# print(map.__doc__)
# print(filter.__doc__)


#10.Number Expansion Calculator:
# a = int(input("Enter an integer: "))
# n1 = int("%s" % a)
# n2 = int("%s%s" % (a,a))
# n3 = int("%s%s%s" % (a,a,a))

# print(n1+n2+n3)



#9.Exam Schedule Formatter:
# exam_st_date = (11,12,2014)
# print("The examination will start from : %i / %i / %i" % exam_st_date)



#8.First and Last Colors:
# color_list = ["Red", "Green", "White", "Black"]
# print("%s %s" % (color_list[0], color_list[-1]))


#7.File Extension Extractor:
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print("The extension of the file is :" + repr(f_extns[-1]))



#6.List and Tuple Generator:
# values = input("Input some comma-separated numbers: ")
# list = values.split(",")
# tuple = tuple(list)
# print("List :", list)
# print('Tuple :', tuple)



#5. Reverse Full Name:
# fname = input("Input your First Name: ")
# lname = input("Input your Last Name: ")
# print("Hello " + lname + " " + fname)



#4.Circle Area Calculator:
# from math import pi
# radius = float(input("Input the radius of the circle: "))
# area = pi * radius ** 2
# print("The area of the circle with radius " + str(radius) + "is :" + str(area))



#3.Current Datetime Display:
# import datetime
# now = datetime.datetime.now()
# print("Current date and time : ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))



#2.Python Version Checker:
# import sys
# print("Python version")
# print(sys.version)
# print("Version info.")
# print(sys.version_info)



#1.Formatted Twinkle Poem:
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")



#Finally:
#2 hisse 150:
#150.Cube Root Reduction Steps:
# def test(n):
#     ctr = 0
    
#     while n >= 3:
#         n = n ** (1./3.)
        
#         ctr = ctr + 1
    
#     return 'Not a positive number!' if n < 0 else ctr

# n = int(input("Input a positive integer:"))

# print(test(n))


#149.NxN Square of Integer:
