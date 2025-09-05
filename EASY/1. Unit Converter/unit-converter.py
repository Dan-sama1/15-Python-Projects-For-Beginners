# #Unit Converter

# Create a program that converts kilometers ↔ miles, Celsius ↔ Fahrenheit, etc.

# User chooses which conversion and inputs a number.

from length import Length
from temperature import Temperature
from data import Data


class Main:
    def run(self):
        while True:
            print("=" * 20)
            print("{:^20}".format("Unit Converter"))
            print("=" * 20)
            print("\n{:^20}".format("Conversion Type"))
            print(f"  1. LENGTH\n"
                  f"  2. TEMPERATURE\n"
                  f"  3. DATA\n"
                  f"  4. EXIT\n")
            print("=" * 20)

            conversion_type = input(": ")

            if conversion_type == "1":
                self.length_converter()
            elif conversion_type == "2":
                self.temperature_converter()
            elif conversion_type == "3":
                self.data_converter()
            elif conversion_type == "4":
                input("Press Enter to Exit")
                print("Bye!")
                break
            else:
                print("Invalid Choice. Please Try Again.")

    def length_converter(self):
        units = ['meter', 'kilometer', 'centimeter', 'millimeter',
            'yard', 'mile', 'foot', 'inch']

        print("Available Units")
        for i, unit in enumerate(units, start=1):
            print(f"{i}. {unit}")

        try:
            from_index = int(input("Convert From (choose number): ")) -1
            to_index = int(input("Convert To (choose number): ")) -1
            value = float(input("Value to Convert\n: "))

        except (ValueError, IndexError):
            print("Invalid Input. Please try again.")
            return

        #GET UNIT FROM UNIT INDEX
        from_unit = units[from_index]
        to_unit = units[to_index]

        result = Length.convert(value, from_unit, to_unit)
        print(f"\n{value} {from_unit} is {result:.4f} {to_unit}")

    def temperature_converter(self):
        units = ['celsius', 'fahrenheit']

        print(f"\nAvailable Units\n"
              f"1. Celsius\n"
              f"2. Fahrenheit")

        try:
            from_index = int(input("Convert From (choose number): ")) -1
            to_index = int(input("Convert To (choose number): ")) -1
            value = float(input("Value to Convert\n: "))

        except (ValueError, IndexError):
            print("Invalid Input. Please try again")
            return

        from_unit = units[from_index]
        to_unit = units[to_index]

        if from_unit == to_unit:
            result = value
        elif from_unit == 'celsius' and to_unit == 'fahrenheit':
            result = Temperature.celsius_to_fahrenheit(value)

        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            result = Temperature.fahrenheit_to_celsius(value)

        else:
            print("Invalid Input. Please Try Again.")
            return

        print(f"\n{value}° {from_unit.capitalize()} is {result:.2f}° to {to_unit.capitalize()}")


    def data_converter(self):
        units = ['megabyte', 'byte', 'kilobyte', 'gigabyte']

        for i, unit in enumerate(units, start=1):
            print(f"{i}. {unit}")

        try:
            from_index = int(input("Convert From (choose a number): ")) -1
            to_index = int(input("Convert To (choose a number): ")) -1
            value = float(input("Value to Convert\n: "))

        except (ValueError, IndexError):
            print("Invalid Input. Please try again.")
            return

        from_unit = units[from_index]
        to_unit = units[to_index]

        result = Data.convert(value, from_unit, to_unit)
        print(f"\n{value} from {from_unit.capitalize()} is {result:.4f} to {to_unit.capitalize()}")


if __name__ == "__main__":
    app = Main()
    app.run()
