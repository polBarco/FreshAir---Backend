import http.client
import json
import ssl

class AirQualityService:

    @staticmethod
    async def get_air_quality(city: str, token: str):
        try:
            conn = http.client.HTTPSConnection("api.waqi.info", context = ssl._create_unverified_context())
            url = f"/feed/{city}/?token={token}"
            conn.request("GET", url)
            response = conn.getresponse()
            if response.status != 200:
                raise Exception('City not found')
            data = response.read()
            conn.close()
            return json.loads(data)
        except Exception:
            raise Exception('City not found')