from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time
from pathlib import Path

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
# chrome_options.add_experimental_option("detach", True)
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


# 2. SCRAPE PRICES

states = [
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", 
    "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Minnesota", "Mississippi", "Missouri", "Montana", 
    "Nebraska", "NewHampshire", "NewJersey", "NewMexico", "NewYork", "NorthDakota", "Ohio", "Oklahoma", 
    "Oregon", "RhodeIsland", "SouthCarolina", "SouthDakota", "Tennessee", "Utah", "Vermont", "Virginia", "Washington",
    "WestVirginia", "Wisconsin", "Wyoming"
]

scraped = [
    "Michigan",
    "Nevada",
    "Pennsylvania",
    "Texas",
    "Arizona",
    "NorthCarolina",
    "Alabama",
    "Alaska",
    "Arkansas",
    "California",
    "Colorado",
]

states_to_scrape = [
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", 
    "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Minnesota", "Mississippi", "Missouri", "Montana", 
    "Nebraska", "NewHampshire", "NewJersey", "NewMexico", "NewYork", "NorthDakota", "Ohio", "Oklahoma", 
    "Oregon"
]

urls_to_scrape = [
    f"https://www.booking.com/searchresults.en-gb.html?ss=Connecticut%2C+united+states&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2994&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=661c8445035d03c5&ac_meta=GhA2NjFjODQ0NTAzNWQwM2M1IAAoATICZW46GkNvbm5lY3RpY3V0LCB1bml0ZWQgc3RhdGVzQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Delaware%2C+united+states&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2995&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=721984907fa903a8&ac_meta=GhA3MjE5ODQ5MDdmYTkwM2E4IAAoATICZW46F0RlbGF3YXJlLCB1bml0ZWQgc3RhdGVzQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Florida%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=1136&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3c7d84b0e970008e&ac_meta=GhAzYzdkODRiMGU5NzAwMDhlIAAoATICZW46DkZsb3JpZGEsIHVuaXRlQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Georgia%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2475&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=c826850a73a207f2&ac_meta=GhBjODI2ODUwYTczYTIwN2YyIAAoATICZW46D0dlb3JnaWEsIHVuaXRlZEAASgBQAA%3D%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Hawaii%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2996&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=d349854a42d0013d&ac_meta=GhBkMzQ5ODU0YTQyZDAwMTNkIAAoATICZW46Ckhhd2FpaSwgdW5AAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Idaho%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2997&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=4f24855f4f6d052e&ac_meta=GhA0ZjI0ODU1ZjRmNmQwNTJlIAEoATICZW46BUlkYWhvQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Illinois%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2443&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=d50386473709051a&ac_meta=GhBkNTAzODY0NzM3MDkwNTFhIAAoATICZW46CklsbGlub2lzLCBAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Indiana%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2998&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=d34986636b1e022b&ac_meta=GhBkMzQ5ODY2MzZiMWUwMjJiIAEoATICZW46B0luZGlhbmFAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Iowa%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2999&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=7b4f867dc7a801bf&ac_meta=GhA3YjRmODY3ZGM3YTgwMWJmIAEoATICZW46BElvd2FAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Kansas%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3000&dest_type=region&ac_position=2&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=ca84869c432e049a&ac_meta=GhBjYTg0ODY5YzQzMmUwNDlhIAIoATICZW46BkthbnNhc0AASgBQAA%3D%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Kentucky%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3001&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=450486b7ff56041f&ac_meta=GhA0NTA0ODZiN2ZmNTYwNDFmIAAoATICZW46DUtlbnR1Y2t5LCB1bmlAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Louisiana%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2934&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=486686d2819d03ec&ac_meta=GhA0ODY2ODZkMjgxOWQwM2VjIAEoATICZW46C0xvdWlzaWFuYSwgQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Maine%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3002&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=4e3b86ec8f6308fe&ac_meta=GhA0ZTNiODZlYzhmNjMwOGZlIAEoATICZW46BU1haW5lQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Maryland%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2328&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=6d718706e3940a50&ac_meta=GhA2ZDcxODcwNmUzOTQwYTUwIAAoATICZW46CE1hcnlsYW5kQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Massachusetts%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2442&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=0ef9871bee7a04e1&ac_meta=GhAwZWY5ODcxYmVlN2EwNGUxIAAoATICZW46DU1hc3NhY2h1c2V0dHNAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Minnesota%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3004&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=50ed8737795a047c&ac_meta=GhA1MGVkODczNzc5NWEwNDdjIAAoATICZW46CU1pbm5lc290YUAASgBQAA%3D%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Mississippi%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3005&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=893e874e60860337&ac_meta=GhA4OTNlODc0ZTYwODYwMzM3IAAoATICZW46C01pc3Npc3NpcHBpQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Missouri%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2935&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=95ff878c74ab02e9&ac_meta=GhA5NWZmODc4Yzc0YWIwMmU5IAAoATICZW46CE1pc3NvdXJpQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Montana%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3234&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=01ee87a8a91f042a&ac_meta=GhAwMWVlODdhOGE5MWYwNDJhIAEoATICZW46B01vbnRhbmFAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Nebraska%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3006&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=427d87eaf8cb0393&ac_meta=GhA0MjdkODdlYWY4Y2IwMzkzIAAoATICZW46CE5lYnJhc2thQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=New+Hampshire%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2604&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b705882c682e0247&ac_meta=GhBiNzA1ODgyYzY4MmUwMjQ3IAAoATICZW46DU5ldyBIYW1wc2hpcmVAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=New+Jersey%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2616&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=a6f18855853004c8&ac_meta=GhBhNmYxODg1NTg1MzAwNGM4IAAoATICZW46CU5ld0plcnNleUAASgBQAA%3D%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=New+Mexico%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3007&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=2454886dde6900f7&ac_meta=GhAyNDU0ODg2ZGRlNjkwMGY3IAAoATICZW46CU5ld01leGljb0AASgBQAA%3D%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=New+York+State&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIG4AIB&sid=2794f1fe1e5c6e6f9ea8f34e3dde050d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=20088325&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=685288d7b6d80648&ac_meta=GhA2ODUyODhkN2I2ZDgwNjQ4IAAoATICZW46Dk5ldyBZb3JrIFN0YXRlQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=North+Dakota%2C+United+States&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIG4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3009&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=1a9f891bf633042d&ac_meta=GhAxYTlmODkxYmY2MzMwNDJkIAAoATICZW46C05vcnRoRGFrb3RhQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Ohio%2C+United+States&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIG4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3010&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b3c9893c4ea602f7&ac_meta=GhBiM2M5ODkzYzRlYTYwMmY3IAAoATICZW46BE9oaW9AAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Oklahoma%2C+United+States&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIG4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3011&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=b4ed895728700339&ac_meta=GhBiNGVkODk1NzI4NzAwMzM5IAEoATICZW46CE9rbGFob21hQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Oregon%2C+United+States&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4Au7RhLkGwAIB0gIkZTg3ZTg3NjEtMTk1ZC00ZGNmLTlkYzgtYzAzNjg1MmUzNWY42AIG4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3012&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=1e6f89818df9063c&ac_meta=GhAxZTZmODk4MThkZjkwNjNjIAEoATICZW46Bk9yZWdvbkAASgBQAA%3D%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
]


for month in DATES.keys():
    for day in DATES.get(month):
        for state, url in zip(states_to_scrape, urls_to_scrape):
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

            # 3. SAVE RESULTS
            df = pd.DataFrame(columns=["title", "price", "rating"])
            df = pd.concat([df, results])
            df['state'] = state
            df['year_month'] = month
            df['day'] = day

            df.to_csv(file_path, index=False)
            print(f"Scraped records for {state}, {month}-{day}, saved to {file_path}")

driver.quit()
