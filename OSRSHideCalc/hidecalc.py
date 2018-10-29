#!/usr/bin/python
# -*- coding: utf-8 -*-

import cfscrape
import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

DEBUG = True
PRICE_TOGGLE = 0
EXCAHNGE_URL = 'https://rsbuddy.com/exchange/?id='

GREEN = ["Green Dragonhide", 1753, 1745]
BLUE = ["Blue Dragonhide", 1751, 2505]
RED = ["Red Dragonhide", 1749, 2507]
BLACK = ["Black Dragonhide", 1747, 2509]

COLORS = [GREEN, BLUE, RED, BLACK]

TAN_COST = 20

scraper = cfscrape.create_scraper()

def main():
    data = get_profit()
    make_graph(data)

def get_profit():
    profits = []
    for COLOR in COLORS:
        name = COLOR[0]
        hide_price = get_prices(COLOR[1])
        leather_price = get_prices(COLOR[2])
        profit = int(leather_price) - int(hide_price) - int(TAN_COST)
        profits.append(profit)
        print "[" + name + "] " + "Profit: " + str(profit)
    return profits


def make_graph(y):
    x = ['Green', 'Blue', 'Red', 'Black']
    y_pos = np.arange(len(x))

    plt.bar(y_pos, y, align='center', alpha=0.5)
    plt.xticks(y_pos, x)
    plt.ylabel('Profit')
    plt.title('Profit per tanned hide')
    plt.savefig("hide-profit.png")

def get_prices(item_id):
    html = lookup_item(item_id)
    parsed_html = BeautifulSoup(html, features="lxml")
    buy_price = parsed_html.body.find('div', attrs={'id': 'buy-price'
                                                    }).text
    sell_price = parsed_html.body.find('div', attrs={'id': 'sell-price'
                                                     }).text
    if PRICE_TOGGLE == 0:
        return buy_price
    elif PRICE_TOGGLE == 1:
        return sell_price


def lookup_item(item_id):
    html = scraper.get(EXCAHNGE_URL + str(item_id)).content
    if DEBUG:
        print "Fetching html for item " + str(item_id)
    return html

if __name__ == '__main__':
    main()
