import pandas as pd

roomTemps = {"Room" : ["E223", "E222", "E208", "E219"],
            "Temperature": [22.1, 21.4, 23.5, 22.6]
}

df = pd.DataFrame(roomTemps, columns = ["Room", "Temperature"])

print(df)