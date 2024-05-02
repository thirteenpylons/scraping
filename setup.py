from setuptools import setup

setup(
    name="holiday_scraper",
    version="1.0",
    packages=["Holidays", "mlib"],
    entry_points={
        "console_scripts": [
            "holiday_scraper = Holidays.__main__:main",
        ],
    },
    install_requires=["requests", "beautifulsoup4"],
)
