#!/usr/bin/python
# -*- coding: utf-8 -*-

import cfscrape
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

EXCAHNGE_URL = 'https://rsbuddy.com/exchange/?id='
AIRORB_ID = '573'
UNPOWERED_ID = '567'
COSMIC_ID = '564'

# 0 is use buy price, 1 is use sell price

PRICE_TOGGLE = 0  # Debug
DEBUG = False
scraper = cfscrape.create_scraper()


def main():
    amount = raw_input('Amount to charge: ')
    profit = get_profit(amount)
    print "Profit of: " + str(profit)
    print "Run count: " + str(get_run_count(amount))

def get_run_count(amount):
	runs = int(amount) / 27
	return runs

def get_profit(amount, ao_id=AIRORB_ID):
    ao_price = get_prices(ao_id)
    total_cost = get_cost()
    profit = int(ao_price) - int(total_cost)
    multiplied_profit = int(amount) * profit
    return multiplied_profit


def get_cost(upo_id=UNPOWERED_ID, cosmic_id=COSMIC_ID, ao_id=AIRORB_ID):
    upo_cost = get_prices(upo_id)
    cosmic_cost = get_prices(cosmic_id)
    cast_cost = 3 * int(cosmic_cost)
    total_cost = int(cast_cost) + int(upo_cost)
    return total_cost


def get_prices(item_id):
    html = lookup_item(item_id)
    parsed_html = BeautifulSoup(html, features="lxml")
    buy_price = parsed_html.body.find('div', attrs={'id': 'buy-price'
            }).text
    sell_price = parsed_html.body.find('div', attrs={'id': 'sell-price'
            }).text
    if DEBUG:
        print item_id + ' has a buy price of ' + buy_price \
            + ' and a sell price of ' + sell_price
    if PRICE_TOGGLE == 0:
        return buy_price
    elif PRICE_TOGGLE == 1:
        return sell_price


def lookup_item(item_id):
    html = scraper.get(EXCAHNGE_URL + item_id).content
    if DEBUG:
        print 'Fetching item info: ' + EXCAHNGE_URL + item_id
    return html


if __name__ == '__main__':
    main()
