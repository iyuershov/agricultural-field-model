create table IF NOT EXISTS weather_info (
	device_id integer,
	device_point text,
	global_latitude real,
	global_longitude real,
	temperature integer,
	pressure integer,
	humidity integer,
	cloudness integer,
	wind_speed integer,
	wind_dir text,
	datetime text
);