# Matplotlib3.py
# Use of pandas  and matplotlib to read an excel file and 
# plot a graph of specified information within the 
# excel file.
#  
# Author:       Eamonn Godfrey
# ID:           13214184
# Date:         05/08/21

import pandas as pd
import matplotlib.pyplot as plt


roomTemps = pd.read_excel(r'C:\Users\eamon\OneDrive\_GORDON\ICT60115 & ICT50118\Data Analytics\1 Pandas - Python Data Analysis Library\_project\RoomTemperature.xlsx')

df = pd.DataFrame(roomTemps, columns=['Room', 'Temperature', 'Humidity', 'CO2', 'Outside Temp', 'Time'])

dfE222 = df[df["Room"] == "E222"]
dfE222TimeHumidity = dfE222[["Time", "Humidity"]]
print(dfE222TimeHumidity)

dfE222TimeHumidity.plot(x='Time', y='Humidity')
plt.xlabel('Time')
plt.ylabel('Humidity')
plt.title('Humidity Over Time')
plt.show()