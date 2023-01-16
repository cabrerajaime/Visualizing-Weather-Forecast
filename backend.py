import requests

API_KEY = "773bab50db6da76c19c866dc34d52b43"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}" \
          f"&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":

    y = get_data(place="Taiwan", forecast_days=1)
    print(y[0:])
