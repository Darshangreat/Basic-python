import sqlite3

var = sqlite3.connect('marks.db')
write = var.cursor()

query = 'delete from students'

write.execute(query)
var.commit()
var.close()