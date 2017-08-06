import psycopg2 as psy
def connect_db():
    """Connects to the specific database."""
    rv = psy.connect(database="redb", user="u3", password=" ")
    return rv