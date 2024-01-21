import gmplot
import webbrowser
import os
  
def drawmap(Array):
    latitude_list = [31.580143741283408]
    longitude_list = [74.3562217369892]
    address=["Address"]
    for i in range(len(Array)):
        latitude_list.append(float(Array[i][0]))
        longitude_list.append(float(Array[i][1]))
        address.append(Array[i][2])
        # print(latitude_list)

    
    gmap3 = gmplot.GoogleMapPlotter(31.580143741283408,
                                    74.3562217369892, 13)
    gmap3.apikey = "AIzaSyCFE8e8PiPP_3u2-mT-WtZUb6WlPAdShKc"
    # gmap3,apikey = "AIzaSyAGthscLPBDQLi9-kq9vxi4I0qrxDO9Pbw"mine
    gmap3.scatter( latitude_list, longitude_list, 'blue',
                                size = 100, marker = True )
    # gmap3.marker( latitude_list, longitude_list,label="abc")
    gmap3.plot(latitude_list, longitude_list, 
            'cornflowerblue', edge_width = 2.5)
    
    gmap3.draw( "map.html" )
    filename = 'file:///'+os.getcwd()+'/' + 'map.html'
    webbrowser.open_new_tab(filename)

# drawmap()