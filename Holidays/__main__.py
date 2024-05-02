"""
Entry point for the scraper program.

Author: Christian M. Fulton
Date: 01.May.24
"""

import sys
import argparse
from Holidays.app import scrape_data

def main():
    parser = argparse.ArgumentParser(description="Web scraper")

    # Either accept a URL directly or a month to generate a URL
    parser.add_argument("-u", "--url", type=str, help="URL to scrape.")
    parser.add_argument("--month", type=str, help="Month to scrape holidays for.")

    args = parser.parse_args()

    # Create a URL if a month is specified
    if args.month:
        month = args.month.lower()
        args.url = f"https://nationaltoday.com/{month}-holidays/"

    # Check if there's a valid URL
    if not args.url:
        print("URL required. Use -u <url> or --month <month> to specify.")
        return

    # Call the scraping function with the final URL
    scrape_data(args.url)

if __name__ == "__main__":
    main()
