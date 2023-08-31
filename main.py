from __db_config__ import *
from __api_request__ import *
from __pd_data_treatment__ import *


# Conectar ao banco de dados MySQL
connection = create_server_connection("localhost", "root", "teste@1234")

# Comando  para criar o banco de dados 
create_database(connection, create_database_query)

# Conecta ao banco de dados
connection = create_db_connection("localhost", "root", "teste@1234", "coinapi")

# Exclui tabela "CRYPTO_PRICES" sempre que rodar aplicação
execute_query(connection, drop_crypto_prices_table, 0)

# Exclui tabela "CANDLE_DATAS" sempre que rodar aplicação
execute_query(connection, drop_candle_datas_table, 0)

# Executa query para criar tabela "CRYPTO_PRICES" se não existir
execute_query(connection, create_crypto_prices_table, 0)

# Executa query para criar tabela "CANDLE_DATAS" se não existir
execute_query(connection, create_candle_datas_table, 0)

# Executa query para evitar erro DATE TIME ZERO no SQL
execute_query(connection, insert_query, 0)

# Faz solicitação à API e imprime dados obtidos
data = api_request(connection)
print(data)

# Faz solicitação à API e imprime dados obtidos
candle_data = candle_api_request(connection)
print(candle_data)

# Tratamento para gráfico valores
data_treatment(data)

# Tratamento para gráfico candle
candle_treatment(candle_data)

# Commit as mudanças e fechar a conexão
connection.commit()
connection.close()



