from flask import Flask, jsonify, request, render_template
import config as config
from project_app.utils import DeliveryPrediction

app = Flask(__name__)

####################################################################################################################
############################################### Homepage API ########################################################
####################################################################################################################

@app.route('/')
def home_page():
    print('Welcome to the Delivery Prediction Model')
    return render_template('index.html')


####################################################################################################################
############################################### Model API ##########################################################
####################################################################################################################

@app.route('/predict_delivery_time', methods=['GET', 'POST'])
def predict_delivery():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form

        # Extracting features from POST form data
        distance_km = float(data['distance_km'])
        hour_of_day = int(data['hour_of_day'])
        is_weekend = int(data['is_weekend'])
        accept_hour = int(data['accept_hour'])
        accept_month = int(data['accept_month'])
        No_of_orders = int(data['No_of_orders'])
        traffic_encoded = int(data['traffic_encoded'])
        num_delivery_partners = int(data['num_delivery_partners'])
        population_density = float(data['population_density'])
        is_rush_hour = int(data['is_rush_hour'])
        weekend_rush_hour = int(data['weekend_rush_hour'])
        distance_per_minute = float(data['distance_per_minute'])
        orders_per_partner = float(data['orders_per_partner'])
        density_per_partner = float(data['density_per_partner'])
        weekend_traffic_interaction = float(data['weekend_traffic_interaction'])
        distance_traffic_interaction = float(data['distance_traffic_interaction'])

        # Categorical
        City = data['City']
        Weather = data['Weather']
        DayOfWeek = data['DayOfWeek']
        AcceptDayOfWeek = data['AcceptDayOfWeek']
        AreaOfInterest = data['AreaOfInterest']
        Traffic = data['Traffic']
        TimeOfDay = data['TimeOfDay']
        WeatherTraffic = data['WeatherTraffic']

        dp = DeliveryPrediction(distance_km, hour_of_day, is_weekend, accept_hour, accept_month,
                                No_of_orders, traffic_encoded, num_delivery_partners, population_density,
                                is_rush_hour, weekend_rush_hour, distance_per_minute, orders_per_partner,
                                density_per_partner, weekend_traffic_interaction, distance_traffic_interaction,
                                City, Weather, DayOfWeek, AcceptDayOfWeek, AreaOfInterest, Traffic, TimeOfDay, WeatherTraffic)

        prediction = dp.get_predicted_delivery_time()
        return jsonify({'Result': f'Predicted Delivery Time: {round(prediction,2)} minutes'})

    else:
        print('We are in GET Method')
        data = request.args

        # Extracting features from GET params
        distance_km = float(data['distance_km'])
        hour_of_day = int(data['hour_of_day'])
        is_weekend = int(data['is_weekend'])
        accept_hour = int(data['accept_hour'])
        accept_month = int(data['accept_month'])
        No_of_orders = int(data['No_of_orders'])
        traffic_encoded = int(data['traffic_encoded'])
        num_delivery_partners = int(data['num_delivery_partners'])
        population_density = float(data['population_density'])
        is_rush_hour = int(data['is_rush_hour'])
        weekend_rush_hour = int(data['weekend_rush_hour'])
        distance_per_minute = float(data['distance_per_minute'])
        orders_per_partner = float(data['orders_per_partner'])
        density_per_partner = float(data['density_per_partner'])
        weekend_traffic_interaction = float(data['weekend_traffic_interaction'])
        distance_traffic_interaction = float(data['distance_traffic_interaction'])

        # Categorical
        City = data['City']
        Weather = data['Weather']
        DayOfWeek = data['DayOfWeek']
        AcceptDayOfWeek = data['AcceptDayOfWeek']
        AreaOfInterest = data['AreaOfInterest']
        Traffic = data['Traffic']
        TimeOfDay = data['TimeOfDay']
        WeatherTraffic = data['WeatherTraffic']

        dp = DeliveryPrediction(distance_km, hour_of_day, is_weekend, accept_hour, accept_month,
                                No_of_orders, traffic_encoded, num_delivery_partners, population_density,
                                is_rush_hour, weekend_rush_hour, distance_per_minute, orders_per_partner,
                                density_per_partner, weekend_traffic_interaction, distance_traffic_interaction,
                                City, Weather, DayOfWeek, AcceptDayOfWeek, AreaOfInterest, Traffic, TimeOfDay, WeatherTraffic)

        prediction = dp.get_predicted_delivery_time()
        return jsonify({'Result': f'Predicted Delivery Time: {round(prediction,2)} minutes'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER, debug=True)
