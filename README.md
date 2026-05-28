# Grocery Delivery Service — Delivery Time Prediction

A machine-learning web app that predicts the **estimated delivery time (in minutes)** for grocery orders based on distance, traffic, weather, order volume, delivery-partner capacity, and time/location features.

The model is a **Random Forest Regressor** trained on a 50,000-row delivery dataset, served through a **Flask** web interface where users fill in order details and get an instant prediction.

---

## Features

- Flask web UI with a single prediction form
- REST-style endpoint (`/predict_delivery_time`) supporting both `GET` and `POST`
- Pre-trained model bundled in the repo — works immediately after install
- Clean separation of model logic (`project_app/utils.py`), config (`config.py`), and serving (`interface.py`)
- Reproducible training pipeline in `project_app/Time estimation.ipynb`

---

## Project Structure

```
.
├── interface.py                 # Flask app (routes + request handling)
├── config.py                    # Model/data paths and server port
├── requirements.txt             # Python dependencies
├── document.pdf                 # Project report / documentation
├── project_app/
│   ├── __init__.py
│   ├── utils.py                 # DeliveryPrediction class (loads model, builds feature vector, predicts)
│   ├── Linear_Model.pkl         # Trained Random Forest model (pickle)
│   ├── project_data.json        # Column order + category metadata used to build the feature vector
│   ├── delivery_dataset_enhanced.csv  # Training dataset (50k rows)
│   └── Time estimation.ipynb    # EDA, cleaning, training, evaluation notebook
├── templates/
│   └── index.html               # Prediction form UI
└── static/
    └── sample.jpg               # Background image
```

> **Note:** `Linear_Model.pkl` is a historical filename — the model it contains is a `RandomForestRegressor`, not a linear model.

---

## Getting Started

### 1. Prerequisites

- Python 3.9+

### 2. Clone the repository

```bash
git clone https://github.com/<your-username>/grocery-delivery-service.git
cd grocery-delivery-service
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the app

```bash
python interface.py
```

Then open **http://localhost:5000** in your browser, fill in the form, and click **Predict Delivery Time**.

---

## API Usage

The model can also be queried directly via the `/predict_delivery_time` endpoint.

**GET example:**

```
GET http://localhost:5000/predict_delivery_time?distance_km=5.4&hour_of_day=14&is_weekend=0&accept_hour=15&accept_month=9&No_of_orders=120&traffic_encoded=1&num_delivery_partners=8&population_density=4500&is_rush_hour=1&weekend_rush_hour=0&distance_per_minute=0.12&orders_per_partner=15&density_per_partner=560&weekend_traffic_interaction=0&distance_traffic_interaction=1&City=New%20York&Weather=Sunny&DayOfWeek=Monday&AcceptDayOfWeek=Monday&AreaOfInterest=Suburb&Traffic=Low&TimeOfDay=morning&WeatherTraffic=Sunny_Low
```

**Response:**

```json
{ "Result": "Predicted Delivery Time: 12.34 minutes" }
```

### Input fields

**Numeric:** `distance_km`, `hour_of_day`, `is_weekend`, `accept_hour`, `accept_month`, `No_of_orders`, `traffic_encoded`, `num_delivery_partners`, `population_density`, `is_rush_hour`, `weekend_rush_hour`, `distance_per_minute`, `orders_per_partner`, `density_per_partner`, `weekend_traffic_interaction`, `distance_traffic_interaction`

**Categorical (must match the model's known categories):**

| Field            | Allowed values                                                                 |
|------------------|--------------------------------------------------------------------------------|
| `City`           | New York, Houston, Los Angeles, San Francisco, Unknown                          |
| `Weather`        | Sunny, Rain                                                                     |
| `DayOfWeek`      | Monday, Tuesday, Wednesday, Thursday, Saturday, Sunday                          |
| `AcceptDayOfWeek`| Monday, Tuesday, Wednesday, Thursday, Saturday, Sunday                          |
| `AreaOfInterest` | Industrial, Suburb                                                             |
| `Traffic`        | Low, Medium                                                                     |
| `TimeOfDay`      | morning, evening, night                                                         |
| `WeatherTraffic` | Sunny_Low, Sunny_Medium, Sunny_High, Rain_Low, Rain_Medium, Rain_High, Overcast_Low, Overcast_Medium |

---

## How It Works

1. The form (or API request) submits order details.
2. `interface.py` parses the inputs and instantiates `DeliveryPrediction` (`project_app/utils.py`).
3. `DeliveryPrediction` loads the trained model and `project_data.json`, builds a one-hot-encoded feature vector aligned to the model's expected column order, and returns a prediction.
4. The predicted delivery time is returned as JSON and shown in the UI.

---

## Model Training

The full pipeline lives in [`project_app/Time estimation.ipynb`](project_app/Time%20estimation.ipynb):

- Data cleaning (median/mode imputation, outlier capping at the 1st/99th percentiles)
- Exploratory data analysis
- One-hot encoding of categorical features
- `RandomForestRegressor` training with `RandomizedSearchCV` hyperparameter tuning
- Evaluation (MAE, R², 5-fold cross-validation)
- Model + metadata export to `Linear_Model.pkl` and `project_data.json`

To retrain, run the notebook from inside the `project_app/` directory so the relative paths resolve.

---

## License

This project is licensed under the [MIT License](LICENSE).
