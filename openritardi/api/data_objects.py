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


class Stop(Station):
    '''Class to represent a stop of a train.
    '''

    def __init__(self, name, id, name_short=None, lat=None, lon=None,
                 id_region=None, arrival_time=None, departure_time=None,
                 delay_arrival=None, delay_departure=None):
        '''_summary_

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
        :param arrival_time: arrival time, defaults to None
        :type arrival_time: int, optional
        :param departure_time: departure time, defaults to None
        :type departure_time: int, optional
        :param delay_arrival: delay on arrival, defaults to None
        :type delay_arrival: int, optional
        :param delay_departure: delay on departure, defaults to None
        :type delay_departure: int, optional
        '''
        super().__init__(name, id, name_short, lat, lon, id_region)
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.delay_arrival = delay_arrival
        self.delay_departure = delay_departure


class Train:
    '''Class to represent a train.
    '''

    def __init__(self, number, origin_id, departure_time):
        '''
        :param number: train number
        :type number: int
        :param origin_id: ID of the station of origin
        :type origin_id: str
        :param departure_time: departure time
        :type departure_time: int
        '''
        self.number = number
        self.origin_id = origin_id
        self.departure_time = departure_time
        self.stops = []

    def __str__(self):
        return(
            f'Number: {self.number}\n'
            f'Origin ID: {self.origin_id}\n'
            f'Departure time: {self.departure_time}\n'
            f'Destination ID: {self.destination_id}'
        )

    def add_stop(self, stop: Stop):
        '''Add a stop to the train.

        :param stop: Stop object
        :type stop: Stop
        '''
        self.stops.append(stop)


class Journey:
    '''Class to represent a journey.
    '''
