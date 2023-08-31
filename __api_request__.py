import requests
from __db_config__ import *
from datetime import datetime, timedelta
import json


# Tabela de period_id aceitos para solicitação
'''
Time unit	Period identifiers
Second	    1SEC, 2SEC, 3SEC, 4SEC, 5SEC, 6SEC, 10SEC, 15SEC, 20SEC, 30SEC
Minute	    1MIN, 2MIN, 3MIN, 4MIN, 5MIN, 6MIN, 10MIN, 15MIN, 20MIN, 30MIN
Hour	    1HRS, 2HRS, 3HRS, 4HRS, 6HRS, 8HRS, 12HRS
Day	        1DAY, 2DAY, 3DAY, 5DAY, 7DAY, 10DAY
Month	    1MTH, 2MTH, 3MTH, 4MTH, 6MTH
Year	    1YRS, 2YRS, 3YRS, 4YRS, 5YRS
'''

def api_request(connection):

    url = "https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?period_id=1MTH&time_start=2018-01-01T00:00:00"
    headers = { "X-CoinAPI-Key": "234FFEBF-0A02-4971-B97B-C302084E1578" }  # Replace with your API key
    response = requests.get(url, headers=headers)
    data = response.json()

    # Script para inserir dados na tabela
    insert_query = "INSERT INTO crypto_prices (period_start, period_end, price_open, price_high, price_close, price_low, volume_traded, trades_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    for crypto in data:
        period_start = crypto['time_period_start']
        period_end = crypto['time_period_end']
        price_open = crypto['price_open']
        price_high = crypto['price_high']
        price_close = crypto['price_close']
        price_low = crypto['price_low']
        volume_traded = crypto['volume_traded']
        trades_count = crypto['trades_count']

        values = (period_start, period_end, price_open, price_high, 
                price_close, price_low, volume_traded, trades_count)

        # Executa comando para inserir dados na tabela
        execute_query(connection, insert_query, values)


    return data

def candle_api_request(connection):

    url = "https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1DAY"
    headers = { "X-CoinAPI-Key": "234FFEBF-0A02-4971-B97B-C302084E1578" }  # Replace with your API key
    response = requests.get(url, headers=headers)
    #data = response.json()
    data = json.loads(response.text)

    # Script para inserir dados na tabela
    insert_query = "INSERT INTO candle_datas (period_start, period_end, price_open, price_high, price_close, price_low, volume_traded, trades_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    for crypto in data:
        period_start = crypto['time_period_start']
        period_end = crypto['time_period_end']
        price_open = crypto['price_open']
        price_high = crypto['price_high']
        price_close = crypto['price_close']
        price_low = crypto['price_low']
        volume_traded = crypto['volume_traded']
        trades_count = crypto['trades_count']

        values = (period_start, period_end, price_open, price_high, 
                price_close, price_low, volume_traded, trades_count)

        # Executa comando para inserir dados na tabela
        execute_query(connection, insert_query, values)

    return data
