#  Do the following tasks.0 check the code tasks to be done:

#Dictionaries

christopher = {}
christopher['first'] = 'Christhoper'
christopher['last'] = 'Harrison'

susan = {}
susan['first'] = 'Susan'
susan['last'] = 'Ibach'

people = []
people.append(christopher)
people.append(susan)
people.append({
     'first': 'Bill' , 'last': 'Gates'
})

print(people)







# A student makes honour role if their avarege is >=85
# and their lowest grade is not below 70

# gpa = float(input('whats your grade point avarage? '))
# lowest_grade = float(input('whats your lowest grade? '))

# if gpa >= 85 and lowest_grade >= 70:
#      honour_roll = True
# else:
#      honour_roll = False
     
# if honour_roll:
#      print('You made the honour roll')





# gpa = float(input('whats your grade point avarage? '))
# lowest_grade = float(input('whats your lowest grade? '))

# if gpa >= .85 and lowest_grade >= .70:
#      print('You made the honour roll')



# if gpa >= .85:
#      if lowest_grade >= .70:
#           print('You made the honour roll')




# country = input('where are you from?')
# if country == 'Canada':
#    province = input('Which province?')
#    if province in('Alberta', 'Nunavut', 'Yukon'):
#         tax = 0.05
#    elif province == 'Ontario':
#         tax = 0.13
#    else:
#         tax = 0.15
# else:
#     tax = 0.0
# print('Your tax is: ') 
# print(tax)




# if province in('Alberta', 'Nunavut', 'Yukon'):
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15



# if province == 'Alberta'or province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15



# if province == 'Alberta':
#     tax = 0.05
# elif province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15



# x = 9
# y = 0
# # print (x / y) # ZeroDivisionError:hatası veriyor. Acaba başka yerde hata var mı diye şöyle bir yöntem kullanılıyor. Bu hata çıkarsa şunu yaz başka hata varsa şunu yaz.
# try:
#     print(x / y)
# except ZeroDivisionError as identifier:
#     print('sıfıra bölemezsiniz.')
# else:
#     print('Başka bir hata var.')
# finally:
#     print('Bu bir hata ayıklama kodudur.')



# country = input('Which country are you from?')
# if country.lower() == 'canada':
#     print('Oh look a Canadian!')
# else:
#     print('You are not from Canada')



# price = input('How much did you pay? ')
# price = float(price)
# if price >= 1.00:
#     tax = .07
# else:
#     tax = 0
# print('Tax rate is: ' + str(tax))


# price = input('How much did you pay? ')
# price = float(price)
# if price >= 1.00:
#     tax = .07
#     print('Tax rate is: ' + str(tax))
# else:
#     tax = 0
#     print('Tax rate is: ' + str(tax))






# country = 'Canada'
# if country.lower() == 'canada'
#     print('Oh look a Canadian!')
# else:
#     print('You are not from Canada')
#ÇAlışmadı SONUNDA : EKSİKMİŞ :-D


# country = input
# input(print('Where are you from?'))
# if input == country
#     print('Hello Englisman')
# else:
#     print('You are not from ' + country)
    


# price = input('input price: ')
# if int(price) >= 1.00:
#     tax = 0.07
# else:
#     tax = 0
# print(tax)



# price = input('input price: ')
# if int(price) >= 1.00:
#     tax = 0.07
#     print(tax)
# else:
#     tax = 0
#     print(tax)







# from datetime import datetime, timedelta
# today = datetime.now()

# print('Day:' + str(today.day))
# print('Month:' + str(today.month))
# print('Year:' + str(today.year))
# print('Hour:' + str(today.hour))
# print('Minute:' + str(today.minute))
# print('Second:' + str(today.second))


# print('Today is ' + str(today))

#one_week = timedelta(weeks=1)
#last_week = today - one_week
#print('Last week was: ' + str(last_week))





# one_day = timedelta(days=1)
#yesterday = today - one_day
#print('Yesterday was: ' + str(yesterday))



#current_date = datetime.now()
#print('Today is: ' + str(current_date) )









#to get current date and time we need to use the datetime library
#from datetime import datetime, timedelta

#current_date = datetime.now()
#print('Today is: ' + str(current_date) )


#days_in_february = 28
#print(str(days_in_february) + ' days in February.')



#first_num = input('enter number')
#second_num = input('enter second number')
#print(float(first_num) ** float(second_num)) #floattaki fark 11.0 \n2şeklinde yazıyor int ile aynı fonksiyon



#first_num = input('enter number')
#second_num = input('enter second number')
#print(int(first_num) ** int(second_num))



#first_num = 5
#second_num = 6
#print(first_num + second_num)


#print('Hello World')
#print ('hello')