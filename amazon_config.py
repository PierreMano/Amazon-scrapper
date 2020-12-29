from selenium import webdriver 

DIRECTORY = 'reports'
NAME = 'THINKPAD X1 CARBON GEN 7'
CURRENCY ='€'
MIN_PRICE = '200'
MAX_PRICE = '1000'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "http://www.amazon.de/"


def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver/chromedriver.exe', chrome_options= options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def  set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito') 