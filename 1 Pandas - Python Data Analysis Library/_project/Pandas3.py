# Pandas3.py
# Use of pandas to read an excel file and return the specified
# results from that file.
#  
# Author:       Eamonn Godfrey
# ID:           13214184
# Date:         05/08/21

import pandas as pd

roomTemps = pd.read_excel(r'C:\Users\eamon\OneDrive\_GORDON\ICT60115 & ICT50118\Data Analytics\1 Pandas - Python Data Analysis Library\_project\RoomTemperature.xlsx')


df = pd.DataFrame(roomTemps, columns=['Room', 'Temperature', 'Humidity', 'CO2', 'Outside Temp', 'Time'])

dfE222 = df[df["Room"] == "E222"]

dfE222TimeHumidity = dfE222[["Time", "Humidity"]]
print(dfE222TimeHumidity)