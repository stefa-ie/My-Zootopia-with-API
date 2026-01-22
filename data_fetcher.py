import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
  api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
  response = requests.get(api_url, headers={'X-Api-Key': f"{API_KEY}"})

  data = response.json()
  return data

#print(fetch_data("fish"))



