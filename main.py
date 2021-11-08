import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import Constants as co

data = pd.read_csv("/Users/payalsagwal/Desktop/UberRequestData.csv")

# Show Length
len(data[co.requestId].unique())
# print(len(data[co.requestId].unique()))

# Show Row and Column
# print(data.shape)

# print(data.isnull().sum())
# print(data.isnull().sum() / data.shape[0] * 100)
# data.info()
# print(data[co.requestTimestamp].value_counts())
data[co.requestTimestamp] = data[co.requestTimestamp].astype(str)
data[co.requestTimestamp] = data[co.requestTimestamp].replace("/", "-")
data[co.requestTimestamp] = pd.to_datetime(data[co.requestTimestamp], dayfirst=True)
# print(data[co.requestTimestamp])
# data.info()

req_hour = data[co.requestTimestamp].dt.hour
# print(len(req_hour))
# print(req_hour)
data["req_hour"] = req_hour
req_day = data[co.requestTimestamp].dt.day
data["req_day"] = req_day
# data.info()

# plt.subplots(2, 3, figsize=(16, 8))
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(16, 8), facecolor='gold')

ax1.hist(data["req_hour"], data=data, bins=50, stacked=True, lw=5)
ax1.legend(['req_hour','data'])
ax2.scatter(data["req_hour"], data["Driver id"])
ax3.plot(data[co.requestTimestamp], data["req_day"])
plt.show()
plt.plot(x=data[co.requestTimestamp], y=data[co.dropTimestamp])
plt.show()

data["Time_Slot"] = 0
# data.info()
j = 0
for i in data["req_hour"]:
    if data.iloc[j, 6] < 5:
        data.iloc[j, 8] = "Pre_Morning"
    elif 5 <= data.iloc[j, 6] < 10:
        data.iloc[j, 8] = "Morning_Rush"

    elif 10 <= data.iloc[j, 6] < 17:
        data.iloc[j, 8] = "Day_Time"

    elif 17 <= data.iloc[j, 6] < 22:
        data.iloc[j, 8] = "Evening_Rush"
    else:
        data.iloc[j, 8] = "Late_Night"
    j = j + 1
print(data)

data["Time_Slot"].value_counts()
# print (data["Time_Slot"])
plt.figure(figsize=(10, 6))
plt.plot(data["Time_Slot"], data=data)
plt.show()

data_morning_rush = data[data['Time_Slot'] == 'Morning_Rush']
# print(data_morning_rush)

# Severity of problem by location and their count (cancellation of cab as per the pickup location at morning rush hours)
data_airport_cancelled = data_morning_rush.loc[
    (data_morning_rush["Pickup point"] == "Airport") & (data_morning_rush["Status"] == "Cancelled")]
# data_airport_cancelled.shape[0]
data_city_cancelled = data_morning_rush.loc[
    (data_morning_rush["Pickup point"] == "City") & (data_morning_rush["Status"] == "Cancelled")]
data_city_cancelled.shape[0]
# print(data_airport_cancelled)
# print(data_city_cancelled)

# Supply and demand
data_morning_rush.loc[(data_morning_rush["Pickup point"] == "City")].shape[0]
data_morning_rush.loc[
    (data_morning_rush["Pickup point"] == "City") & (data_morning_rush["Status"] == "Trip Completed")].shape[0]
data_morning_rush.loc[(data_morning_rush["Pickup point"] == "Airport")].shape[0]
data_morning_rush.loc[
    (data_morning_rush["Pickup point"] == "Airport") & (data_morning_rush["Status"] == "Trip Completed")].shape[0]
# print (data_morning_rush.loc[(data_morning_rush["Pickup point"]=="City")])

# Supply and Demand for evening rush
data_evening_rush = data[data['Time_Slot'] == 'Evening_Rush']
data_city_cancelled = data_evening_rush.loc[
    (data_evening_rush["Pickup point"] == "City") & (data_evening_rush["Status"] == "Cancelled")]
plt.plot(data_evening_rush["Pickup point"], data=data_evening_rush)
data_city_cancelled.shape[0]
data_evening_rush["Status"].value_counts()
data_evening_rush.loc[(data_evening_rush["Pickup point"] == "City")].shape[0]
data_evening_rush.loc[
    (data_evening_rush["Pickup point"] == "City") & (data_evening_rush["Status"] == "Trip Completed")].shape[0]
data_evening_rush.loc[(data_evening_rush["Pickup point"] == "Airport")].shape[0]
data_evening_rush.loc[
    (data_evening_rush["Pickup point"] == "Airport") & (data_evening_rush["Status"] == "Trip Completed")].shape[0]

# Severity problem at each location by looking at cancellation of cabs in each of the pickup location
data_evening_rush.loc[
    (data_evening_rush["Pickup point"] == "Airport") & (data_evening_rush["Status"] == "Cancelled")].shape[0]
data_evening_rush.loc[
    (data_evening_rush["Pickup point"] == "City") & (data_evening_rush["Status"] == "Cancelled")].shape[0]
