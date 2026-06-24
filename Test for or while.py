# 1.WRITE A PROGRAM TO PRINT ONLY DIGITS FROM THE STRING
#
# EXAMPLE- a='Yash@1$2'
#          output='12'

# a=(input('string:'))
# for i in a:
#     if '0' <= i <= '9':
#         print(i)

# a=(input('string:'))
# i = 0
# while i < len(a):
#     if '0' <= a[i] <= '9':
#         print(a[i])
#     i += 1




#
# 2.WRITE A PROGRAM TO EXTRACT ONLY UPPERCASE CHARACTERS FROM THE STRING
#
# EXAMPLE- a='YaSHrAJ@12'
#          output='YSHAJ'


# a=input('Enter the string:')
#
# i = 0
# upper = ''
#
# while i < len(a):
#     if 'A' <= a[i] <= 'Z':
#         upper += a[i]
#     i += 1
# print(upper)

#
# 3.WRITE A PROGRAM TO EXTRACT ONLY INTEGERS FROM THE BELOW LIST IF THEIR LAST DIGIT IS 5
#
# data=[12,45,'Hii',True,8+9j,60]

# i = 0
# while i < len(data):
#     if type(data[i]) == int and data[i] %  10==5:
#         print(data[i])
#     i += 1




# for i in data:
    # if type(i) == int and i % 10 == 5:
    #     print(i)


# 4.WRITE A PROGRAM TO GET THE FOLLOWING OUTPUT
#
# a='PjKTY@3!8'
#
# upper='PKTY'
# lower='j'
# digits='38'
# special='@!'

# i = 0
# upper = ''
# lower = ''
# digits = ''
# sc = ''
#
# while i < len(a):
#     if 'A' <= a[i] <='Z':
#         upper += a[i]
#     elif 'a' <= a[i] <= 'z':
#         lower += a[i]
#     elif '0' <= a[i] <= '9':
#         digits += a[i]
#     else:
#         sc += a[i]
#     i += 1
# print(upper)
# print(lower)
# print(digits)
# print(sc)
#
#
# 5.WRITE A PROGRAM TO PRINT ONLY NUMBERS DIVISIBLE BY 5 BETWEEN 200 TO 400


# i = 200
# while i <= 400:
#     if i % 5 == 0:
#         print(i)
#     i += 1