




def area_shape(base, height, shape):
	if shape == 'triangle':
		return 0.5 * base * height
	else:
		return base * height


def ASCII(txt):
    return ord(txt)

def has_spaces(txt):
	return ' ' in txt 


def stack_boxes(n):
	if n > 0:
		return n ** n
	else:
		return 1

def odd_or_even(word):
	return len(word) % 2 == 0

oddOrEven=lambda w:len(w)%2<1

def odd_or_even(str):
	return not len(str) % 2

def flip_bool(b):
	return 1 - b


def flip_bool(b):
	return not b



def is_last_character_n(word):
	return word[-1] == 'n'





def is_plural(word):
	return word[-1] == 's'


# Fix this broken code!
def check_equals(lst1, lst2):
	return lst1 == lst2




# class Employee:
# 
    # raise_amt = 1.04
    # num_of_emps = 0
# 
    # def __init__(self, first, last, pay):
        # self.first = first
        # self.last = last
        # self.email = first + '.' + last + '@email.com'
        # self.pay = pay
# 
        # Employee.num_of_emps += 1
        # 
    # def fullname(self):
        # return '{} {}'.format(self.first, self.last)
# 
    # def apply_raise(self):
        # self.pay = int(self.pay * self.raise_amt)


# print(Employee.num_of_emps)
# 
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)
# 
# print(Employee.raise_amt)
# print(emp_2.pay)
# Employee.apply_raise(emp_2)
# print(emp_2.pay)


# print(Employee.num_of_emps)

# emp_1.raise_amt = 1.05
# print(emp_1.__dict__)
# Employee.raise_amt = 1.05

# print(Employee.__dict__)
# print(emp_2.__dict__)

# print(Employee.raise_amt)
# print(emp_1.pay)
# Employee.apply_raise(emp_1)
# print(emp_1.pay)

# print(emp_2.raise_amt)
# print(Employee.raise_amt)
# print(emp_2.raise_amt)

# print(emp_1.last, emp_2.first, emp_1.pay, emp_2.email)
# print(emp_1.fullname())








# ------------ OBJECT ORIENTED PROGRAMMING---------------



# colors = ['red', 'green', 'yellow', 'white', 'black']

# with open('new_file.txt', 'w', encoding='utf-8') as file:
#     for i in colors:
#         file.writelines(i + '\n')

# with open('new_file.txt', 'r', encoding='utf-8') as file:
#     print(file.read())




# with open('fishes.txt', 'r', encoding = "utf-8") as sea:
#     fish_lines = sea.readlines()

# with open('fishes.txt', 'w', encoding = "utf-8") as sea:
#     for reef in fish_lines:
#         sea.write(reef + '\n')


# with open('fishes.txt', 'r', encoding = "utf-8") as sea:
#     print(sea.read())








# with open('new_file.txt', 'w', encoding='utf-8') as file:
#     file.write('Live to help others live.')

# file = open("new_file.txt", 'r')   
# print(file.read())




# sudoku = [
#     [0, 0, 0, 0, 6, 4, 0, 0, 0],
#     [7, 0, 0, 0, 0, 0, 3, 9, 0],
#     [8, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 5, 0, 2, 0, 6, 0],
#     [0, 8, 0, 4, 0, 0, 0, 0, 0],
#     [3, 5, 0, 6, 0, 0, 0, 7, 0],
#     [0, 0, 2, 0, 0, 0, 1, 0, 3],
#     [0, 0, 1, 0, 5, 9, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 7, 0, 0]
# ]

# def slice_and_write(table_name):
#     k = 0
#     print(*'-' * 13)
#     while k < len(table_name):
#         for i in table_name[k:(k+3)]:
#             print(*i[0:3], ' | ', *i[3:6], ' | ', *i[6:9])
#         print(*'-' * 13)
#         k += 3

# slice_and_write(sudoku)


