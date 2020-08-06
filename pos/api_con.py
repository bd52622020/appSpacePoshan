import requests
import con
class ApiCon:
    def get_api(self):
        headers = {
            'App-Id': 'd5313144',
            'App-Key': '19c56a17e5c95840e79c2681089be16c'
        }
        api_url = requests.get(con.API_URL, headers=headers)

        if api_url.ok:
            json_array = api_url.json()
            filtered_data = json_array
            return filtered_data

        else:
            return False
