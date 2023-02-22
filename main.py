import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from links import HEADER, URL , FORM_URL


response = requests.get(URL , headers=HEADER)
data = response.text

#print(data)
soup = BeautifulSoup(data , "html.parser")


property_price = soup.find_all("span" , {'data-test' : 'property-card-price'})
rates = [rate.get_text().split("+")[0] for rate in property_price ]

property_address = soup.find_all("address" , {'data-test' : 'property-card-addr'})
addresses = [address.get_text() for address in property_address]

property_links = soup.find_all("a" , {'data-test' : 'property-card-link'})
all_links = []
for link in property_links:
    href = link["href"]
    #print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)



#print(rates)
#print(addresses)
#print(all_links)

chrome_driver_path = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

for n in range(len(all_links)):
    # Substitute your own Google Form URL here 👇
    driver.get(FORM_URL)

    address_fill = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price_fill = driver.find_element(By.XPATH , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link_fill = driver.find_element(By.XPATH , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_button = driver.find_element(By.XPATH , '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')


    address_fill.send_keys(addresses[n])
    price_fill.send_keys(rates[n])
    link_fill.send_keys(all_links[n])
    submit_button.click()

    