# print(*'-------------')
# k=0
# while k <len(sudoku) :
#     for i in sudoku[k:(k+3)]:
#         print(*i[0:3], ' | ', *i[3:6], ' | ', *i[6:9])
#     print(*'-------------')    
#     k+=3



# sudoku = [x[0:3]+["|"]+x[3:6]+["|"]+x[6:] for x in sudoku]
# count=0
# for i in sudoku:
#     if count%3==0:
#         print(21*"-")
#     print(*i)
#     # for ii in range(len(sudoku)+2):
#     #     print(i[ii],end=" ")
#     # print("\r")
#     count+=1
# print(21*"-")



# print(*'-------------')

# for i in sudoku[0:3]:
#     print(*i[0:3], ' | ', *i[3:6], ' | ', *i[6:9])
# print(*'-------------')

# for i in sudoku[3:6]:
#     print(*i[0:3], ' | ', *i[3:6], ' | ', *i[6:9])
# print(*'-------------')

# for i in sudoku[6:9]:
#     print(*i[0:3], ' | ', *i[3:6], ' | ', *i[6:9])
# print(*'-------------')






# fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']

# with open('fruit.txt', 'w', encoding='utf-8') as file:
#     for i in fruits:
#         file.write(i + '\n')

# with open('fruit.txt', 'w', encoding='utf-8') as file:
#     print(file.read())


# with open("dummy_file.txt", 'w', encoding="utf-8") as file:
#     file.write('My first sentence')
#     file.write('My second sentence,')
#     file.write('My third sentence\n')
#     file.write('My fourth sentence ')
#     file.write('My last sentence')

# with open("dummy_file.txt", 'r', encoding="utf-8") as file:
#     print(file.read())


# with open('dummy_file.txt', 'w', encoding='utf-8') as file:
#     file.write('This is the new line for my dummy_file')

# with open('dummy_file.txt', 'r') as file:
#     print(file.read())


# with open('dummy_file.txt', 'w', encoding='utf-8') as file:
#     file.write('This is the first line of the file.')

# with open('dummy_file.txt', 'r') as file:
#     print(file.read())



# my_file = open('fishes.txt', 'r')
# for i in my_file:
#     print(i)
# my_file.close()



# my_file = open('fishes.txt', 'r')
# print(my_file.readlines())
# my_file.close()


# my_file = open('fishes.txt', 'r')
# print(my_file.read(9))
# my_file.close()

# my_file = open('fishes.txt', 'r')
# print(my_file.readline())
# my_file.close()


# my_file = open('fishes.txt', 'r')
# print(my_file.read(40))
# my_file.close()



# my_file = open('fishes.txt', 'r')
# print(my_file.read())
# my_file.close()

# my_file = open('fishes.txt', encoding='utf-8')

# print(type(my_file))


# with open('fishes.txt', 'r', encoding='utf-8') as my_file:
#     print(type(my_file))


# with open ('fishes.txt', 'r') as my_file:
#     print(my_file.read())


# with open("fishes.txt", "r") as sea:
#     print(sea.read())  # needs indented code block


# sea = open("fishes.txt", 'r')   

# print(sea.readlines())

# sea.close()


# sea = open("fishes.txt", 'r')   

# print(sea.readline(13))
# print(sea.readline(13))
# print(sea.readline(13))
# print(sea.readline(13))

# sea.close()


# sea = open("fishes.txt", 'r')   

# print(sea.readline())  # displays the first line of the text
# print(sea.readline())  # displays the second line
# print(sea.readline())  # each time it goes to the new line

# sea.close()


# my_file = open("fishes.txt", 'r')   
# print(my_file.read(5)) 
# my_file.close()




# sea = open("fishes.txt", 'r')   

# print(sea.read(33))  # displays the first 33 chars of the text
# print()
# print(sea.read(25))  # displays the next 25 chars of the text
# print()
# sea.seek(0)  # changes the stream (cursor) position to zero
# sea.seek(2) 
# print(sea.read(33))  # displays the first 33 chars again
# print()
# print(sea.tell())  # returns the current stream (cursor) position

