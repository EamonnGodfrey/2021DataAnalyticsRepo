#pandas DataFrame loaded from excel data with data filtering
import pandas as pd

#open file and read data
roomTemps = pd.read_excel(r'C:\Users\eamon\OneDrive\_GORDON\ICT60115 & ICT50118\Data Analytics\1 Pandas - Python Data Analysis Library\_project\RoomTemperature.xlsx')

#specify the column that match the excel file
df = pd.DataFrame(roomTemps, columns = ['Room', 'Temperature', 'Humidity', 'Time'])

print(df)

#filter out unneeded columns, make a new DateFrame with just Room and Temperature values
dfRoomTemp = df[["Room", "Temperature"]]

print(dfRoomTemp)