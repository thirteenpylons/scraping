"""
Web scraper for www.nationaltoday.com.

Author: Christian M. Fulton
Date: 01.May.24
"""

import requests
import argparse
import sys
from typing import List, Tuple
from bs4 import BeautifulSoup
from mlib.parser import parse_holidays

def execute(args=None) -> None:
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Web scraper")
    parser.add_argument("-u", "--url", type=str, help="Enter the URL that you want to scrape.")
    parsed_args, _ = parser.parse_known_args(args)

    if not parsed_args.url:
        print("URL required. Use -u <url> to specify.")
        return

    scrape_data(parsed_args.url)

def scrape_data(url: str) -> None:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching the URL: {url}")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    holidays = parse_holidays(soup)

    print(f"Holidays scraped from {url}:")

    for day, holiday_titles in holidays:
        print(f"- {day}:")
        for title in holiday_titles:
            print(f"  - {title}")

if __name__ == "__main__":
    execute()
