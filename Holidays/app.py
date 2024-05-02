"""
Web scraper for www.nationaltoday.com.

Author: Christian M. Fulton
Date: 01.May.24
"""
import requests
import sys
import os
import argparse
import csv
from typing import List, Tuple
from bs4 import BeautifulSoup
from mlib.parser import parse_holidays


def execute(args=None) -> None:
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Web scraper")
    parser.add_argument("-u", "--url", type=str, help="Enter the URL that you want to scrape.")
    parser.add_argument("--output", type=str, help="File path to save the extracted data.")
    parsed_args, _ = parser.parse_known_args(args)

    if not parsed_args.url:
        print("URL required. Use -u <url> to specify.")
        return

    scrape_data(parsed_args.url, parsed_args.output)

def scrape_data(url: str, output_file: str = None) -> None:
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

    # Write to a CSV file if specified
    if output_file:
        write_to_csv(holidays, output_file)

def write_to_csv(data: List[Tuple[str, List[str]]], output_file: str) -> None:
    """
    Writes the extracted data to a CSV file.

    :param data: List of tuples containing day and holiday information.
    :param output_file: The file path to write the data to.
    """
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["Date", "Day", "Holiday"])

        # Write each row of extracted data
        for date_day, holidays in data:
            date, day = date_day.split(" (")
            day = day.strip(")")

            # Write each holiday in a separate row
            for holiday in holidays:
                writer.writerow([date, day, holiday])

if __name__ == "__main__":
    sys.path.append(os.path.dirname(__file__))
    execute()
