import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    """Fetch animal data from the API Ninjas animals API.

    Args:
        animal_name: The name of the animal to search for.

    Returns:
        A list of animal data dictionaries, or None if the request fails.
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    try:
        response = requests.get(
            api_url,
            headers={'X-Api-Key': API_KEY},
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again later.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch data. {e}")
        return None

#print(fetch_data("fish"))



