#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from time import strftime

import requests_cache
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from data_manager import DataManager
from datetime import datetime, timedelta
from pprint import pprint
from notification_manager import NotificationManager
#========================Conserve requests and preserve ur free plan===================
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*sheety.co":requests_cache.DO_NOT_CACHE,
        "*":3600,
    }
)

#=======================datamanager=======================
# print(flights.search_result())
data=DataManager()
sheet_data=data.get_destination_data()
print(sheet_data)
#################flight_search#######################

tomorrow=datetime.now() +timedelta(days=1)
six_month_from_today=datetime.now()+timedelta(days=(6*30))

#================================Do flight SeARCH====================
for data in sheet_data['sheet1']:
    flight=FlightSearch()
    # for info in sheet_data:
    #     flight_result=flight.check_flights(info["City"],info["IATA Code"],info["prices"])
    #     print(flight_result)

    flights=flight.check_flights(origin_city_code=data["iataCode"],destination_city_code=data["destIataCode"],from_time=tomorrow,to_time=six_month_from_today)
    pprint(flights)

    #==========================show cheapest_flight========
    cheapest_flight=find_cheapest_flight(data=flights,return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{data['origin']}:BBP{cheapest_flight.price}")

    send=NotificationManager()
    send.send_message(cheapest_flight)

###################cutomer email#########
customers_email=data.get_customer_emails()
customers_email_list=[row["skitae@gmail.com"] for row in customers_email]
