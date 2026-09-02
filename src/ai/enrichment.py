import requests
from utils.helpers import EMAIL



import requests


def check_location(city_name: str) -> bool:
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{city_name}, South Africa",
        "format": "json",
        "addressdetails": 1,
        "limit": 5
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        
        # Catch any specific HTTP errors (like 406, 403, etc.)
        if response.status_code != 200:
            print(f"Failed to fetch data. HTTP Status: {response.status_code}")
            print(f"Server response snippet: {response.text[:200]}")
        else:
            return True

    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        return False


if __name__ == "__main__":
    pass
