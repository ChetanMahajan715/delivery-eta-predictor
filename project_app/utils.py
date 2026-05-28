import pickle
import json
import numpy as np
import config as config

class DeliveryPrediction():

    def __init__(self, distance_km, hour_of_day, is_weekend, accept_hour, accept_month,
                 No_of_orders, traffic_encoded, num_delivery_partners, population_density,
                 is_rush_hour, weekend_rush_hour, distance_per_minute, orders_per_partner,
                 density_per_partner, weekend_traffic_interaction, distance_traffic_interaction,
                 City, Weather, DayOfWeek, AcceptDayOfWeek, AreaOfInterest, Traffic, TimeOfDay, WeatherTraffic):
        
        # Continuous / numeric
        self.distance_km = distance_km
        self.hour_of_day = hour_of_day
        self.is_weekend = is_weekend
        self.accept_hour = accept_hour
        self.accept_month = accept_month
        self.No_of_orders = No_of_orders
        self.traffic_encoded = traffic_encoded
        self.num_delivery_partners = num_delivery_partners
        self.population_density = population_density
        self.is_rush_hour = is_rush_hour
        self.weekend_rush_hour = weekend_rush_hour
        self.distance_per_minute = distance_per_minute
        self.orders_per_partner = orders_per_partner
        self.density_per_partner = density_per_partner
        self.weekend_traffic_interaction = weekend_traffic_interaction
        self.distance_traffic_interaction = distance_traffic_interaction

        # Categoricals
        self.City = "city_" + City
        self.Weather = "weather_" + Weather
        self.DayOfWeek = "day_of_week_" + DayOfWeek
        self.AcceptDayOfWeek = "accept_day_of_week_" + AcceptDayOfWeek
        self.AreaOfInterest = "area_of_interest_type_" + AreaOfInterest
        self.Traffic = "traffic_" + Traffic
        self.TimeOfDay = "time_of_day_" + TimeOfDay
        self.WeatherTraffic = "weather_traffic_combined_" + WeatherTraffic

    def load_model(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.project_data = json.load(f)

    def get_predicted_delivery_time(self):
        self.load_model()

        # Create test array
        test_array = np.zeros(len(self.project_data['columns']))

        # Numeric features
        test_array[0]  = self.distance_km
        test_array[1]  = self.hour_of_day
        test_array[2]  = self.is_weekend
        test_array[3]  = self.accept_hour
        test_array[4]  = self.accept_month
        test_array[5]  = self.No_of_orders
        test_array[6]  = self.traffic_encoded
        test_array[7]  = self.num_delivery_partners
        test_array[8]  = self.population_density
        test_array[9]  = self.is_rush_hour
        test_array[10] = self.weekend_rush_hour
        test_array[11] = self.distance_per_minute
        test_array[12] = self.orders_per_partner
        test_array[13] = self.density_per_partner
        test_array[14] = self.weekend_traffic_interaction
        test_array[15] = self.distance_traffic_interaction

        # One-hot categorical variables
        for col in [self.City, self.Weather, self.DayOfWeek, self.AcceptDayOfWeek,
                    self.AreaOfInterest, self.Traffic, self.TimeOfDay, self.WeatherTraffic]:
            if col in self.project_data['columns']:
                idx = self.project_data['columns'].index(col)
                test_array[idx] = 1

        print("Test Array:", test_array)

        # Prediction
        prediction = self.model.predict([test_array])[0]
        print(f"Predicted Delivery Time: {round(prediction, 2)} minutes")
        return prediction


if __name__ == "__main__":
    # Example test run
    dp = DeliveryPrediction(
        distance_km=5.2, hour_of_day=14, is_weekend=0, accept_hour=14, accept_month=9,
        No_of_orders=120, traffic_encoded=2, num_delivery_partners=50, population_density=3000,
        is_rush_hour=1, weekend_rush_hour=0, distance_per_minute=0.18, orders_per_partner=2.4,
        density_per_partner=60, weekend_traffic_interaction=0.5, distance_traffic_interaction=0.9,
        City="NewYork", Weather="Sunny", DayOfWeek="Monday", AcceptDayOfWeek="Monday",
        AreaOfInterest="Suburb", Traffic="High", TimeOfDay="Evening", WeatherTraffic="Rain_High"
    )
    dp.get_predicted_delivery_time()
