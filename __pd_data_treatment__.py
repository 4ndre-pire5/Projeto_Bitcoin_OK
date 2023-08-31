import json
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

def data_treatment(data):

    # Salva 'data' com nome 'savedata.json'
    save_file = open("savedata.json", "w")
    json.dump(data, save_file, indent=6)
    save_file.close()

    # Cria dataframe com pandas
    df = pd.read_json('savedata.json')

    # Cria uma nova coluna com o valor médio do preço
    df["mean_price"] = df.loc[:,['price_open','price_high','price_low','price_close']].mean(axis = 1)

    # Exclui colunas não usadas
    df.drop(['time_period_start', 'time_open', 'time_close', 'trades_count'], axis=1, inplace=True)

    # Conversão para datetime pegando apenas a data
    df['time_period_end'] = pd.to_datetime(df['time_period_end'])
    
    # Tamanho da figura
    plt.figure(figsize=(20, 10))

    # Títulos do gráfico
    plt.title('Valor mensal médio do BITCOIN nos últimos 5 anos')
    plt.xlabel('Ano')
    plt.ylabel('Valor (USD)')
    plt.grid(color = 'gray', linestyle = 'dotted')
    plt.legend(loc = 'upper right', title = 'Valor BitCoin', edgecolor = 'blue', shadow = True)
    
    # Dados do gráfico
    plt.plot(df['time_period_end'],
             df['mean_price'],
             marker = '.'
            )
    
    plt.show() 


def candle_treatment(data):

    # Salva 'data' com nome 'candledata.json'
    save_file = open("candledata.json", "w")
    json.dump(data, save_file, indent=6)
    save_file.close()

    # Cria dataframe com pandas
    first_df = pd.read_json('candledata.json')

    # Filtra o dataframe para o periodo de 1 mês
    df = first_df.loc[(first_df['time_period_start'] >= '2023-08-01')
                        & (first_df['time_period_start'] <= '2023-08-31')]
                   
    # Conversão para datetime
    df['time_period_start'] = pd.to_datetime(df['time_period_start'])

    # Faz 'time_period_start como índice da tabela
    df = df.set_index('time_period_start')

    # Exclui colunas não usadas
    df.drop(['time_period_end', 'time_open', 'time_close', 'trades_count'], axis=1, inplace=True)

    # Renomeia colunas para equalizar com mplfinance
    df.rename(columns = {'price_open':'Open', 
                         'price_high':'High', 
                         'price_low':'Low', 
                         'price_close':'Close', 
                         'volume_traded':'Volume'}, 
                         inplace=True)

    # Plota o gráfico                                                                                                 
    mpf.plot(df, 
             type = 'candle', 
             style = 'charles',
             figratio = (20, 10),
             xlabel = 'Data',
             ylabel = 'Valor (USD)',
             title = 'Gráfico CandleStick do BitCoin do mês Agosto-23'
            )


    


    
