import requests
from dotenv import load_dotenv
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("SERP_API_KEY")
        self.serp_endpoint=os.getenv("SERP_ENDPOINT")
    def check_flights(self,origin_city_code,destination_city_code,from_time,to_time):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date":from_time.strftime("%Y-%m-%d"),
            "return_date":to_time.strftime("%Y-%m-%d"),
            "currency": "INR",
            "type":"1",
            "adults":"1",
            "api_key":self.api_key
        }
        response=requests.get(self.serp_endpoint,params=params)
        if response.status_code!=200:
            print(f"check_flights code:{response.status_code}")
            return None
        data=response.json()
        if "error" in data:
            print(f"API error:{data['error']}")
            return None
        return data