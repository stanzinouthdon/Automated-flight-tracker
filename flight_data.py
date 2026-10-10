
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price,origin,destination,out_date,return_date):
        self.price=price
        self.origin_airport=origin
        self.destination_airport=destination
        self.out_date=out_date
        self.return_date=return_date
def find_cheapest_flight(data,return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("no flight data")
        return FlightData("N/A","N/A","N/A","N/A","N/A")

    all_flight=data.get("best_flights",[])+data.get("other_flights",[])
    min_price = all_flight[0]["price"]
    best_flight=all_flight[0]
    for flight in all_flight:
        try:
            price=flight["price"]
        except KeyError:
            print(" no flights available")
            continue
        if price< min_price:
            min_price=price
            best_flight=flight

    price=min_price
    origin_airport=best_flight["flights"][0]["departure_airport"]["id"]
    destination_airport=best_flight["flights"][0]["arrival_airport"]["id"]
    out_date=best_flight["flights"][0]["departure_airport"]["time"]
    return_date=best_flight["flights"][0]["departure_airport"]["time"]
    cheapest_flight= FlightData(price,origin_airport,destination_airport,out_date,return_date)
    return cheapest_flight
