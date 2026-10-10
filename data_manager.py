import os
from requests.auth import HTTPBasicAuth
import requests
from datetime import datetime
from dotenv import load_dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.sheet_endpoint_sheet1="https://api.sheety.co/4f1d703060290b0e24ac1654f88b91a8/cheapFlights/sheet1"
        self.sheet_endpoint_users="https://api.sheety.co/4f1d703060290b0e24ac1654f88b91a8/cheapFlights/users"
        load_dotenv()
        self.USERNAME=os.getenv("USERNAME1")
        self.PASSWORD=os.getenv("PASSWORD")
        self.destination_data=[]
        self.users_list=[]
        self._authorization=HTTPBasicAuth(self.USERNAME,self.PASSWORD)
    def get_destination_data(self):
        response = requests.get(url=self.sheet_endpoint_sheet1,auth=self._authorization)
        data=response.json()
        self.destination_data=data
        print(self.destination_data)
        return self.destination_data

    def get_customer_emails(self):
        response=requests.get(url=self.sheet_endpoint_users,auth=self._authorization)
        data=response.json()
        self.users_list=data
        print(self.users_list)
        return self.users_list
    def update_lowest_price(self,row_id,new_price):
        new_data={"prices":{"lowestPrice":new_price}}
        requests.put(url=self.sheet_endpoint_sheet1,json=new_data,auth=self._authorization)




