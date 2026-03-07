import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

df = pd.read_csv("datasets/monthly_revenue_dataset.csv")

df["Month"] = pd.to_datetime(df["Month"])

df = df.sort_values("Month")

df.set_index("Month", inplace=True)

revenue = df["Total_Actual_Revenue"]

train_size = int(len(revenue) * 0.8)

train = revenue[:train_size]
test = revenue[train_size:]

model = ARIMA(train, order=(1,1,1))
model_fit = model.fit()

forecast_test = model_fit.forecast(steps=len(test))

mae = mean_absolute_error(test, forecast_test)
rmse = np.sqrt(mean_squared_error(test, forecast_test))
mape = np.mean(np.abs((test - forecast_test) / test)) * 100

print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)

future_forecast = model_fit.forecast(steps=6)

forecast_df = pd.DataFrame({
    "Forecasted_Revenue": future_forecast
})

forecast_df.to_csv("datasets/revenue_forecast.csv")

print("Revenue forecasting completed")