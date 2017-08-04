import MySQLdb as mysql
def connect_db():
    """Connects to the specific database."""
    rv = mysql.connect(host='localhost',user='root',passwd='u3shadow',db='test')
    return rv