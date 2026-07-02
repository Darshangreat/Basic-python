# example :-

#Function without argument and without values


#
# def extract():
#     a = input('Enter the name:')
#     data = ''
#     for i in a:
#         if i in 'AEIOUaeiou':
#             data = data + i
#     print(data)
#
# extract()



#Function with arguments

# def extract(a:str,data=''):
#     for i in a:
#         if i in 'AEIOUaeiou':
#             data = data + i
#     print(data)
#
# extract('Darshan')
# extract('Rahul')

#Q.Wap to print prime numbers the between the specify limit


# a=int(input('Enter the number:'))
# b=int(input('Enter the number:'))
#
# for i in range(2,10):
#     if i % 2 == 0:
#         print(i)
#


#Q.Check the given number is prime number or not

def extract(a:int):

    for i in range(2, a):
        if a % i == 0:
            print('Prime number')
            break
    else:
        print('Not prime')

extract(5)
