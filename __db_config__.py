import mysql.connector
from mysql.connector import Error

# Conexão com o MySQL
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Server connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# Criação do banco de dados
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# Conexão ao banco de dados
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection  


# Execução de queries
def execute_query(connection, query, values):
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# Script para criar banco de dados
create_database_query = "CREATE DATABASE coinapi"        


# Script para excluir tabela "CRYPTO_PRICES"
drop_crypto_prices_table = "DROP TABLE IF EXISTS crypto_prices"


# Script para excluir tabela "CANDLE_DATAS"
drop_candle_datas_table = "DROP TABLE IF EXISTS candle_datas"


# Script para criar tabela 'crypto_prices'se não existir
create_crypto_prices_table = '''
    CREATE TABLE IF NOT EXISTS crypto_prices (
        id INT AUTO_INCREMENT PRIMARY KEY,
        period_start DATETIME,
        period_end DATETIME,
        price_open DECIMAL(18, 2),
        price_high DECIMAL(18, 2),
        price_close DECIMAL(18, 2),
        price_low DECIMAL(18, 2),
        volume_traded DECIMAL(18, 2),
        trades_count INT
    )
'''  


# Script para criar tabela 'candle_datas'se não existir
create_candle_datas_table = '''
    CREATE TABLE IF NOT EXISTS candle_datas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        period_start DATETIME,
        period_end DATETIME,
        price_open DECIMAL(18, 2),
        price_high DECIMAL(18, 2),
        price_close DECIMAL(18, 2),
        price_low DECIMAL(18, 2),
        volume_traded DECIMAL(18, 2),
        trades_count INT
    )
'''  

# Script para evitar erro DATE TIME ZERO no SQL
insert_query = "SET GLOBAL sql_mode = ''"



