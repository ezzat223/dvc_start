import pandas as pd 

Data = [
    {"name": "ezzat", "age": 23, "city": "cairo"},
    {"name": "hegazy", "age": 47, "city": "october"},
    {"name": "fahmy", "age": 13, "city": "alex"},
    {"name": "orabi", "age": 80, "city": "paris"}
]

# converto to a dataframe then save in a csv
Data = pd.DataFrame(Data)
Data.to_csv("data/data.csv", index=False)