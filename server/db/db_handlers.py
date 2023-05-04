import sqlite3
from datetime import datetime
from typing import Dict


def insert_unknown_exception(device_id: int) -> None:
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    cursor.execute(f'''
        insert into exceptions (datetime, device_id, message, description)
        values (
            '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', 
            {device_id}, 
            'UNKNOWN ERROR', 
            NULL
        );
    ''')

    connection.commit()
    cursor.close()
    connection.close()


def insert_device_exception(device_id: int, sensor: str) -> None:
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    cursor.execute(f'''
        insert into exceptions (datetime, device_id, message, description)
        values (
            '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', 
            {device_id}, 
            'ERROR: no data from {sensor} sensor', 
            'Check the device'
        );
    ''')

    connection.commit()
    cursor.close()
    connection.close()


def insert_weather_info(weather_info: Dict[str, str]) -> None:
    connection = sqlite3.connect('db/data.db')
    cursor = connection.cursor()

    query = f'''
        insert into weather_info (
            device_id, device_point, global_latitude, global_longitude, 
            temperature, pressure, humidity, cloudness, wind_speed, wind_dir, datetime
        )
        values (
            {weather_info['device_id']},
            '{weather_info['point']}',
            {weather_info['global_latitude']},
            {weather_info['global_longitude']},
            {weather_info['temperature']},
            {weather_info['pressure']},
            {weather_info['humidity']},
            {weather_info['cloudness']},
            {weather_info['wind_speed']},
            '{weather_info['wind_dir']}',
            '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}'
        );
    '''

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
