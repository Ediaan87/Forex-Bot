import requests
import pandas as pd

def collect_data():
    response = requests.get("your_data_source_url")
    data = pd.DataFrame(response.json())
    return data