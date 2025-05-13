# Truck Routing Program

This is a Python-based delivery routing system that uses the Nearest Neighbor algorithm to simulate efficient package deliveries. It tracks truck mileage, delivery timestamps, and package status in real-time via a command-line interface.

## Features

- Route optimization using the Nearest Neighbor algorithm
- Tracks package status: At Hub, En Route, Delivered
- Calculates total and per-truck mileage
- Simulates two drivers and enforces realistic delivery constraints
- User interface to search delivery status by time and package ID

## Technologies Used

- Python 3.13
- Custom Hash Table for package storage
- CSV parsing for location, distance, and package data
- CLI-based tracking and reporting

## How to Run

1. Clone this repository:
   ```bash
   git clone git@github.com:MelMer779/Truck_Routing_Program.git
   cd Truck_Routing_Program
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Run the program:
   ```bash
   python main.py
   ```

## Author

**Melissa Mercado**  
[GitHub Profile](https://github.com/MelMer779)
