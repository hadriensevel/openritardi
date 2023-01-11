'''Module to define the classes that represent the objects containing the data.
'''

class Station:
    '''Class to represent a station.
    '''
    
    def __init__(self, name, id, lat, lon, name_short=None):
        '''
        :param name: Name of the station
        :type name: str
        :param id: ID of the station
        :type id: str
        :param lat: Latitude of the station
        :type lat: int
        :param lon: Longitude of the station
        :type lon: int
        '''

        self.name = name
        self.id = id
        self.lat = lat
        self.lon = lon
        self.name_short = name_short

class Train:
    '''Class to represent a train.
    '''