from hashtable import HashTable
from datetime import timedelta

## Creates a hash table with an initial size of 40 to store package information.
hashtable = HashTable(size=40)

# Initialize Package and add attributes
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.original_address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = "At Hub"
        self.departure_time = None
        self.delivered_time = None
        self.truck = None

    def package_status(self, lookup_time):
        # Handle package 9's address update
        if self.package_id == 9:
            # Convert input time string to timedelta for comparison
            if isinstance(lookup_time, str):
                hours, minutes = map(int, lookup_time.split(':'))
                lookup_time = timedelta(hours=hours, minutes=minutes)

            # Set correct address based on time
            if lookup_time >= timedelta(hours=10, minutes=20):
                self.address = "410 S State St"
                self.zip_code = "84111"
            else:
                self.address = "300 State St"
                self.zip_code = "84103"

        # Verifying times to assign status
        if self.delivered_time and lookup_time >= self.delivered_time:
            status = "Delivered!"
            time_info = f"{str(self.delivered_time)}"

        elif self.departure_time and lookup_time >= self.departure_time:
            status = "En Route"
            time_info = f"{str(self.departure_time)}"
        else:
            status = "At the Hub"
            time_info = f"{str(lookup_time)}"
        # Gets truck number
        truck_info = f"Truck {self.truck}" if self.truck else "Not assigned"

        # Returns details of package
        return (f" {truck_info} \t Package ID: {self.package_id} \t Address: {self.address} \t  "
                f"\t City: {self.city} \t Zip Code: {self.zip_code} \t Package Weight: {self.weight} kilograms"
                f"\t Status: {status} \t {time_info} \t Deadline: {self.deadline}")