# sea.close()




# sea = open("fishes.txt", 'r')   
# print(sea.read())  # displays the entire text content
# sea.close()  # be sure to close the file



# def factor(x):
#     result = 1
#     for i in range(x):
#         result *= (i + 1)
#     print (result)

# factor(4)

# import string
# print(string.punctuation)




# def not_string(word):
#     (word == word) if (word[0:4]) == 'not ' else (word = ('not', word))

        

# def not_string(word):
#     if (word[0:4]) == 'not ':
#         return word
#     else:
#         return 'not ' + word


# def not_string(word):  # ÇALIŞMIYOR
#     if (word[0:4]) != 'not ':
#         return 'not', word
#     return word


# print(not_string('sugar'))  # not sugar
# print(not_string('x'))  # not x
# print(not_string('not bad'))  # not bad


# def parrot_trouble(talking, hour):
#     if talking == True and (7 > hour or hour> 20):
#         return True
#     else:
#         return False
# print(parrot_trouble(True, 5))
# print(parrot_trouble(True, 8))
# print(parrot_trouble(False, 22))


# def parrot_trouble(talking, hour):
#     lambda x: False if talking == True or 7 < hour < 20 True





# def sum_double(x, y):
#     if x == y:
#         return((x + y) * 2)
#     else:
#         return (x + y)
# print(sum_double(5, 7))
# print(sum_double(5, 5))




# def repeater(n):
#     return lambda x: x * n

# print(repeater(5)('Alex '))


# def modular_function(n):
#     return lambda x: x ** n

# print(modular_function(2)(3))






# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(filter(lambda x: True if x >= 6 else False, number_list))

# print(result)




# vowel_list = ['a', 'e', 'i', 'o', 'u']
# first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# selected = filter(lambda x: True if x in vowel_list else False, first_ten)
# print(list(selected))


# rumi = open('runi.txt', 'r', encoding='utf-8')
# # print(rumi.read())
# print(rumi.read(33))
# print(rumi.read(25))

# print(rumi.tell())
# rumi.close()


# number_list = [1, 2, 3, 4, 5]

# result = list(map(lambda x : x * 3, number_list))
# print(result)


# echo_word = lambda x, y: x * y
# print(echo_word('hello', 3))


# def outer():
#     x = "previous"
    
#     def inner():
#         nonlocal x
#         x = "later"
#         print("inner:", x)
    
#     inner()
#     print("outer:", x)

# outer()



# city = "I love Paris!"

# def my_function(): 
#     city = 'I love London!'
#     print(city) 
# my_function()


# y = 10  
# def my_function_2(): 
#     y += 5 
#     print(y)
# my_function_2()




# x = 10
# def my_function_1(): 
#     x = 20 
#     print(x)
# my_function_1() 



# def longer(a, b):
#     if len(a) >= len(b):
#         longer_one = a
#     else:
#         longer_one = b
#     return longer_one

# print(longer('Richard', 'Johnsonn'))




# area = 0
# def my_function(x, y):
#     area = (x * y)
#     return area
# print(my_function(3, 4))


# hypotenuse = 0

# def my_function(a, b):
#     hypotenuse = (a**2 + b**2)**0.5
#     return hypotenuse
# print(my_function(1, 1))


# def make_sentence(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for i in kwargs.values():
#         result += i
#     return result

# print(make_sentence(a="I ", b="love ", c="Clarusway! ", d="said"))



# def gene(x='Solomon', y='David'):  # defined by kwargs (default values assigned to x and y)
#     print(x, "belongs to Generation X")
#     print(y, "belongs to Generation Y")
 
# dict_gene = {'y' : "Marry", 'x' : "Fred"}
# gene(**dict_gene) 


# def gene(x, y):  # defined by positional args
#     print(x, "belongs to Generation X")
#     print(y, "belongs to Generation Y")
 
