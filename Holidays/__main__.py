"""
Entry point for the scraper program.

Author: Christian M. Fulton
Date: 01.May.24
"""

import sys
import argparse
from Holidays.app import scrape_data
from mlib.query import query_by_date

def main():
    parser = argparse.ArgumentParser(description="Web scraper")

    # Either accept a URL directly or a month to generate a URL
    parser.add_argument("-u", "--url", type=str, help="URL to scrape.")
    parser.add_argument("-m", "--month", type=str, help="Month to scrape holidays for.")
    parser.add_argument("-d", "--date", type=str, help="Date to query holidays for.")
    parser.add_argument("-c", "--csv", type=str, help="CSV file to save to or query from.")

    args = parser.parse_args()

    # Create a URL if a month is specified
    if args.month:
        month = args.month.lower()
        args.url = f"https://nationaltoday.com/{month}-holidays/"
    
    if args.date and args.csv:
        holidays = query_by_date(args.csv, args.date)

        print(f"Holidays on {args.date}:")
        for holiday in holidays:
            print(f"- {holiday}")
    elif args.url and args.csv:
        scrape_data(args.url, args.csv)
    else:
        print("Specify either a URL and CSV to scrape to, or a CSV and date to query.")


if __name__ == "__main__":
    main()
