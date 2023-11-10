from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

_service = Service()
_options = Options()
driver = webdriver.Chrome(service=_service, options=_options)

# ------------------------------------------------------------- #

from itertools import chain, product
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(4, maxlength + 1)))

# ------------------------------------------------------------- #

def main():

    for gt in bruteforce('abcdefghijklmnopqrstuvwxyz', 6):

        # the check 'again' page redirects to the main page
        driver.get("https://www.gamertagavailability.com")

        time.sleep(2)
        search = driver.find_element(By.XPATH, '//*[@id="mytag"]')
        time.sleep(3)
        search.send_keys(gt)
        search.send_keys(Keys.RETURN)

        try:
            result = driver.find_element(By.XPATH, '//*[@id="nres"]/p[2]').text
            time.sleep(2)
        except:
            # since the try block failed, the 'not available' message
            # was not found, so the gamertag is available and there
            # is no need to check for the 'available' message
            print('Gamertag ' + gt + ' is available!')
            time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()