# dict_gene = {'y' : "Marry", 'x' : "Fred"}
# gene(**dict_gene)  # we call the function by a single argument(variable)



# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments 
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# deger = input('give a number')
# if deger.isdigit() == False:
#     print ("It is an invalid entry. Don't use non-numeric, float, or negative values!")
# liste = list(deger)
# total = 0
# if deger.isdigit() == True:
#     for i in liste:
#         her_sayi = (int(i)) ** len(liste)
#         total += her_sayi
#     if int(deger) == total:
#         print(f'{total} is an Armstrong number')
#     else:
#         print(f'{deger} is not an Armstrong number')





# given_number = input('Please enter a number: ')
# given_number_set = set(given_number)
# given_number_list = list(given_number)
# numeric_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
# union_set = given_number_set.union(numeric_set)
# n = len(given_number)

# if len(union_set) > len(numeric_set):
#     print('It is an invalid entry. Don\'t use non-numeric, float, or negative values!')
# else:
#     result = 0
#     for i in given_number_list:
#         result += int(i) ** n

#     if str(result) == given_number:
#         print('This is Armstrong number.')
#     else:
#         print('This is not an Armstrong number.')



# if len(union_set) <= len(numeric_set):
#     if str(result) == given_number:
#         print('This is Armstrong number.')
#     else:
#         print('This is not an Armstrong number.')
# else:
#     print('It is an invalid entry. Don\'t use non-numeric, float, or negative values!')






# print(given_number_list)
# print(type(given_number_list[0]))
# # print(given_number_set)
# # print(numeric_set)
# # print(union_set)
# print(type(n))





# 371

# sonuç == given_number >>>>>>>>> Armstrong















# if type(number) == type(2):
#     print('OK')
# else:
#     print('It is an invalid entry. Don\'t use non-numeric, float, or negative values!')


# sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]
# for i in sample_list:
#     print('The type of', i, 'is', type(i))


# number = int(input('Please enter a number: '))
# x = 0
# while x < number:
#     print(x ** 2)
#     x += 1



# a = 49
# while  a <= 62:
#     print(a)
#     a += 5


# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# for day in range(len(weekdays)):
#     print('Day', day+1, ':', weekdays[day])



# x = 0
# list_word = []
# sentence = input('bir cümle giriniz: ')
# while x < len(sentence) :
#     list_letter = []
#     while x < len(sentence) and sentence[x] != ' ':
#         list_letter.append(sentence[x])
#         x += 1
#     list_word.append(list_letter)
#     x += 1
# max_word_list = max(list_word, key = len)
# separator = ''
# print(separator.join(max_word_list), len(max_word_list))


# math_mark = int(input('Please write your score: '))

# if math_mark >= 85:
#     letter = 'A (Excellent)'
# elif math_mark >= 70:
#     letter = 'B (Good)'
# elif math_mark >= 60:
#     letter = 'C (Medium)'
# elif math_mark >= 45:
#     letter = 'D (Not Bad)'
# else:
#     letter = 'F (Failed)'
# result = f'Your score is {letter}'
# print(result)






# saved_amount = int(input('Please enter your saved amount: '))
# ps4_price = 200

# if saved_amount >= ps4_price:
#     print('Yippee! You can buy your PS4')
# else:
#     if saved_amount > ps4_price / 2:
#         print('You saved more than half, keep saving!')
#     else:
#         print("You must save more, keep saving!")



# total = 149
# country = "FR"

# if country == "FR":
#     if total <= 50:
#         print("Shipping Cost is  €30")
#     elif total <= 100:
#         print("Shipping Cost is €15")
#     elif total <= 150:
#         print("Shipping Costs €10")
#     else:
#         print("Free Shipping")
# if country == "DE": 
#     if total <= 50:
#         print("Shipping Cost is  €25")
#     else:
#         print("Free Shipping")


