import os


def get_postgres_database_uri():
    sql_user = os.environ["SQL_USER"]
    sql_password = os.environ["SQL_PASSWORD"]
    sql_host = os.environ["SQL_HOST"]
    sql_port = os.environ["SQL_PORT"]
    sql_database = os.environ["SQL_DATABASE"]
    return f"postgresql://{sql_user}:{sql_password}@{sql_host}:{sql_port}/{sql_database}"