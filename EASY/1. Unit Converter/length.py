class Length:
    conversion_to_meters = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'yard': 0.9144,
        'mile': 1609.34,
        'foot': 0.3048,
        'inch': 0.0254
    }

    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        #CHECKER
        if from_unit not in Length.conversion_to_meters or to_unit not in Length.conversion_to_meters:
            raise ValueError("Unsupported Unit. Please use a valid length unit.")

        #CONVERT VALUE TO METERS
        value_in_meters = value * Length.conversion_to_meters[from_unit]
        #CONVERT METERS TO DESIRED CONVERSION
        converted_value = value_in_meters / Length.conversion_to_meters[to_unit]
        return converted_value
