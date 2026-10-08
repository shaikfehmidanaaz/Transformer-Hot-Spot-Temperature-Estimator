class TransformerHotSpotTemperatureEstimator:
    def __init__(self, ambient_temperature, oil_temperature,
                 load_percentage, winding_temperature_rise):
        self.ambient_temperature = ambient_temperature
        self.oil_temperature = oil_temperature
        self.load_percentage = load_percentage
        self.winding_temperature_rise = winding_temperature_rise

    def calculate_top_oil_temperature(self):
        return self.ambient_temperature + self.oil_temperature

    def calculate_hot_spot_temperature(self):
        top_oil = self.calculate_top_oil_temperature()

        # Load factor
        load_factor = self.load_percentage / 100

        # Winding temperature rise increases approximately with load
        winding_rise = self.winding_temperature_rise * (load_factor ** 2)

        hot_spot = top_oil + winding_rise

        return hot_spot

    def get_condition(self, hot_spot):
        if hot_spot < 80:
            return "NORMAL"
        elif hot_spot < 100:
            return "WARNING"
        else:
            return "CRITICAL"

    def display_result(self):
        top_oil = self.calculate_top_oil_temperature()
        hot_spot = self.calculate_hot_spot_temperature()
        condition = self.get_condition(hot_spot)

        print("----- Transformer Hot-Spot Temperature Estimator -----")
        print(f"Ambient Temperature      : {self.ambient_temperature:.2f} °C")
        print(f"Oil Temperature Rise     : {self.oil_temperature:.2f} °C")
        print(f"Top Oil Temperature      : {top_oil:.2f} °C")
        print(f"Load Percentage          : {self.load_percentage:.2f} %")
        print(f"Winding Temperature Rise : {self.winding_temperature_rise:.2f} °C")
        print(f"Estimated Hot-Spot Temp  : {hot_spot:.2f} °C")
        print(f"Transformer Condition    : {condition}")


# Example values
ambient_temperature = 30
oil_temperature = 40
load_percentage = 80
winding_temperature_rise = 50

estimator = TransformerHotSpotTemperatureEstimator(
    ambient_temperature,
    oil_temperature,
    load_percentage,
    winding_temperature_rise
)

estimator.display_result()
