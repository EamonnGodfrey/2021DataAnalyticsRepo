import pandas as pd

#read RoomTemperature.xlsx file 
roomTemps = pd.read_excel(r'C:\Users\eamon\OneDrive\_GORDON\ICT60115 & ICT50118\Data Analytics\1 Pandas - Python Data Analysis Library\_project\RoomTemperature.xlsx')

#setup roomTemps as DataFrame object and then display
df = pd.DataFrame(roomTemps, columns=['Room', 'Temperature', 'Humidity', 'Time'])
print(df)

#initialise new columns co2 and outside temps, then add them to DataFrame df
carbondioxide = [554, 899, 1111, 988, 735, 549]
outsideTemp = [26.5, 25.3, 25.99, 24.11, 22.79, 26.20]
df['CO2'] = carbondioxide
df['Outside Temp'] = outsideTemp
#print to show the new added columns
print(df)

#write the modified DataFrame to the RoomTemperature.xlsx file
df.to_excel('RoomTemperature.xlsx', sheet_name='Sheet1')