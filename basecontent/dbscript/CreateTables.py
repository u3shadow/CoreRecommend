from MainToFlask import connect_db
db = connect_db()
schema = open('schema.sql')
db.cursor().execute(schema.read())