import uvicorn
from fastapi import FastAPI
from device import Device

device = Device()
app = FastAPI()


@app.get('/weather_info')
async def get_weather_info():
    data = await device.get_weather_info()
    return data


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
