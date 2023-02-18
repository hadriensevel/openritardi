"""Run tests for viaggiatreno on the package openritardi.api.
"""

import pytest
from openritardi.api.providers import Viaggiatreno
from openritardi.api.exceptions import ErrorResponse, VoidResponse


viaggiatreno = Viaggiatreno()


def test_send_request():
    """Test the function send_request
    """

    request_data = viaggiatreno.API_ENDPOINTS['autocomplete_station'] + '/milano'
    request_error = viaggiatreno.API_ENDPOINTS['station_details'] + '/S017000000'
    request_void = viaggiatreno.API_ENDPOINTS['autocomplete_station'] + '/milanooooooooooo'

    # Test a request that returns data
    response = viaggiatreno.send_request(request_data)
    assert response

    # Test a request that returns an empty response
    with pytest.raises(VoidResponse):
        viaggiatreno.send_request(request_void)

    # Test a request that returns an error
    with pytest.raises(ErrorResponse):
        viaggiatreno.send_request(request_error)


def test_get_stations_region():
    """Test the function get_stations_region
    """

    # Test a request that returns data
    stations = viaggiatreno.get_stations_region(1)
    assert stations

    # Test a request that returns an empty response
    with pytest.raises(VoidResponse):
        viaggiatreno.get_stations_region(1111111)

    # Test a request that returns an error
    with pytest.raises(ErrorResponse):
        viaggiatreno.get_stations_region('string argument')


def test_autocomplete_station():
    """Test the function autocomplete_station
    """

    # Test a request that returns data
    stations = viaggiatreno.autocomplete_station('milano')
    assert stations

    # Test a request that returns an empty response
    with pytest.raises(VoidResponse):
        viaggiatreno.autocomplete_station('milanoooooooooo')

    # Test a request that returns an error
    with pytest.raises(ErrorResponse):
        viaggiatreno.autocomplete_station('')


def test_get_region_station():
    """Test the function get_region_station
    """

    # Test a request that returns data
    stations = viaggiatreno.get_region_station('S01700')
    assert stations

    # Test a request that returns an error
    with pytest.raises(ErrorResponse):
        viaggiatreno.get_region_station('')
