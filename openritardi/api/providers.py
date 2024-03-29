"""API providers to get the data from.
"""

import json
import requests

from .data_objects import Station, Train, Stop
from .exceptions import VoidResponse, ErrorResponse


class Viaggiatreno:
    """Viaggiatreno API
    """

    BASE_URL = 'http://www.viaggiatreno.it/infomobilita/resteasy/viaggiatreno/'
    API_ENDPOINTS = {
        'stations_list': 'elencoStazioni',
        'autocomplete_station': 'cercaStazione',
        'autocomplete_train_number': 'cercaNumeroTrenoTrenoAutocomplete',
        'region_station': 'regione',
        'station_details': 'dettaglioStazione',
        'train_stops': 'tratteCanvas',
        'train_details': 'andamentoTreno'
    }

    def __init__(self):
        pass

    def send_request(self, end_point: str) -> str:
        """Send a request to the API.

        Args:
            end_point (str): end point of the request

        Raises:
            VoidResponse: void response from viaggiatreno
            ErrorResponse: error response from viaggiatreno

        Returns:
            str: response of the request
        """

        # Send the request
        response = requests.get(self.BASE_URL + end_point, timeout=10)

        # Check if the response is void
        if response.text == '' or response.text == '[]':
            raise VoidResponse('the response from viaggiatreno is void')

        # Check if the response is an error
        if response.status_code != 200 or response.text == 'Error':
            raise ErrorResponse('viaggiatreno returned an error')

        # Return the response
        return response.text

    def get_stations_region(self, id_region: int) -> list[Station]:
        """Get the list of stations in a region.

        Args:
            id_region (int): ID of the region

        Returns:
            list[Station]: list of Station objects
        """

        # Get the data from the API
        response = self.send_request(self.API_ENDPOINTS['stations_list'] + '/' + str(id_region))
        data_json = json.loads(response)

        # Create a list of Station objects from the response of the request
        stations = []
        for station in data_json:
            stations.append(Station(name=station['localita']['nomeLungo'],
                                    name_short=station['localita']['nomeBreve'],
                                    station_id=station['codiceStazione'],
                                    lat=station['lat'],
                                    lon=station['lon'],
                                    id_region=station['codReg']))

        return stations

    def autocomplete_station(self, query: str) -> list[Station]:
        """Autocomplete a station name.
        It returns a list of stations (name, short name and ID) that match the query.

        Args:
            query (str): query to search

        Returns:
            list[Station]: list of Station objects
        """

        # Get the data from the API
        response = self.send_request(self.API_ENDPOINTS['autocomplete_station'] + '/' + query)
        data_json = json.loads(response)

        # Create a list of Station objects from the response of the request
        stations = []
        for station in data_json:
            stations.append(Station(name=station['nomeLungo'],
                                    name_short=station['nomeBreve'],
                                    station_id=station['id']))

        return stations

    def get_region_station(self, id_station: str) -> int:
        """Get the region ID of a station.

        Args:
            id_station (str): ID of the station

        Returns:
            int: ID of the region
        """

        # Get the data from the API
        response = self.send_request(self.API_ENDPOINTS['region_station'] + '/' + id_station)
        return int(response)

    def get_station_details(self, id_station: str) -> Station:
        """Create a Station object with its details.

        Args:
            id_station (str): ID of the station

        Returns:
            Station: Station object
        """

        # Get the ID of the region of the station
        id_region = self.get_region_station(id_station)

        # Get the data from the API
        response = self.send_request(self.API_ENDPOINTS['station_details'] +
                                     '/' + id_station + '/' + str(id_region))
        data_json = json.loads(response)

        # Create a Station object
        station = Station(name=data_json['localita']['nomeLungo'],
                          name_short=data_json['localita']['nomeBreve'],
                          station_id=data_json['codiceStazione'],
                          lat=data_json['lat'],
                          lon=data_json['lon'],
                          id_region=data_json['codReg'])

        return station

    def autocomplete_train_number(self, query: int) -> list[Train]:
        """Autocomplete a train number.
        It returns a list of trains (number, origin ID and departure time) that match the query.

        Args:
            query (int): query to search

        Returns:
            list[Train]: list of Train objects
        """

        # Get the data from the API
        # The data that we get is text, not JSON
        response = self.send_request(self.API_ENDPOINTS['autocomplete_train_number'] + '/' + str(query))
        data_txt = response

        # Loop on every line of the response test to create
        # and object and add it to the list
        trains = []
        for train in data_txt.splitlines():

            # Example of a line: 41 - DOMODOSSOLA|41-S01003-1673391600000
            # Drop everything before | and split the rest
            train = train.split('|')[1].split('-')

            # Create a Train object and add it to the list
            trains.append(Train(number=int(train[0]),
                                origin_id=train[1],
                                departure_time=int(train[2])))

        return trains

    def get_train_stops(self, train: Train) -> Train:
        """Get the stops of a train with realtime data.

        Args:
            train (Train): Train object

        Returns:
            Train: initial Train object with the stops
        """

        # Get the data from the API
        response = self.send_request(self.API_ENDPOINTS['train_stops'] + '/' +
                                     train.origin_id + '/' + str(train.number) + '/' + str(train.departure_time))
        data_json = json.loads(response)

        # Loop on every stop and add it to the train object
        for stop in data_json:
            train.add_stop(Stop(name=stop['fermata']['stazione'],
                                station_id=stop['fermata']['id'],
                                arrival_time=stop['fermata']['arrivo_teorico'],
                                departure_time=stop['fermata']['partenza_teorica'],
                                delay_arrival=stop['fermata']['ritardoArrivo'],
                                delay_departure=stop['fermata']['ritardoPartenza']))
        return train

    def get_train_details(self, train: Train) -> Train:
        # TODO: finish function (choose which details to return)
        """Get the details of a train with realtime data.

        Args:
            train (Train): Train object

        Returns:
            Train: initial Train object with the details
        """
        return train
