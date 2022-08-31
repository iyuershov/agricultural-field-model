import requests
from typing import Dict
from multiprocessing.pool import ThreadPool
from config import devices
from db.db_handlers import insert_unknown_exception, insert_device_exception, insert_weather_info


weather_params = ['temperature', 'pressure', 'humidity', 'cloudness', 'wind_speed', 'wind_dir']


def get_device_data(device: Dict[str, str]) -> Dict[int, Dict[str, str]]:
    device_data = None

    try:
        response = requests.get(device['url'])
        device_data = response.json()
    except requests.RequestException as error:
        print(error)

    return {
        'device_id': int(device['device_id']),
        'data': device_data
    }


def main() -> None:
    threads_number = 4
    if len(devices) < threads_number:
        threads_number = len(devices)

    pool = ThreadPool(processes=threads_number)
    results = []
    for device in devices:
        results.append(
            pool.apply_async(get_device_data, args=[device])
        )
    pool.close()
    pool.join()
    results = [result.get() for result in results]

    for device_weather_data in results:
        if device_weather_data['data'] is None:
            insert_unknown_exception(device_weather_data['device_id'])
            continue

        for weather_param in weather_params:
            if device_weather_data['data'].get(weather_param, None) is None:
                insert_device_exception(device_weather_data['device_id'], weather_param)

        insert_weather_info(device_weather_data['data'])


if __name__ == '__main__':
    main()
