host = "157.230.209.171"
user = "innis_1655"
password = "OdPs0rIewWqZMzRuMpsJizcg0ebKH8Ae"


# get_db_url returns a formatted sql connection string
def get_db_url(database, user=user, password=password, host=host):
    return f"mysql+pymysql://{user}:{password}@{host}/{database}"