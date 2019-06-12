import datetime
import json
import threading
import time
from logging import getLogger

import requests
from urllib.parse import urlencode, urljoin

from IoT_Serwer.models import CurrentStateData


class WeatherData:
    def __init__(self, timestamp, temperature, cloudiness) -> None:
        self.reading_datetime = datetime.datetime.utcfromtimestamp(timestamp)
        self.temperature = temperature
        self.cloudiness = cloudiness

    def __repr__(self) -> str:
        data_dict = {
            'temperature': self.temperature,
            'cloudiness': self.cloudiness,
            'weather_reading_date_utc': self.reading_datetime
        }
        return json.dumps(data_dict)

    @classmethod
    def from_json(cls, api_json):
        main_data = api_json['main']
        cloud_data = api_json['clouds']
        return WeatherData(
            api_json['dt'],
            main_data['temp'],
            cloud_data['all']
        )


class ApiConnectionError(Exception):

    def __init__(self, reason, status_code):
        super().__init__(reason)
        self.reason = reason
        self.status_code = status_code


class WeatherApiApp:
    POOLING_INTERVAL_SECONDS = 60
    RETRY_INTERVAL_SECONDS = 10
    API_SECRETS = None
    logger = getLogger()
    BASE_API_URL = "http://api.openweathermap.org/data/2.5/weather?"
    QUERY_PARAMS = {
        "id": 3081368,
        "appid": None,
        "units": 'metric'
    }

    @classmethod
    def start(cls):
        cls.API_SECRETS = cls.get_secrets()
        cls.QUERY_PARAMS['appid'] = cls.API_SECRETS['weather_api_key']
        pooling_thread = threading.Thread(target=cls.pool_api, args=(WeatherApiApp.POOLING_INTERVAL_SECONDS,))
        pooling_thread.start()

    @classmethod
    def get_secrets(cls):
        secrets = {}
        with open('api_keys.secret', 'r') as file:
            for line in file:
                key, value = line.split('=')
                secrets[key] = value

        return secrets

    @classmethod
    def pool_api(cls, interval):
        retry_counter = 0
        while True:
            try:
                json_data = cls.fetch_data()
                weather_data = WeatherData.from_json(json_data)
                cls.update_model(weather_data)
                time.sleep(interval)
                cls.logger.info("Updated model with api data")
                retry_counter = 0
            except ApiConnectionError as ex:
                retry_counter += 1
                cls.logger.error(
                    f"""Weather API call failed with status code {ex.status_code} and retry counter: {retry_counter}, 
                             will try again after {WeatherApiApp.RETRY_INTERVAL_SECONDS} seconds""")
                time.sleep(WeatherApiApp.RETRY_INTERVAL_SECONDS)

    @classmethod
    def fetch_data(cls):
        url_query = urlencode(query=cls.QUERY_PARAMS)
        final_url = urljoin(cls.BASE_API_URL, '?' + url_query)
        cls.logger.debug(f"Calling API at URL : {final_url}")
        response = requests.get(final_url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ApiConnectionError("Error", response.status_code)

    @classmethod
    def update_model(cls, weather_data: [WeatherData, dict]):
        state_data = CurrentStateData.objects.get(pk=1)
        state_data.temperature = weather_data.temperature
        state_data.cloudiness = weather_data.cloudiness
        state_data.weather_reading_date_utc = weather_data.reading_datetime
        state_data.save()
