import pandas as pd
import matplotlib.pyplot as plt

roomTemps = pd.read_excel(r'C:\Users\eamon\OneDrive\_GORDON\ICT60115 & ICT50118\Data Analytics\1 Pandas - Python Data Analysis Library\_project\RoomTemperature.xlsx')

df = pd.DataFrame(roomTemps, columns=['Room', 'Temperature', 'Humidity', 'CO2', 'Outside Temp', 'Time'])

dfE208 = df[df["Room"] == "E208"]

dfE208TimeCo2 = dfE208[["Time", "CO2"]]
dfE208TimeCO2sorted = dfE208TimeCo2.sort_values("Time")
print(dfE208TimeCo2)
print(dfE208TimeCO2sorted)
