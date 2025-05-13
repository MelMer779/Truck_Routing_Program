from datetime import timedelta
from trucks import Truck
from hashtable import HashTable
from imported_data import *


# Creates an instance of HashTable
package_table = HashTable()

# Inserts packages into the package_table
for package in packages:
    package_table.insert(package)

# Manually load trucks with packages and set departure times
truck_one = Truck(1, [13, 14, 15, 16, 19, 20, 1, 29, 30, 31, 34, 37, 40],
                  timedelta(hours=8, minutes=0, seconds=0))
truck_two = Truck(2, [3, 6, 18, 25, 28, 32, 36, 38, 27, 35, 39],
                  timedelta(hours=9, minutes=5, seconds=0))
truck_three = Truck(3, [9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 33],
                    timedelta(hours=9, minutes=54, seconds=0))


# Lookup the index of an address from the address data
def address_lookup(address):
    return addresses.index(address)

# Get the distance between two addresses using the distance table
def distance_between(address1, address2):
    return float(distances[address_lookup(address1)][address_lookup(address2)])


# Finds the minimum distance from the truck's current location to the next package
# Returns a sorted list of package IDs in the best order
def get_sorted_route(truck):
    if not truck.not_delivered:
        return []

    remaining_packages = truck.not_delivered[:]
    sorted_route = []
    current_address = truck.start_address

    while remaining_packages:
        nearest_package_id = None
        min_dist = float("inf")

        for package_id in remaining_packages:
            package = package_table.search(package_id)
            if package:
                dist = distance_between(current_address, package.address)
                if dist < min_dist:
                    min_dist = dist
                    nearest_package_id = package_id

        if nearest_package_id:
            sorted_route.append(nearest_package_id)
            remaining_packages.remove(nearest_package_id)
            current_address = package_table.search(nearest_package_id).address

    return sorted_route


# Sorts the trucks out and sets depart time
def delivery(truck):
    truck.not_delivered = get_sorted_route(truck)  # Pre-sort packages
    truck.current_time = truck.depart_time

    # Verifies all packages on the truck have the correct departure time
    for package_id in truck.not_delivered:
        package = package_table.search(package_id)
        if package:
            package.truck = truck.truck_id #assigns truck number
            if package.departure_time is None:
                package.departure_time = truck.current_time

    # Deliver all packages in sorted order
    while truck.not_delivered:
        nearest_package_id = truck.not_delivered.pop(0)
        nearest_package = package_table.search(nearest_package_id)

        # Update truck's location and mileage
        dist = distance_between(truck.start_address, nearest_package.address)
        truck.start_address = nearest_package.address
        truck.miles_traveled += dist
        truck.current_time += timedelta(hours=dist / truck.speed)

        # Mark package as delivered
        nearest_package.status = "Delivered"
        nearest_package.delivered_time = truck.current_time
        truck.delivered.append(nearest_package_id)

        # Print status for debugging
        #print(
            #f"DEBUG: Package {nearest_package.package_id} is now {nearest_package.status} at {nearest_package.delivered_time}")


    # determines the last delivered package’s address, calculates the distance back to the hub,
    # and updates the truck’s total mileage and current time
    if truck.delivered:
        last_address = package_table.search(truck.delivered[-1]).address
        dist_back_to_hub = distance_between(last_address, truck.end_address)
        truck.miles_traveled += dist_back_to_hub
        truck.current_time += timedelta(hours=dist_back_to_hub / truck.speed)

        #Prints final status update
        print(f"Truck {truck.truck_id} total miles travelled: {truck.miles_traveled} miles")


# Run deliveries
delivery(truck_one)
delivery(truck_two)
delivery(truck_three)



