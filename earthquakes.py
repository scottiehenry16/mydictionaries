import json

infile = open('eq_data.json', 'r')
earthquakes = json.load(infile)


#Part 1
EarthquakeDic = earthquakes["features"]
print()
print("Total Earthquakes:",len(EarthquakeDic))
print()


#Part 2
eq_dict = {}

for Earthquake in EarthquakeDic:
    if Earthquake["properties"]["mag"] > 6:
        location = Earthquake["properties"]["place"]
        magnitude = Earthquake["properties"]["mag"]
        longitude = Earthquake["geometry"]["coordinates"][0]
        latitude = Earthquake["geometry"]["coordinates"][1]
        eq_dict[location] = {"Magnitude": magnitude, "Longitude": longitude, "Latitude": latitude}
print(eq_dict)
print()


#Part 3      
for metrics in eq_dict:
    print("Location:", metrics)
    print("Magnitude:", eq_dict[metrics]["Magnitude"])
    print("Longitude:", eq_dict[metrics]["Longitude"])
    print("Latitude:", eq_dict[metrics]["Latitude"])
    print()