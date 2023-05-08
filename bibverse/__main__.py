#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


def main():
    text = requests.get("https://www.verseoftheday.com/").text
    soup = BeautifulSoup(text, "html.parser")
    result = soup.find_all("div", "bilingual-left")[0].get_text()
    print(result)
