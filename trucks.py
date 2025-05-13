# Initialize truck and add attributes
class Truck:
    def __init__(self, truck_id, packages, depart_time, speed=18, capacity=16):
        self.truck_id = truck_id  # Truck name/identifier
        self.packages = packages  # List of package IDs assigned to the truck
        self.depart_time = depart_time  # Departure time
        self.speed = speed  # Truck speed
        self.start_address = "4001 South 700 East"  # Hub location as the starting point
        self.not_delivered = packages  # Packages yet to be delivered
        self.delivered = []  # List of delivered packages
        self.miles_traveled = 0.0  # Total miles traveled by the truck
        self.mileage_history = [(depart_time, 0.0)] # Mileage history
        self.current_time = depart_time  # Updated as deliveries are made
        self.end_address = "4001 South 700 East"  # Hub location to return to at the end of delivery

    # Returns the mileage of the truck at a given time.
    def get_mileage_at_time(self, time):
        last_mileage = 0.0
        for timestamp, mileage in self.mileage_history:
            if timestamp <= time:
                last_mileage = mileage
            else:
                break  # Stop checking once we go past the input time
        return last_mileage

    # Updates the current time by adding travel time.
    def update_current_time(self, travel_time):
        self.current_time += travel_time
        self.mileage_history.append((self.current_time, self.miles_traveled))  # Keeps mileage history updated

    # Simulate delivering a package, update truck time and mileage
    def deliver_package(self, package, travel_time):
        self.update_current_time(travel_time)
        self.not_delivered.remove(package)
        self.delivered.append(package)
        package.delivered_time = self.current_time  # Updates the package's delivery time








