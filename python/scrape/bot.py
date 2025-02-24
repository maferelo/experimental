import datetime
import time
import json

from seleniumwire.utils import decode
from seleniumwire import webdriver
from urllib.parse import urlencode

ALIEXPRESS_URL = "https://best.aliexpress.com/"
ALIEXPRESS_US_LOCALE_COOKIE = {
    "name": "aep_usuc_f",
    "value": "site=glo&c_tp=USD&b_locale=en_US",
    "domain": ".aliexpress.com"
}
ALIEXPRESS_CATEGORIES_API = "mtop.relationrecommend.aliexpressrecommend.recommend"
ALIEXPRESS_CATEGORY_URL = "https://www.aliexpress.com/p/calp-plus/index.html?"
ALIEXPRESS_CATEGORY_URL_PARAMS = {'categoryTab': ""}


def delay(func):
    def wrapper(*args, **kwargs):
        time.sleep(5)
        return func(*args, **kwargs)
    return wrapper

def screenshot(func):
    def wrapper(*args, **kwargs):
        args[0].save_screenshot("screenshot.png")
        return func(*args, **kwargs)
    return wrapper

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    return webdriver.Chrome(options=options)

@delay
@screenshot
@log
def set_driver_aliexpress_cookie_locale(driver):
    driver.get(ALIEXPRESS_URL)
    driver.add_cookie(ALIEXPRESS_US_LOCALE_COOKIE)
    del driver.requests

@log
def get_driver_api_request(driver, api):
    responses = []
    for request in driver.requests:
        if request.response and api in request.url:
            body = json.loads(decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')))
            responses.append(body)
    return responses

@delay
@screenshot
@log
def get_categories(driver, filename="categories.json"):
    try:
        categories = load_json_data(filename)
    except FileNotFoundError:
        driver.get(ALIEXPRESS_URL)
        requests = get_driver_api_request(driver, ALIEXPRESS_CATEGORIES_API)
        categories = get_categories_from_api_request(requests)
        save_json_to_file(categories, filename)
    return categories

@log
def get_categories_from_api_request(responses):
    for response in responses:
        if "data" in response and "data" in response["data"] and "categoryTabs" in response["data"]["data"]:
            print(f"Found {len(response['data']['data']['categoryTabs']['items'])} categories")
            return response["data"]["data"]["categoryTabs"]["items"]
    raise Exception("Categories not found")

@log
def load_json_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

@screenshot
@delay
@log
def visit_category(driver, category):
    params = ALIEXPRESS_CATEGORY_URL_PARAMS.copy()
    params["categoryTab"] = category["id"]
    driver.get(ALIEXPRESS_CATEGORY_URL + urlencode(params))
    for i in range(3):
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


@log
def visit_categories(driver, categories):
    for category in categories:
        visit_category(driver, category)

@log
def get_products_from_api_request(responses):
    products = []
    for response in responses:
        if "data" in response["data"] and "fountainListInfo" in response["data"]["data"]:
            products.extend(response["data"]["data"]["fountainListInfo"]["mods"]["itemList"]["content"])
    return products

@log
def add_timestamp_to_products(products):
    for product in products:
        product["timestamp"] = datetime.datetime.now().isoformat()
    return products

@delay
@screenshot
@log
def get_products_from_categories(driver, categories):
    visit_categories(driver, categories)
    requests = get_driver_api_request(driver, ALIEXPRESS_CATEGORIES_API)
    products = get_products_from_api_request(requests)
    save_json_to_file(products, "products.json")
    return add_timestamp_to_products(products)

@log 
def save_json_to_file(data, filename, append=False):
    if append:
        load_json_data(filename)
        data.extend(load_json_data(filename))
    with open(filename,"w") as file:
        json.dump(data, file)

def main() -> None:
    driver = get_driver()
    set_driver_aliexpress_cookie_locale(driver)
    categories = get_categories(driver)
    products = get_products_from_categories(driver, categories)
    print(f"Found {len(products)} products")
    driver.quit()


if __name__ == "__main__":
    main()