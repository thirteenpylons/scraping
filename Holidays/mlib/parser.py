"""
Functions for parsing and processing webpage content.

Author: Christian M. Fulton
Date: 01.May.24

"""

from typing import List, Tuple
from bs4 import BeautifulSoup

def parse_holidays(soup: BeautifulSoup) -> List[Tuple[str, List[str]]]:
    """
    Parses a BeautifulSoup object representing a month's holidays page.

    :param soup: BeautifulSoup object containing the webpage content.
    :return: List of tuples containing day and holiday information.
    """
    holidays = []

    # Extract all rows with day and holiday data
    day_rows = soup.find_all('tr', class_="row-header row-days")

    for row in day_rows:
        # Extract the date and day information
        date_cell = row.find('td', class_="date")
        if not date_cell:
            continue

        event_wrapper = date_cell.find('div', class_="event-wrapper")
        if not event_wrapper:
            continue

        # Extract the date link
        date_link = event_wrapper.find('a')
        date_text = date_link.get_text(strip=True) if date_link else "Unknown Date"

        # Extract the day name
        day_span = event_wrapper.find('span', class_="event-day")
        day_text = day_span.get_text(strip=True) if day_span else "Unknown Day"

        # Extract all holidays related to this day
        holiday_rows = row.find_next_siblings('tr', class_="row-data")
        holiday_titles = []

        for holiday_row in holiday_rows:
            title_cell = holiday_row.find('td', class_="title")
            if title_cell:
                holiday_link = title_cell.find('a')
                holiday_text = holiday_link.get_text(strip=True) if holiday_link else "Unknown Holiday"
                holiday_titles.append(holiday_text)

            # Break the loop if we encounter another day row
            if holiday_row.find('td', class_="date"):
                break

        holidays.append((f"{date_text} ({day_text})", holiday_titles))

    return holidays
