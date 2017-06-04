# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:21:17 2016

@author: elbagomeznavas
"""
# For uploading polygon (delhi) layer
layer = iface.addVectorLayer("/Users/elbagomeznavas/Desktop/Delhi_Distance/Delhi_projected.shp", "Delhi_projected.shp", "ogr")
if not layer:
  print "Layer failed to load!"
  
# For uploading centroid layer
layer = iface.addVectorLayer("/Users/elbagomeznavas/Desktop/Delhi_Distance/Delhi_Proj_Centroid.shp", "Delhi_Proj_Centroid", "ogr")
if not layer:
  print "Layer failed to load!"

# Tutorial version of buffer
import processing
layer = iface.activeLayer()
processing.runalg("qgis:fixeddistancebuffer",layer.name(),29000,10,False,"/Users/elbagomeznavas/Desktop/temp_buffers/buffer_test.shp")
vlayer = QgsVectorLayer('/Users/elbagomeznavas/Desktop/temp_buffers/buffer_test.shp', "buffer", "ogr")
QgsMapLayerRegistry.instance().addMapLayer(vlayer)

#adding 50 km radius increments (for loop)
distances =[29000+50000]#, 29000+100000, 29000+150000,29000+200000, 29000+250000]
for distance in distances:
    import processing
    layer = iface.activeLayer()
    processing.runalg("qgis:fixeddistancebuffer",layer.name(),distance,10,False,"/Users/elbagomeznavas/Desktop/temp_buffers/buffer_test_ring.shp")
    vlayer = QgsVectorLayer('/Users/elbagomeznavas/Desktop/temp_buffers/buffer_test_ring.shp', "buffer", "ogr")
    QgsMapLayerRegistry.instance().addMapLayer(vlayer)

#counting the p.m. 2.5 within each buffer (not working yet)
import processing
layer = iface.activeLayer()
Result = "/Users/elbagomeznavas/Desktop/temp_buffers/points_in_buffer_1.shp"
processing.runalg("qgis:countpointsinpolygon", layer.name(), "/Users/elbagomeznavas/Desktop/P.M.2.5_all/pm2.5_all.shp", 'NUMPOINTS', Result)
vlayer = QgsVectorLayer("/Users/elbagomeznavas/Desktop/temp_buffers/points_in_buffer_1.shp", "points_in_buffer_1", "ogr")
QgsMapLayerRegistry.instance().addMapLayer(vlayer)
    

#begin main code structure

cityList=['asdf','asdf3','asdf4']
DISTANCE_LIST=[5,6,7]


def main():
    cityID_list=cityList[0:5] # when ready to do whole thing, remove [0:5]
    
    final_output=[]
    
    for aCity in cityID_list: #loops through all the cities
        city=getCity(aCity,'afilepath') #returns the city information given the ID and the file path
        startDistance=DISTANCE_LIST[cityList.index(aCity)]
        distanceList=createDistanceList(startDistance)
        
        p2m_vector=[] #initializes p2m list to empty
        for distance in distanceList: #loop thorugh all the cirlces
            city_buffer=createBuffer(city,distance)
            p2m=getP2M(city_buffer)
            p2m_vector.append(p2m) #adds the p2m to the p2m list
        
        output=(aCity,p2m_vector)
        final_output.append(output)        
    return final_output
        
        
        
def getCity(cityID,filePath):
    '''this function gets the required city information from the file and loads it in a ready to use format'''
    return 5 #need the name
    


def createDistanceList(startDistance):
    '''simple function that takes the an initial distance and creates a list with NUM_CIRCLE elements with an increasing radius of CIRLCE_DIST'''
    i=1
    distList=[startDistance]
    while i< NUM_CIRCLES:
        dist=i*CIRCLE_DIST + startDistance
        distList.append(dist)
        i=i+1
    return distList
    
    
def createBuffer(city,distance):
    '''creates a buffer for the given city and the given distance and then retuns that buffer'''
    return 5
    
def getP2M(city_buffer):
    '''takes a city buffer and returns the p2m inside the circle. Must return it as an float'''
    return 5
    
    
    
result=main()
print(result)
