'''Module to define the classes that represent the objects containing the data.
'''

class Station:
    '''Class to represent a station.
    '''
    
    def __init__(self, name, id, name_short=None, lat=None, lon=None):
        '''
        :param name: name of the station
        :type name: str
        :param id: ID of the station
        :type id: str
        :param name_short: short name of the station, defaults to None
        :type name_short: str, optional
        :param lat: latitute of the station, defaults to None
        :type lat: int, optional
        :param lon: longitude of the station, defaults to None
        :type lon: int, optional
        '''

        self.name = name
        self.id = id
        self.name_short = name_short
        self.lat = lat
        self.lon = lon

class Train:
    '''Class to represent a train.
    '''