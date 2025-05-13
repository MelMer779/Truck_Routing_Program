import csv
import os
from datetime import datetime
from packages import Package


def load_addresses(file_path):
    file_path = os.path.join('data', file_path)
    addresses = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Adding address only
            addresses.append(row[2].strip())

    return addresses


def load_distances(file_path):
    file_path = os.path.join('data', file_path)
    distances = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            distances.append([float(val) if val else None for val in row])  # Convert each value to float
    return distances


def load_package_info(file_path):
    file_path = os.path.join('data', file_path)
    packages = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline_str = row[5]
            if deadline_str == 'EOD':
                deadline = 'End of Day'
            else: deadline = datetime.strptime(deadline_str, "%I:%M %p").strftime("%I:%M %p")


            weight = int(row[6])
            notes = row[7] if len(row) > 7 else None  # Handle missing notes

            # Creates a Package instance and adds it to the list
            package = Package(package_id, address, city, state, zip_code, deadline, weight, notes)
            packages.append(package)
    return packages



addresses = load_addresses('addresses.csv')
distances = load_distances('distances.csv')
packages = load_package_info('package_info.csv')
