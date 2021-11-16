import pandas as pd
from pandas.plotting import register_matplotlib_converters
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import Constants as co

register_matplotlib_converters()

data = pd.read_csv("/Users/payalsagwal/Documents/PycharmCaseStudy/UberAnalysis/UberRequestData.csv")

# Show Length
# print(len(data[co.requestId].unique()))

# Show Row and Column
# print(data.shape)

# find the null values in column and the percentage of null values
# print(data.isnull().sum())
# print(data.isnull().sum()/ data.shape[0] *100)

# print(data[co.requestTimestamp].value_counts())
data[co.requestTimestamp] = data[co.requestTimestamp].astype(str).replace("/", "-")
data[co.requestTimestamp] = pd.to_datetime(data[co.requestTimestamp], dayfirst=True)
# print(data[co.requestTimestamp])

req_hour = data[co.requestTimestamp].dt.hour
# print(len(req_hour))
# print(req_hour)
data[co.reqHour] = req_hour
req_day = data[co.requestTimestamp].dt.day
# print(req_day)
data[co.reqDay] = req_day
# data.info()

# plt.subplots(2, 3, figsize=(16, 8))
# fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(16, 8), facecolor='gold')
# ax1.hist(data[co.reqHour], data=data[co.driverId], color='red', bins=50, stacked=True, lw=5)
# ax1.legend([co.reqHour, co.driverId])
# ax2.hist(data[co.reqHour])
# ax3.plot(data[co.reqHour], data[co.driverId])
# plt.show()

# plt.subplot(1, 2, 1)
# plt.scatter(data[co.reqHour], data[co.driverId])

# plt.subplot(1, 2, 2)
# plt.hist(data[co.reqHour], bins=50)
# plt.show()

data[co.timeSlot] = 0

def setTimeSlot():
    j = 0
    for i in data[co.reqHour]:
        if data.iloc[j, 6] < 5:
            data.iloc[j, 8] = co.preMorning
        elif 5 <= data.iloc[j, 6] < 10:
            data.iloc[j, 8] = co.morningRush

        elif 10 <= data.iloc[j, 6] < 17:
            data.iloc[j, 8] = co.dayTime

        elif 17 <= data.iloc[j, 6] < 22:
            data.iloc[j, 8] = co.eveningRush
        else:
            data.iloc[j, 8] = co.lateNight
        j = j + 1
    # pass


setTimeSlot()

# data[co.timeSlot].value_counts()

data_morning_rush = data[data[co.timeSlot] == co.morningRush]
print(data_morning_rush)

# Severity of problem by location and their count (cancellation of cab as per the pickup location at morning rush hours)
data_airport_morning_cancelled = data_morning_rush.loc[(data_morning_rush[co.pickupPoint] == co.airport) & (data_morning_rush[co.status] == co.cancelled)]
print(data_airport_morning_cancelled)

data_city_morning_cancelled = data_morning_rush.loc[(data_morning_rush[co.pickupPoint] == co.city) & (data_morning_rush[co.status] == co.cancelled)]
print(data_city_morning_cancelled)

# Supply and demand for morning rush
# Trip completed from city to airport in morning
data_city_morning_completed = data_morning_rush.loc[(data_morning_rush[co.pickupPoint] == co.city) & (data_morning_rush[co.status] == co.tripCompleted)]
print(data_city_morning_completed)

# Trip completed from airport to city in morning
data_airport_morning_completed = data_morning_rush.loc[(data_morning_rush[co.pickupPoint] == co.airport) & (data_morning_rush[co.status] == co.tripCompleted)]
print(data_airport_morning_completed)

# Supply and Demand for evening rush

data_evening_rush = data[data[co.timeSlot] == co.eveningRush]
print(data_evening_rush)

# Trip cancelled from city to airport
data_city_evening_cancelled = data_evening_rush.loc[(data_evening_rush[co.pickupPoint] == co.city) & (data_evening_rush[co.status] == co.cancelled)]
print (data_city_evening_cancelled)

# Trip completed from city to airport
data_city_evening_completed = data_evening_rush.loc[(data_evening_rush[co.pickupPoint] == co.city) & (data_evening_rush[co.status] == co.tripCompleted)]
print(data_city_evening_completed)

# Trip completed from airport to city
data_airport_evening_completed = data_evening_rush.loc[(data_evening_rush[co.pickupPoint] == co.airport) & (data_evening_rush[co.status] == co.tripCompleted)]
print(data_airport_evening_completed)

# Severity problem at each location by looking at cancellation of cabs in each of the pickup location
# Trip cancelled from airport to city
data_airport_evening_cancelled = data_evening_rush.loc[(data_evening_rush[co.pickupPoint] == co.airport) & (data_evening_rush[co.status] == co.cancelled)]
print(data_airport_evening_cancelled)