# a = 3
# while a**2 < 299:
#     print('I will stop smoking')
#     a += 3


# text = ['ali', 'veli', 'deli']
# number = [1, 2, 3]
# for x, y in zip(text, number):
#     print(x, '-', y)

# print(*range(100,0,-3))
# print(* 'separate')

# n = int(input('enter a number between 1-10: '))

# for i in range(1,11):
#     print('{}x{} = '.format(n, i), n*i)
#     print('%d x %d = ' %(n, i), n*i)
    # print('I am %d. I have %.3f dollars.' % (age, dollar)) # Örnek satır


# iterable = [1, 2, 3, 4]
# for i in iterable:
#     print(i ** 2)


# for i in {'n1' : 'one', 'n2' : 'two'} : 
#     print(i)


# flowers = ['Rose', 'Orchid', 'Tulip']
# count1 = len(flowers)
# count2 = 0

# while count1 > 0 :
#     print(flowers[count2])
#     count1 -= 1
#     count2 += 1
    

# answer = 39

# question = 'What number am I thinking of?  '
# print ("Let's play the guessing game!")

# while True:
#     guess = int(input(question))

#     if guess < answer:
#         print('Little higher')
#     elif guess > answer:
#         print('Little lower')
#     else:  # guess == answer
#         print('Are you a MINDREADER!!!')
#         break



# score = int (input("Enter your score :"))

# if score >= 90:
#     if score >= 95:
#         Score_letter="A+"
#     else:
#         Score_letter="A"
# elif score >= 80:
#     if score >= 85:
#         Score_letter="B+"
#     else:
#         Score_letter="B"
# else:
#     Score_letter="below B"

# print ("Your degree: %s" % Score_letter)



# number = 7
# if number >= 10:
#     print('The number is equal or greater than 10')
# else:
#     print('The number is less than 10')

# family_members = ['Meghan', 'Tom', 'Nicole', 'Tim']
# family = tuple(family_members)
# print(family)
# print(type(family))




# letters = list(word)
# n = len(word)
# print(n)
# letters[0]


# print(list(word))
# print((word in 'left_hand') and (word in 'right_hand'))

# left_hand = {
#         ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'],
# }

# right_hand = {
#         ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'],
# }


# school_records={
#     "personal_info":
#         {"kid":{"tom": {"class": "intermediate", "age": 10},
#                 "sue": {"class": "elementary", "age": 8}
#                },
#          "teen":{"joseph":{"class": "college", "age": 19},
#                  "marry":{"class": "high school", "age": 16}
#                },
#         },
#     "grades_info":
#         {"kid":{"tom": {"math": 88, "speech": 69},
#                 "sue": {"math": 90, "speech": 81}
#                },
#          "teen":{"joseph":{"coding": 80, "math": 89},
#                  "marry":{"coding": 70, "math": 96}
#                },
#         },
# }

# print(school_records['grades_info']['teen']['joseph'])
# print(list(school_records['grades_info']['teen']['joseph'].items()))

# my_dic = {
#     'name1' : 'Feyzullah',
#     'name2' : 'Dilek',
#     'name3' : 'Serdar',
#     'name4' : 'Azra'
# }
# print(my_dic, end='\n')

# new_dic = dict(name1 = 'Ali', name2 = 'Veli')
# print(new_dic)

# print(len(["e,r,t,y,u", '3233'][1]))

# planets = ('mercury', 'jupiter', 'saturn')
# print(planets)
# print(type(planets))


# print(list(range(11)))


# numbers = {}
# numbers['x'] = 12
# numbers['y'] = 4
# numbers.update({'z': 3})

# print(numbers['x'] + numbers['y'] + numbers['z']**2)

# print(len(set('listen to the voice of enlisted')))

# flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
# colors = ["red", ("blue", ["yellow", "green"]), "pink"]

# text = "My two favorite flowers are {} and {}, two favorite colors are {} and {}.".format(flowers[0][2],flowers[0][1][1],colors[1][0],colors[1][1][1])
# print(text)

# flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
# colors = ["red", ("blue", ["yellow", "green"]), "pink"]
# text = ("My two favorite flowers are {[0][2]} and {[0][1][1]},".format(flowers)) 
#     # "two favorite colors are {[1][0]} and  {[1][1][2]}.".format(colors))
# print(text)


# escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]
# sentence = "I am 40 years old. {}I have two children. {}{}\
#     Data Science is my IT domain.".format("\n\t", "\n", "\t\t")
# sentence = "I am 40 years old. {}I have two children. {}{}\
#     Data Science is my IT domain.".format(escapes[0], escapes[2][0], escapes[1][1])
# print(sentence)


# grocer = ["banana", \
#         ["orange", \
#             ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ],  
#             "water"],\
#         "mandarin"]
# print(grocer[1][1][1:6:2]) # 1den 6ya atlayarak yazdırdı
# print([grocer[0], grocer[1][1][0]])  # ayrı ayrı yazdırmak için

# my_list = [* range(1,11)]
# my_list.sort(reverse = True)  # Tersten yazdırma bu şekil
# print(my_list)

# print(*range(2,10))  # ÇALIŞMADI!!!!!!!!!!!!!!
# my_list = [(range(1, 11)]
# my_list.append )
# my_list.sort(-1)
# print(my_list)

# mix_value = (10, False, 'fruit', 1.618)
# mix_value.append(['vegetable', 2+3j])
# print(len(mix_value))

# mountain = tuple('Alps')
# print(mountain) 

# my_tuple=(1, 4, 3, 4, 5, 6, 7, 4)
# my_list = list(my_tuple)
# print(type(my_list), my_list)

# my_tuple=(1, 4, 3, 4, 5, 6, 7, 4)
# my_list = list(my_tuple)
# print(type(my_list), my_list)

# planets = 'mercury', 'jupiter', 'saturn'
# print(planets)
# print(type(planets))

# try_tuple = ('love')
# print(try_tuple)
# print(type(try_tuple)) # it's not tuple type.

# try_tuple2 = ('love',)
# print(try_tuple2)
# print(type(try_tuple2)) # it's a tuple type.

# odd_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(odd_no[7:3:-1])
# print(odd_no[2:6:-1])


# print(len([[12, 34, 56]][0]))  # ANLAMADIM????

# print(len([[12, 34, 56]]))

# even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(even_numbers[4:9])


# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[:])  # all elements of the list

# count = list(range(11))
# print(count)
# print(count[0:11:2])

# numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# print(numbers[2:5])  # we get the elements from index=2 to index=5(5 is not included)

# fruits = ['apple', 'banana', 'watermelon', 'orange', 'mango', 'avocado']
# fruit_list = []
# fruit_list.insert(0, fruits)
# print(fruit_list[0][2][7])

# city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']]
# print(city_list[0][2][3])

# colors = ['red', 'purple', 'blue', 'yellow', 'green']
# print(colors[2])  # If we start at zero, the second element will be 'blue'.











# yas = {'emma':75, 'ahmet':19, 'selim':9, 'jack':99, 'sema':111, 'serdar':41}
# def dic_val(dic,maxORmin):
#     dicTolist = list(dic.items())                # dictionary'i listeye çevirir.
#  #   values = list(dic.values())                 # fazladan yazdım silinebilir.
#  #   keys = list(dic.keys())                     # fazladan yazdım silinebilir.
#     if maxORmin == "max":                        # dictionary içerisinde max value bulmak için.
#         dicMaxVal = max(list(dic.values()))      # listeye çevrilen dictonary içerisinde max value'yi bulur
#         x = 0
#         for i in dicTolist:        # for döngüsü ile listeye çevrilen dictonary içerisinde max value hangi cell de onu bulur.
#             if dicMaxVal in i:
#                 print("  Key  : ",i[0],"\n Value : ",i[1])
#             else:
#                 x+=1
#                 continue
#     elif maxORmin == "min":                     # dictionary içerisinde min value bulmak için.
#         dicMinVal = min(list(dic.values()))     # listeye çevrilen dictonary içerisinde max value'yi bulur
#         x = 0
#         for i in dicTolist:
#             if dicMinVal in i:
#                 print("  Key  : ",i[0],"\n Value : ",i[1])
#             else:
#                 x+=1
#                 continue
#     else:
#         print("lütfen 'dic_val(dic,maxORmin)' içerisinde 'dict' yanında 'max' veya 'min' değerlerinden birini girdiğinize emin olunuz.")
# dic_val(yas,"min")                    # burada fonksiyon içerisinde dictionary'nın "min" value'yi aryoruz.("max" ı da arayabiliriz.)


