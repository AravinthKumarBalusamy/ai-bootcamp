
import os
import json
from datetime import datetime

class TemperatureConverter:

    def __init__(self):
        self.history_file = 'data/conversion_history.json'
        self.history = self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as file:
                return json.load(file)
        return []
    
    def save_history(self):
        os.makedirs('data', exist_ok=True)
        with open(self.history_file, 'w') as file:
            json.dump(self.history, file)

    def record_conversion(self, conversion_type, input_temp, output_temp):
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "type": conversion_type,
            "input": input_temp,
            "output": output_temp
        })
        self.save_history()

    def celcius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        self.record_conversion("C to F", celsius, fahrenheit)
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        self.record_conversion("F to C", fahrenheit, celsius)
        return celsius

    def show_statistics(self):
        print("Conversion History:")
        if not self.history:
            print("No conversions yet.")
        c_to_f = [record for record in self.history if record['type'] == "C to F"]
        f_to_c = [record for record in self.history if record['type'] == "F to C"]
        print(f"C to F conversions: {len(c_to_f)}")
        print(f"F to C conversions: {len(f_to_c)}")
        if c_to_f:
            print("C to F Conversion Details:")
            for record in c_to_f:
                print(f"  {record['timestamp']}: {record['input']} -> {record['output']}")
        if f_to_c:
            print("F to C Conversion Details:")
            for record in f_to_c:
                print(f"  {record['timestamp']}: {record['input']} -> {record['output']}")

    def run(self):
        print("Temperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        
        while True:
            choice = input("Choose an option (1/2): ")

            if choice == '1':
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = self.celcius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit}°F")
            elif choice == '2':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = self.fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius}°C")
            elif choice == '3':
                self.show_statistics()
            elif choice == '4':
                print(f"Saved {len(self.history)} conversions to {self.history_file}")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    converter = TemperatureConverter()
    converter.run()