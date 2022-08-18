from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

driver.get("https://www.amazon.fr/s?k=ordinateur+portable&sprefix=ordi%2Caps%2C106&ref=nb_sb_ss_ts-doa-p_1_4")

content = driver.page_source

soup = BeautifulSoup(content)

ordi_list = list(soup.findAll('div', attrs={'class',"sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20"})) + list(soup.findAll('div', attrs={'class',"sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"}))
print(len(ordi_list))

for article in ordi_list:
    name = article.find('span', attrs={'class',"a-size-base-plus a-color-base a-text-normal"})
    price = article.find('span', attrs={'class',"a-offscreen"})
    print(name.text)
    if price is not None:
        print(price.text)

