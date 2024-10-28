from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time

from src.paths import DATA_DIR

def initial_search(state: str, year_month: str, day: str, timeout: int = 20):

    WebDriverWait(driver, 60).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    destination = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-destination="1"]'))
    )
    time.sleep(1)
    destination.send_keys(f"{state}, United States", Keys.TAB, Keys.TAB)

    time.sleep(2)
    year_month = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'select[data-name="year-month"]'))
    )
    time.sleep(1)
    select_year_month = Select(year_month)
    time.sleep(1)
    select_year_month.select_by_value(f"{year_month}")

    time.sleep(2)
    day = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'select[data-name="day"]'))
        )
    time.sleep(1)
    select_day = Select(day)
    time.sleep(1)
    select_day.select_by_value(f"{day}")

    time.sleep(2)
    search = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    search.click()


def scrape_page(url: str, quit_driver: bool = False) -> pd.DataFrame:
    # Scroll and scrape prices until the target count is reached
    while len(prices) < target_price_count:
        # Scrape the currently visible prices
        title_elements = driver.find_elements(
            By.CSS_SELECTOR,
            'div[data-testid="property-card"] div[data-testid="title"]',
        )

        time.sleep(2)
        price_elements = driver.find_elements(
            By.CSS_SELECTOR,
            'div[data-testid="property-card"] span[data-testid="price-and-discounted-price"]',
        )

        time.sleep(2)
        rating_elements = driver.find_elements(
            By.CSS_SELECTOR,
            'div[data-testid="property-card"] div[class="a3b8729ab1 d86cee9b25"]',
        )

        for t, p, r in zip(title_elements, price_elements, rating_elements):
            titles.append(t.text)
            prices.append(p.text)
            ratings.append(r.text)

        # Scroll down the page to load more results
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the next batch of results to load
        time.sleep(2)

    if quit_driver:
        driver.quit()

    print(f"Successfully scraped {len(prices)} records")

    return pd.DataFrame({"title": titles, "price": prices, "rating": ratings})

DEC_DAYS = ["4", "11", "18", "25", "7", "14", "21", "28"]
JAN_DAYS = ["1", "8", "15", "22", "29", "4", "11", "18", "25"]
FEB_DAYS = ["5", "12", "19", "26", "1", "8", "15", "22"]

DATES = {
    "2024-12": DEC_DAYS,
    "2025-1": JAN_DAYS,
    "2025-2": FEB_DAYS,
}


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
# driver.get("https://www.booking.com/")


# parent = driver.current_window_handle
# uselessWindows = driver.window_handles
# for winId in uselessWindows:
#     if winId != parent:
#         driver.switch_to.window(winId)
#         driver.close()


# 1. MAKE SEARCH
# initial_search(state=state, year_month=y_m, day=d)

# 2. SCRAPE PRICES

state = "Nevada"
for month in DATES.keys():
    for day in DATES.get(month):
        
        url = f"https://www.booking.com/searchresults.en-gb.html?ss=nevada%2C+united+states&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApCU-LgGwAIB0gIkMzA0ZGY2ZDMtYTcxOC00MWNmLWI0NDItODY0MDE4OWVjODU02AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2326&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=d7cd909ec9db0708&ac_meta=GhBkN2NkOTA5ZWM5ZGIwNzA4IAAoATICZW46FW5ldmFkYSwgdW5pdGVkIHN0YXRlc0AASgBQAA%3D%3D&checkin={month}-{int(day):02d}&checkout={month}-{int(day)+1:02d}&group_adults=2&no_rooms=1&group_children=0"
        try:
            time.sleep(10)
            driver.get(url)
            print(f"Accessed URL for {state}, {month}-{day}  OK...")
        except:
            driver.quit()
            print(f"Can't access URL for {state}, {month}-{day}.")
            print("Trying next day...")
            continue
        titles, prices, ratings = [], [], []
        target_price_count = 100
        results = scrape_page(url=url, quit_driver=False)

        # 3. SAVE RESULTS
        df = pd.DataFrame(columns=["title", "price", "rating"])
        df = pd.concat([df, results])
        df['state'] = state
        df['year_month'] = month
        df['day'] = day

        file_path = DATA_DIR / f"{state}_{month}_{day}.csv"

        df.to_csv(file_path, index=False)
        print(f"Scraped records for {state}, {month}-{day}, saved to {file_path}")

driver.quit()
