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
                                    lon=station['lon']))

        return stations

    def autocomplete_station(self, query: str) -> list[Station]:
        '''Autocomplete a station name.

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
        pass