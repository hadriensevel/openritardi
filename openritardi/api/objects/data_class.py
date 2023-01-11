'''Module to define the classes that represent the objects containing the data.
'''

class Station:
    '''Class to represent a station.
    '''
    
    def __init__(self, name, id, lat, lon):
        '''
        :param name: Name of the station
        :type name: string
        :param id: ID of the station
        :type id: string
        :param lat: Latitude of the station
        :type lat: integer
        :param lon: Longitude of the station
        :type lon: integer
        '''

        self.name = name
        self.id = id
        self.lat = lat
        self.lon = lon

class Train:
    '''Class to represent a train.
    '''