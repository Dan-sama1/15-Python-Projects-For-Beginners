class Data:
    conversion_to_mb = {
        'megabyte': 1.0,
        'byte': 1/1000000,
        'kilobyte': 1/1000,
        'gigabyte': 1000.0
    }

    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in Data.conversion_to_mb or to_unit not in Data.conversion_to_mb:
            print("Unsupported Unit. Please try again.")
            return

        value_in_mb = value * Data.conversion_to_mb[from_unit]
        converted_value = value_in_mb / Data.conversion_to_mb[to_unit]
        return converted_value
