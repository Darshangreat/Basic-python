import pymysql

mysql = pymysql.connect(

host = 'localhost',
user = 'root',
password = 'stockstreet',
database = 'amazon',
port = 3306

)

cursor=mysql.cursor()
query='''SELECT * FROM amazon_electronics'''

cursor.execute(query)
data=cursor.fetchall()

# print(data)


#Q3.

# for i in data:
#     print(i[1])
#     print(i[4])


#Q4.

# for i in data:
#     if i[3] == 'Apple':
#         print(i)


#Q5.

# for i in data:
#     if i[4] >= 50000:
#         print(i)


#Q6. 

# for i in data:
#     if i[5] <= 20:
#         print(i)

#Q7.

# out = []
# for i in data:
#     if i[2] == 'Laptop':
#         out.append(i)
# print(out)

#Q10. Increase the stock of a product using Product ID. 

# query = '''update amazon_electronics set stock = 10 '''
# cursor.execute(query)


#Q.11. Update the price of a product. 

# query = '''update amazon_electronics set price = 100'''
# cursor.execute(query)


#Q12. Update the seller name

# query = '''update amazon_electronics set seller = 'Redmi' where product_id = 1'''
# cursor.execute(query)


#Q13. Update the delivery days

# query = '''update amazon_electronics set delivery_days = 100 where product_id = 5'''
# cursor.execute(query)


#Q14. Delete a product using Product ID. 

# query = '''delete from amazon_electronics where product_id = 1 '''
# cursor.execute(query)


#Q15. Delete all products whose stock is zero.

query = '''delete from amazon_electronics where stock = 0'''
cursor.execute(query)
mysql.commit()
mysql.close()