# text = "{0}! I am a {1} programmer and I {2} Clarusway.".format("Hello", "new", "love")
# print(text)

# empty_list_1= ['New York', 'London', 'Stockholm']
# empty_list_2 = list('Yaşamak insanca ve özgürce')

# print(empty_list_1)
# empty_list_1.append('114') # liste sonuna ekledi
# print(empty_list_1)
# empty_list_1.append('plastic-free sea')
# print(empty_list_1)
# empty_list_1.append('Son Durak') 
# print(empty_list_1)
# empty_list_1.insert(0, 'inserted_object')  # en başa ekleme yaptı
# print(empty_list_1)
# empty_list_1.remove('New York')  # New York listeden çıktı
# print(empty_list_1)
# deleted_item = empty_list_1.pop(2)  # index 2'deki nesneyi çıkardı.
# print(deleted_item)
# print(empty_list_1)
# empty_list_1.pop(-1)  # en sondaki nesneyi çıkardı.
# print(empty_list_1)



# print(empty_list_2.index('a', 2, 20))  # index 2'den başladı 20'ye kadar a \
#                                       # karakterini bulduğu yerin indexini verir.
# del empty_list_1  # listeyi komple siler

# print(empty_list_1)
# print('Liste uzunluğu: ' + str(len(empty_list_1)))  # len uzunluğu verir(int)
# print()
# print(empty_list_2)
# print(* empty_list_2)  # listeyi aralara boşluk bıraktırarak yazdırdı.
# print()
# print(empty_list_2 * 2)  # listeyi iki defa yazdırdı.



# warning = 'You must quit smoking!'
# print(warning)
# print(list(warning))
# print(len(list(warning)))

# word = 'clarusway'
# n = 3
# front = word[:n]
# back = word [4:]
# print(front + back)

# text = "Clarusway, Clarusway, Clarusway, \n\tClarusway, Clarusway, Clarusway, \n\t\tClarusway, Clarusway, Clarusway"
# print(text)

# city = "SARAJEVO"
# text = f"I live in {city.capitalize()}."
# print(text)

# city = "SARAJEVO".capitalize()
# text = f"I live in {city}."
# print(text)

# var1 = "sleep"
# var2 = "eat"
# var3 = "better"
# var4 = "life"
# text = f"The less you {var1} and {var2}, the {var3} your {var4} will be."
# print(text)

# print(int("5" + "1"))
# print(str("5" + "1"))
# print("5" + "1")

# print(float("140" * int(input("Enter a number:" ))))


# print(False and {0} or [])

# section_3_5 = "python data types and useful operations".title()
# print(section_3_5)


# print('{3} {2} {4} {1} {0}'.format('job.', 'a', 'will', 'I', 'find'))


# print(not(3 or None))
# print()
# print(not(None) or 4)

# print("{4} {9} {1} {7} {5} {0} {6} {8} {3} {2}".format('while',\
#      'dream', 'work.', 'and', 'Some', 'success', 'others', 'of', 'wake up', 'people'))


