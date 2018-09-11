#!/usr/bin/env python3
 
import json
import calendar
import datetime

import urllib
 
import pybikes
import re
 
global station_regxes
station_regexes = ['rescent / Ren' ,'Hutchison / Sherbrooke','ity Counc']
 
def getBikeData():
    bixi = pybikes.get('bixi-montreal')
    bixi.update()
    return bixi
 
def stationSearch(regex,data):
    stations = data.stations
    for station in stations:
        if re.search(regex,station.name) is not None:
            id = station.extra['uid']
            #renting = station.extra['renting']
            #returning = station.extra['returning']
            name = station.name.replace(" ","\\ ")
            bikes = station.bikes
            free = station.free
            latitude = station.latitude
            longitude = station.longitude
            ts = calendar.timegm(station.timestamp.timetuple())
            #astr = ''.join((name,' ',str(bikes),'/',str(free))).encode('utf-8')
            astr = ''.join(('Bixi,','Station=',name,',Longitude=',str(longitude),',Latitude=',str(latitude),' Bikes=',str(bikes),',Free_Docks=',str(free),',Total_Docks=',str(bikes+free),' ',str(ts),             '000000000'))
            print astr

 
def allStations(data):
    stations = data.stations
    for station in stations:
        id = station.extra['uid']
        #renting = station.extra['renting']
        #returning = station.extra['returning']
        name = station.name
        bikes = station.bikes
        free = station.free
        latitude = station.latitude
        longitude = station.longitude
        ts = calendar.timegm(station.timestamp.timetuple())
        #astr = ''.join((name,' ',str(bikes),'/',str(free))).encode('utf-8')
        astr = ''.join(('Bixi ','Station=\"',name,'\",Longitude=',str(longitude),',Latitude=',str(latitude),' Bikes=',str(bikes),',Free_Docks=',str(free),',Total_Docks=',str(bikes+free),' ',str(ts),             '000000000'))
        print astr
 
 
def print_bikes():
    bikes = getBikeData()
    for regex in station_regexes:
        stationSearch(regex,bikes)
 
 
bikes = getBikeData()
#allStations(bikes)
stationSearch('rescent / Ren',bikes)

