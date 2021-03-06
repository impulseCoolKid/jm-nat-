# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
        

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):     #for task 1F by Nathan
    #checks the typical high/low range data for consistency
        
        if self.typical_range == None:
            #checks if data is unavailable
            return False
        else:
            if  self.typical_range[0] > self.typical_range[1]:
                #checks if the reported typical low range is greater than the high one
                return False
            else:
                return True

    def relative_water_level(self): # task 2B by james mcallister

        #quick calcs with useful data
        if self.latest_level == None or self.typical_range == None: #checks data is valed
            return None
        else: 
            bottom, top = self.typical_range
            quickMath = (self.latest_level - bottom)/(top - bottom)
            return quickMath




def inconsistent_typical_range_stations(stations):      #also for task 1F by Nathan
    #given a list of stations, returns a list of those stations which have inconsistent data
    
    InconsistentStations = []
    
    #checks which stations have inconsistent data and adds them to the list
    for station in stations:
        if station.typical_range_consistent() == False:
            InconsistentStations.append(station)
    return InconsistentStations