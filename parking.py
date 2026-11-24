import sys

class VehicleParking:

    def __init__(self, customer_name, vehicle_number, vehicle_type, parking_hours):
        self.customer_name = customer_name
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type.lower()
        self.parking_hours = int(parking_hours)

    def calculate_charge(self):
        if self.vehicle_type == "bike":
            rate = 20
        elif self.vehicle_type == "car":
            rate = 50
        else:
            rate = 30

        return rate * self.parking_hours

    def display_details(self):
        print("\n===== Vehicle Parking Management System =====")
        print("Customer Name:", self.customer_name)
        print("Vehicle Number:", self.vehicle_number)
        print("Vehicle Type:", self.vehicle_type)
        print("Parking Hours:", self.parking_hours)
        print("Parking Charge: Rs.", self.calculate_charge())
        print("============================================")


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python parking.py name number type hours")
        sys.exit(1)

    name = sys.argv[1]
    number = sys.argv[2]
    vehicle_type = sys.argv[3]
    hours = sys.argv[4]

    if not hours.isdigit() or int(hours) <= 0:
        print("Invalid parking hours")
        sys.exit(1)

    parking = VehicleParking(name, number, vehicle_type, hours)
    parking.display_details()