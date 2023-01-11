'''Module to define the classes that represent the objects containing the data.
'''

class Station:
    '''Class to represent a station.
    '''
    
    def __init__(self, name, id, name_short=None, lat=None, lon=None, id_region=None):
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
        :param id_region: ID of the region of the station, defaults to None
        :type id_region: int, optional
        '''
        self.name = name
        self.id = id
        self.name_short = name_short
        self.lat = lat
        self.lon = lon
        self.id_region = id_region

    def __str__(self):
        return (
            f'Name: {self.name}\n'
            f'Short name: {self.name_short}\n'
            f'ID: {self.id}\n'
            f'Latitude: {self.lat}\n'
            f'Longitude: {self.lon}\n'
            f'ID region: {self.id_region}'
        )


class Train:
    '''Class to represent a train.
    '''

class Journey:
    '''Class to represent a journey.
    '''