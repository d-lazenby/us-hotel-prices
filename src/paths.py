from pathlib import Path
import os

PARENT_DIR = Path(__file__).parent.resolve().parent

DATA_DIR = PARENT_DIR / "data"
OXFORD_DATA_DIR = PARENT_DIR / "oxford_data"
DASHBOARD_DATA_DIR = PARENT_DIR / "dashboard_data"

if not Path(DATA_DIR).exists():
    os.mkdir(DATA_DIR)

if not Path(OXFORD_DATA_DIR).exists():
    os.mkdir(OXFORD_DATA_DIR)

if not Path(DASHBOARD_DATA_DIR).exists():
    os.mkdir(DASHBOARD_DATA_DIR)


STATES = [
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "NewHampshire",
    "NewJersey",
    "NewMexico",
    "NewYork",
    "NorthDakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "RhodeIsland",
    "SouthCarolina",
    "SouthDakota",
    "Tennessee",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "WestVirginia",
    "Wisconsin",
    "Wyoming",
]

STATE_MAPPING = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "NewHampshire": "NH",
    "NewJersey": "NJ",
    "NewMexico": "NM",
    "NewYork": "NY",
    "NorthCarolina": "NC",
    "NorthDakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "RhodeIsland": "RI",
    "SouthCarolina": "SC",
    "SouthDakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "WestVirginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}


URLS = [
    f"https://www.booking.com/searchresults.en-gb.html?ss=Wyoming%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3020&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=893e95abc74f0087&ac_meta=GhA4OTNlOTVhYmM3NGYwMDg3IAAoATICZW46BVd5b21pQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0"
    f"https://www.booking.com/searchresults.en-gb.html?ss=Wisconsin%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3019&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=2141959a5c6800d7&ac_meta=GhAyMTQxOTU5YTVjNjgwMGQ3IAEoATICZW46B1dpc2NvbnNAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=West+Virginia%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3018&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=47ef95874c8a01ad&ac_meta=GhA0N2VmOTU4NzRjOGEwMWFkIAAoATICZW46DXdlc3QgdmlyZ2luaWFAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Washington%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=1155&dest_type=region&ac_position=4&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=86ed956cd51d01a4&ac_meta=GhA4NmVkOTU2Y2Q1MWQwMWE0IAQoATICZW46Cldhc2hpbmd0b25AAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Virginia%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2463&dest_type=region&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=bcd1955af11215cc&ac_meta=GhBiY2QxOTU1YWYxMTIxNWNjIAEoATICZW46CFZpcmdpbmlhQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Vermont%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=2471&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=483d95487add004f&ac_meta=GhA0ODNkOTU0ODdhZGQwMDRmIAAoATICZW46BlZlcm1vbkAASgBQAA%3D%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Utah%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3017&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=c8269532835503c8&ac_meta=GhBjODI2OTUzMjgzNTUwM2M4IAAoATICZW46BFV0YWhAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Tennessee%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3016&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=6f0a9518c4d20335&ac_meta=GhA2ZjBhOTUxOGM0ZDIwMzM1IAAoATICZW46CVRlbm5lc3NlZUAASgBQAA%3D%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=South+Dakota%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3015&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=524094f19972002f&ac_meta=GhA1MjQwOTRmMTk5NzIwMDJmIAAoATICZW46CVNvdXRoIERha0AASgBQAA%3D%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=South+Carolina%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=8ff74c491f5acb5d5cbe3c5ba7a99c0d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3014&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=38a494de15cd00be&ac_meta=GhAzOGE0OTRkZTE1Y2QwMGJlIAAoATICZW46DlNvdXRoIENhcm9saW5hQABKAFAA&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
    f"https://www.booking.com/searchresults.en-gb.html?ss=Rhode+Island%2C+United+States&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApTkj7kGwAIB0gIkYWQ4MjBlOWItN2M5NS00MmE2LWIyZDctYTA3MTJiNmQ1ZDRh2AIF4AIB&sid=2794f1fe1e5c6e6f9ea8f34e3dde050d&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=3013&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=525294caa3b0039c&ac_meta=GhA1MjUyOTRjYWEzYjAwMzljIAAoATICZW46B1Job2RlIElAAEoAUAA%3D&checkin=2024-12-01&checkout=2024-12-02&group_adults=2&no_rooms=1&group_children=0",
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
