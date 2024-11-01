from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd
import time

from src.paths import DATA_DIR, STATES, URLS

# Wednesdays and Saturdays only
DEC_DAYS = ["4", "11", "18", "25", "7", "14", "21", "28"]
JAN_DAYS = ["1", "8", "15", "22", "29", "4", "11", "18", "25"]
FEB_DAYS = ["5", "12", "19", "26", "1", "8", "15", "22"]

DATES = {
    "2024-12": DEC_DAYS,
    "2025-1": JAN_DAYS,
    "2025-2": FEB_DAYS,
}


def scrape_page(url: str) -> pd.DataFrame:
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

    print(f"Successfully scraped {len(prices)} records")

    return pd.DataFrame({"title": titles, "price": prices, "rating": ratings})

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)


for month in DATES.keys():
    for day in DATES.get(month):
        for state, url in zip(STATES, URLS):
            file_path = DATA_DIR / f"{state}_{month}_{day}.csv"
            if file_path.exists():
                print(f"File {state}_{month}_{day}.csv exists locally already, try next URL")
                continue
            
            url_modified = url.replace(
                "checkin=2024-12-01&checkout=2024-12-02",
                f"checkin={month}-{int(day):02d}&checkout={month}-{int(day)+1:02d}",
            )

            try:
                time.sleep(10)
                driver.get(url_modified)
                print(f"Accessed URL for {state}, {month}-{day}  OK...")
            except:
                print(f"Can't access URL for {state}, {month}-{day}.")
                print("Trying next day...")
                continue
            
            titles, prices, ratings = [], [], []
            target_price_count = 100
            results = scrape_page(url=url_modified, quit_driver=False)

            df = pd.DataFrame(columns=["title", "price", "rating"])
            df = pd.concat([df, results])
            df['state'] = state
            df['year_month'] = month
            df['day'] = day

            df.to_csv(file_path, index=False)
            print(f"Scraped records for {state}, {month}-{day}, saved to {file_path}")

driver.quit()
