import os
import requests
from urllib.parse import urlencode

from config import ya_api_key, ya_api_url


class Device:
    def __init__(self):
        print(os.environ)
        self.point = os.environ.get('point', '0,0')
        self.device_id = os.environ.get('device_id', '0')
        self.global_longitude = float(os.environ.get('longitude', '37.738279'))
        self.global_latitude = float(os.environ.get('latitude', '55.812170'))

    async def get_weather_info(self):
        request_params = {
            'lat': self.global_latitude,
            'lon': self.global_longitude,
            'lang': 'ru_RU',
            'limit': 1
        }

        request_headers = {
            'X-Yandex-API-Key': ya_api_key
        }

        weather_info = {
            'device_id': int(self.device_id),
            'point': self.point,
            'global_latitude': float(self.global_latitude),
            'global_longitude': float(self.global_longitude),
            'temperature': None,
            'pressure': None,
            'humidity': None,
            'cloudness': None,
            'wind_speed': None,
            'wind_dir': None
        }

        print(ya_api_url + '?' + urlencode(request_params))
        try:
            response = requests.get(
                url=ya_api_url + '?' + urlencode(request_params),
                headers=request_headers
            )

            if response.status_code == 200:
                data = response.json().get('fact', None)
                if data is not None:
                    weather_info = {
                        'device_id': int(self.device_id),
                        'point': self.point,
                        'global_latitude': float(self.global_latitude),
                        'global_longitude': float(self.global_longitude),
                        'temperature': data.get('temp', None),
                        'pressure': data.get('pressure_mm', None),
                        'humidity': data.get('humidity', None),
                        'cloudness': data.get('cloudness', None),
                        'wind_speed': data.get('wind_speed', None),
                        'wind_dir': data.get('wind_dir', None)
                    }

        except requests.RequestException as error:
            from log import log
            log.exception('message')
            log.error(error)

        return weather_info
