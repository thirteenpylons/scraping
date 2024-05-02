import csv
from typing import List


def query_by_date(file_path: str, date: str) -> List[str]:
    """
    Queries holidays from a CSV file for a specific date.

    :param file_path: the path to the CSV file.
    :param data: The date to query holidays for (e.g., "May 1").
    :return: List of holidays found on the specified date.
    """
    holidays = []

    with open(file_path, mode="r") as holidays_csv:
        reader = csv.DictReader(holidays_csv)

        for row in reader:
            if row["Date"] == date:
                holidays.append(row["Holiday"])
    
    return holidays