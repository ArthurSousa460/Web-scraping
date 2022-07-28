import pandas as pd
from scraping import dolar, euro, gold

#código que atualiza a tabela

table = pd.read_excel('Produtos.xlsx')


def update_coin_value():
    #atualiza a cotação da moeda no dia
    table.loc[table['Moeda'] == 'Dólar', 'Cotação'] = float(dolar)
    table.loc[table['Moeda'] == 'Euro', 'Cotação'] = float(euro)
    table.loc[table['Moeda'] == 'Ouro', 'Cotação'] = float(gold)


def update_purchase_price():
    #atualiza o preço de compra da table produtos
    table['Preço de Compra'] = table['Preço Original'] * table['Cotação']


def update_sale_price():
    #atualiza o preço de venda
    table['Preço de Venda'] = table['Preço de Compra'] * table['Margem']


update_coin_value()
update_purchase_price()
update_sale_price()

table.to_excel('Produtos Novo.xlsx', index=False)
