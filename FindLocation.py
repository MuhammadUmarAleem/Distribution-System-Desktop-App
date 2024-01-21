import phonenumbers
import opencage
import folium
import webbrowser
import os
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder
from phonenumbers import carrier


pepnumber = phonenumbers.parse("+923334875857")
location = geocoder.description_for_number(pepnumber,'en')
print(location)

print(carrier.name_for_number(pepnumber, "en"))

key = '9556c6a1c7684680bc22e93b73e4211c'
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

mymap = folium.Map(location=[lat,lng] , zoom_start = 15)
folium.Marker([lat,lng],popup=location).add_to(mymap)

mymap.save('mylocation.html')
filename = 'file:///'+os.getcwd()+'/' + 'mylocation.html'
webbrowser.open_new_tab(filename)