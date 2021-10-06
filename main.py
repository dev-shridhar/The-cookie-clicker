from selenium import webdriver
import time

chrome_driver_path = "F:/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_css_selector("#cookie")
money = int(driver.find_element_by_css_selector("#money").text)
all_price = driver.find_elements_by_css_selector("#store b")

store = {}

for price in all_price:
    element_price = price.text
    if element_price != "":
        cost = int(element_price.split("-")[1].strip().replace(",", ""))
        element = element_price.split("-")[0].strip()
        store[element] = cost


def get_money():
    return int(driver.find_element_by_css_selector("#money").text)


Factory = driver.find_element_by_id("buyFactory")
Factory.click()

test = 5

while True:
    timeout = time.time() + 10  # 10 seconds from now
    while True:
        cookie.click()
        if time.time() > timeout:
            break
        for i in store:
            if money >= store[i]:
                i = driver.find_element_by_id(f"buy{i}")
                i.click()

    test = test - 1

    print(get_money())