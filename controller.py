from model import Color, FuelType, Manufacturer, Transmission, Vehicle
import csv
from typing import List

# Class responsible for managing vehicle files (importing and exporting)
class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    # Method to import vehicle data from a CSV file
    def import_vehicles_from_file(self, file_path: str) -> List[List[str]]:
        vehicles_data_array = []
        # Open the CSV file for reading
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            # Read each row in the CSV and add it to the list
            for row in csv_reader:
                vehicles_data_array.append(row)
        return vehicles_data_array

    # Method to rewrite the vehicle data back to the file
    def rewrite_file(self, vehicle_list: List[Vehicle]):
        # Open the CSV file for writing, overwriting existing content
        with open(self.file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            # Write each vehicle's information as a row in the CSV
            for vehicle in vehicle_list:
                vehicle_info = self.prepare_the_vehicle_for_rewriting(vehicle)
                csv_writer.writerow(vehicle_info)

    # Method to prepare a vehicle's data for writing to the CSV
    def prepare_the_vehicle_for_rewriting(self, vehicle: Vehicle) -> List[str]:
        return [
            str(vehicle.get_ID()),                   # Vehicle ID
            vehicle.get_Manufacturer(),         # Manufacturer name
            vehicle.get_Model(),                     # Model name
            str(vehicle.get_HorsePower()),           # Horsepower
            str(vehicle.get_Price()),                # Price
            vehicle.get_Color(),                # Color name
            str(vehicle.get_Mileage()),              # Mileage
            str(vehicle.get_ProductionYear()),       # Production year
            vehicle.get_FuelType(),             # Fuel type
            vehicle.get_Transmission()         # Transmission type
        ]

# Class responsible for printing vehicle information and messages
class VehicleShopPrinter:
    # Method to print the list of available vehicles
    def print_available_vehicles(self, vehicle_list):
        # Check if the vehicle list is empty or None
        if not vehicle_list:
            print("No vehicles available.")
            return
        
        # Print header
        header = f"{'ID':<2} | {'Manufacturer':<14} | {'Model':<10} | {'HorsePower':<10} | {'Mileage':<9} | {'Color':<8}  |  {'Price':<6}  | {'ProductionYear':<5} | {'FuelType':<14} | {'Transmission':<15}  "
        print(header)
        print("=" * len(header))
        
        # Print each vehicle's details
        for vehicle in vehicle_list:
            if isinstance(vehicle, Vehicle):
                vehicle_details = f"{vehicle.get_ID():<2} | {vehicle.get_Manufacturer():<14} | {vehicle.get_Model():<10} | {vehicle.get_HorsePower():<11} | {vehicle.get_Mileage():<8}  | {vehicle.get_Color():<9}  | {vehicle.get_Price():<6} | {vehicle.get_ProductionYear():<13}   | {vehicle.get_FuelType():<15} | {vehicle.get_Transmission():<18} "
            print(vehicle_details)  
       
    
    def print_vehicle_sold_message(self, vehicle_chosen_id):
        print("\nVehicle with ID", vehicle_chosen_id, "was sold.")
    
    def print_vehicle_id_to_sell_message(self):
        print("\n\n Please enter the number (ID) of the vehicle you want to sell: ")

# Class responsible for processing vehicle transactions
class VehicleShopProcessor:
    # Method to "sell" a vehicle, i.e., remove it from the list by ID
    def sell_vehicle(self, vehicle_list: List[Vehicle], selected_vehicle_id: int) -> List[Vehicle]:
        # Filter out the vehicle with the matching ID from the list
        return [vehicle for vehicle in vehicle_list if vehicle.get_ID() != selected_vehicle_id]

# Class responsible for transforming data from strings to Vehicle objects
class VehicleTransformer:
    # Method to transform a list of vehicle data strings into a list of Vehicle objects
    def transform_data_as_string_array_to_vehicle_objects(self, vehicles_as_string_array: List[str]) -> List[Vehicle]:
        vehicle_list = []
        for vehicle_string in vehicles_as_string_array:
            if isinstance(vehicle_string, list):
                # Transform each string list into a Vehicle object
                vehicle = self.transform_to_vehicle_object(vehicle_string)
                vehicle_list.append(vehicle)
            else:
                raise TypeError("Expected a list for vehicle data, got: " + str(type(vehicle_string)))
        return vehicle_list

    # Method to transform a single string array into a Vehicle object
    def transform_to_vehicle_object(self, vehicle_as_string_array: List[str]) -> Vehicle:
        if len(vehicle_as_string_array) != 10:
            raise ValueError("Invalid data format for vehicle")
        
        # Extract and convert the vehicle attributes from the string array
        vehicle_id = int(vehicle_as_string_array[0])
        manufacturer = (vehicle_as_string_array[1])
        model = vehicle_as_string_array[2]
        horse_power = int(vehicle_as_string_array[3])
        price = float(vehicle_as_string_array[4])
        color = (vehicle_as_string_array[5])
        mileage = int(vehicle_as_string_array[6])
        production_year = int(vehicle_as_string_array[7])
        fuel_type = (vehicle_as_string_array[8])
        transmission = (vehicle_as_string_array[9])

        # Create and return the Vehicle object
        return Vehicle(
            ID=vehicle_id,
            Manufacturer=manufacturer,
            Model=model,
            HorsePower=horse_power,
            Price=price,
            Color=color,
            Mileage=mileage,
            ProductionYear=production_year,
            FuelType=fuel_type,
            Transmission=transmission
        )

    # Helper method to convert a manufacturer string to a Manufacturer enum
    def get_manufacturer_from_string(self, manufacturer_as_string: str) -> Manufacturer:
        for manufacturer in Manufacturer:
            if manufacturer.name == manufacturer_as_string:
                return manufacturer
        raise ValueError("Manufacturer not supported: " + manufacturer_as_string)

    # Helper method to convert a color string to a Color enum
    def get_color_from_string(self, color_as_string: str) -> Color:
        for color in Color:
            if color.name == color_as_string:
                return color
        raise ValueError("Color not supported: " + color_as_string)

    # Helper method to convert a fuel type string to a FuelType enum
    def get_fuel_type_from_string(self, fuel_type_as_string: str) -> FuelType:
        for fuel_type in FuelType:
            if fuel_type.name == fuel_type_as_string:
                return fuel_type
        raise ValueError("FuelType not supported: " + fuel_type_as_string)

    # Helper method to convert a transmission string to a Transmission enum
    def get_transmission_from_string(self, transmission_as_string: str) -> Transmission:
        for transmission in Transmission:
            if transmission.name == transmission_as_string:
                return transmission
        raise ValueError("Transmission not supported: " + transmission_as_string)
