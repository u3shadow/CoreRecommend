from DBmethods import connect_db
db = connect_db()
schema = open('schema.sql')
cur = db.cursor()
cur.execute(schema.read())
db.commit()
db.close()
print "create finish"

