'''Module to define the classes that represent the objects containing the data.
'''


class Station:
    '''Class to represent a station.
    '''

    def __init__(self, name, station_id, name_short=None, lat=None, lon=None, id_region=None):
        '''
        Args:
            name (str): name of the station
            station_id (str): ID of the station
            name_short (str, optional): short name of the station. Defaults to None.
            lat (int, optional): latitute of the station. Defaults to None.
            lon (int, optional): longitude of the station. Defaults to None.
            id_region (int, optional): ID of the region of the station. Defaults to None.
        '''
        self.name = name
        self.station_id = station_id
        self.name_short = name_short
        self.lat = lat
        self.lon = lon
        self.id_region = id_region

    def __str__(self):
        return (
            f'Name: {self.name}\n'
            f'Short name: {self.name_short}\n'
            f'ID: {self.station_id}\n'
            f'Latitude: {self.lat}\n'
            f'Longitude: {self.lon}\n'
            f'ID region: {self.id_region}'
        )


class Stop(Station):
    '''Class to represent a stop of a train.
    '''

    def __init__(self, name, station_id, name_short=None, lat=None, lon=None,
                 id_region=None, arrival_time=None, departure_time=None,
                 delay_arrival=None, delay_departure=None):
        '''
        Args:
            name (str): name of the station
            station_id (str): ID of the station
            name_short (str, optional): short name of the station. Defaults to None.
            lat (int, optional): latitute of the station. Defaults to None.
            lon (int, optional): longitude of the station. Defaults to None.
            id_region (int, optional): ID of the region of the station. Defaults to None.
            arrival_time (int, optional): arrival time. Defaults to None.
            departure_time (int, optional): departure time. Defaults to None.
            delay_arrival (int, optional): delay on arrival. Defaults to None.
            delay_departure (int, optional): delay on departure. Defaults to None.
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
        Args:
            number (int): train number
            origin_id (str): D of the station of origin
            departure_time (int): departure time
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
        )

    def add_stop(self, stop: Stop):
        '''Add a stop to the train

        Args:
            stop (Stop): stop to add
        '''
        self.stops.append(stop)


class Journey:
    '''Class to represent a journey.
    '''
