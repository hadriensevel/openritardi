'''API providers to get the data from.
'''

import json
import requests

from .data_objects import Station

class Viaggiatreno:
    '''Viaggiatreno API
    '''

    BASE_URL = 'http://www.viaggiatreno.it/infomobilita/resteasy/viaggiatreno/'
    API_ENDPOINTS = {
        'stations_list': 'elencoStazioni',
        'autocomplete_station': 'cercaStazione',
        'autocomplete_train_number': 'cercaNumeroTreno',
        'region_station': 'regione',
        'station_details': 'dettaglioStazione'
    }

    def __init__(self):
        pass

    def get_stations_region(self, id_region: int) -> list[Station]:
        '''Get the list of stations in a region.

        :param id_region: ID of the region
        :type id_region: int
        :return: list of Station objects
        :rtype: list[Station]
        '''

        # Get the data from the API
        response = requests.get(self.BASE_URL + self.API_ENDPOINTS['stations_list'] + '/' + str(id_region))
        data_json = json.loads(response.text)

        # Create a list of Station objects from the response of the request
        stations = []
        for station in data_json:
            stations.append(Station(name=station['localita']['nomeLungo'],
                                    name_short=station['localita']['nomeBreve'],
                                    id=station['codiceStazione'],
                                    lat=station['lat'],
                                    lon=station['lon'],
                                    id_region=station['codReg']))

        return stations

    def autocomplete_station(self, query: str) -> list[Station]:
        '''Autocomplete a station name.
        It returns a list of stations (name, short name and ID) that match the query.

        :param query: query to search
        :type query: str
        :return: list of Station objects
        :rtype: list[Station]
        '''

        # Get the data from the API
        response = requests.get(self.BASE_URL + self.API_ENDPOINTS['autocomplete_station'] + '/' + query)
        data_json = json.loads(response.text)

        # Create a list of Station objects from the response of the request
        stations = []
        for station in data_json:
            stations.append(Station(name=station['nomeLungo'],
                                    name_short=station['nomeBreve'],
                                    id=station['id']))

        return stations

    def get_region_station(self, id_station: str) -> int:
        '''Get the region ID of a station.

        :param id_station: ID of the station
        :type id_station: str
        :return: ID of the region
        :rtype: int
        '''

        # Get the data from the API
        response = requests.get(self.BASE_URL + self.API_ENDPOINTS['region_station'] + '/' + id_station)
        return int(response.text)
        
    def get_station_details(self, id_station: str) -> Station:
        '''Create a Station object with its details.

        :param id_station: _description_
        :type id_station: str
        :return: _description_
        :rtype: Station
        '''

        # Get the ID of the region of the station
        id_region = self.get_region_station(id_station)

        # Get the data from the API
        response = requests.get(self.BASE_URL + self.API_ENDPOINTS['station_details'] + '/' + id_station + '/' + str(id_region))
        data_json = json.loads(response.text)

        # Create a Station object
        station = Station(  name=data_json['localita']['nomeLungo'],
                            name_short=data_json['localita']['nomeBreve'],
                            id=data_json['codiceStazione'],
                            lat=data_json['lat'],
                            lon=data_json['lon'],
                            id_region=data_json['codReg'])

        return station