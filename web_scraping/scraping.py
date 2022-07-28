from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Código que faz o web scraping

driver = webdriver.Chrome(executable_path=r'C:\Users\Arthur - PC\Documents\Web_driver\chromedriver.exe')


def get_coin_value(coin):
    #Procura automaticamente o valor da moeda, sendo necessário passar o valor coin que é a moeda.
    driver.get('https://google.com')
    input = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input.send_keys(f'Cotação {coin}')

    button_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    button_search.send_keys(Keys.ENTER)

    coin_value = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
    return coin_value


def get_gold_value():
    #Pega o valor do ouro
    driver.get('https://www.melhorcambio.com/ouro-hoje')
    gold_value = driver.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value') 
    gold_value = gold_value.replace(',', '.')
    return gold_value



dolar = get_coin_value('dolar')
euro = get_coin_value('euro')
gold = get_gold_value()

driver.quit()