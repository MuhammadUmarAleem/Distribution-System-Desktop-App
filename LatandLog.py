import folium
import webbrowser
import csv
import pandas as pd
from classes import MedicalStore,MedicalStoreNode
import os
# code
# api_key = 'AIzaSyBCYPbpfdfwPkm1iR54y6Zn--qETb_JDyQ'
# app = Nominatim(user_agent="test")
# address = "University of Engineering and Technology,Pakistan"
# location = app.geocode(address).raw
# lat = location['lat']
# lng = location['lon']
medicalstores = MedicalStore()
def readmedicalStore():
    try:
            with open("MedicalStore.csv", 'r') as file:
                    csvreader = csv.reader(file)
                    for row in csvreader:
                            if (row[0] != 'StoreName'):
                                    data = MedicalStoreNode(row[3], row[4], row[0],
                                                            row[1], row[2])
                                    data.bill = row[5]
                                    medicalstores.addMedicalStore(data)
    except:
            print("MedicalStore.csv")

readmedicalStore()
name = []
lat = []
log = []
s = medicalstores.head
while s != None:
    name.append(s.mName)
    lat.append(s.lattitude)
    log.append(s.longitude)
    s = s.next
df_counters = pd.DataFrame(
    {
     'Name' : name,
     'latitude' : lat,
     'longitude' : log
    })
df_counters.head()
locations = df_counters[['latitude', 'longitude']]
locationlist = locations.values.tolist()
mymap = folium.Map(location=[medicalstores.head.lattitude,medicalstores.head.longitude] , zoom_start = 15)
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=df_counters['Name'][point]).add_to(mymap)
# folium.Marker([s.lattitude,s.longitude],popup=location).add_to(mymap)
mymap.save('mylocation.html')
filename = 'file:///'+os.getcwd()+'/' + 'mylocation.html'
webbrowser.open_new_tab(filename)