# ay = 12
# aylik_maas = input('Aylık maaşı giriniz: ')
# for ay in range(6, 12) :
#     reel_maas = int(aylik_maas) * ay / 12
#     print(reel_maas)
#     ay -= 1


# print(not(0) and 'write me')





# tutar = float(input("Lutfen alışveriş tutarını girin"))
# verien_para = float(input("Lütfen verilen miktarı girin"))
# if verien_para < tutar:
#     print("Daha fazla para vermelisin")
# para_ustu = verien_para - tutar
# paralar = [500, 200, 100, 50, 20, 10, 5,2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
# adet,bol = 0,0
# for i in paralar:
#     bol = para_ustu//i
#     if(bol!=0):
#         adet +=bol
#         print(f"{i} euro dan  {bol} tane")
#     para_ustu = round(para_ustu%i,2)
#     #print(para_ustu)
# print(f"Toplam {adet} tane para ve { verien_para - tutar} euro vermelisin")





# def money_exchange(amount, d=[500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5,
#                               0.2, 0.1, 0.05, 0.02, 0.01]):
#     print(f'Total returned money: {amount}')
#     i = 0
#     used = {}  # start with an empty dictionary
#     while (amount > 0) and i < len(d):  # go until all money gone
#         num = amount // d[i]
#         used[d[i]] = num
#         amount -= num * d[i]
#         i += 1
#     for i in used:
#         if used[i] > 0:
#             print(f'{int(used[i])} times {i} banknotes')
#     return used
# money = float(input('Please enter your money: '))
# payment = float(input('Please enter your payment: '))
# change = money-payment
# money_exchange(change)


# 






# verilen=500
# harcama=498.14
# kasiyer=verilen-harcama
# A=(200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05)
# bozukpara={}
# for bozuk in A:
#     bozukpara[bozuk]=kasiyer//bozuk
#     kasiyer%=bozuk
#     if kasiyer < 0.05:
#         bozukpara[0.05]+=1.0
# print(bozukpara) 




# print('{3} {2} {4} {1} {0}'.format('job.', 'a', 'will', 'I', 'find')
      

# print("{4} {9} {1} {7} {5} {0} {6} {8} {3} {2}".format('while', 'dream', 'work.', 'and', 'Some', 'success', 'others', 'of', 'wake up', 'people'))

# print(bool(-1))




# x = 12
# y = x + 21
# x = 2
# print(y//x)



# text = "Clarusway, Clarusway, Clarusway"

# print(3 * text, '\t', '\n')

# print ('Yes/No lütfen', end = '\a') 
# print ('Yes/No lütfen') 


# while True:
#     age = input("Are you older then 75?  (yes/no): ")
#     if age == 'yes':
#         age = False
#     if age == 'no':
#         age = True
#         break
#     print('Yes/No lütfen') #farklı bir şey yazılması durumunda ikaz ediyor.



# while True:
#     age = input("Are you older then 75?  (yes/no): ")
#     if ((age.lower() == "yes" ) or (age.lower() == "no")):
#         print("işlem basarılı")
#         break
#     print ('Yes/No lütfen')



# city = '0123456'

# print(city[1:])  # starts from index 1 to the end
# print(city[:6])  # starts from zero to 5th index
# print(city[::2])  # starts from zero to end by 2 step
# print(city[1::2])  # starts from index 1 to the end by 2 step
# print(city[-3:])  # starts from index -3 to the end
# print(city[::-1])  # negative step starts from the end to zero

# fruit = 'Orange'

# print('Word                   : ' , fruit)
# print('First letter           : ' , fruit[0])
# print('Second letter          : ' , fruit[1])
# print("3rd to 5th letters     : " , fruit[2:5])
# print("Letter all after 3rd   : " , fruit[2:])



# age = input('Whats your age?')
# print("Eligible") if int(age)>20 else print("Not Eligible")


# print ('merhabalar efendim')
# print('dskjka dlkasfh alhf')
# list.append('utf8')  #adds a new element into a list
