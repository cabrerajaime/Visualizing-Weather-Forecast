import requests

API_KEY = "773bab50db6da76c19c866dc34d52b43"


def get_data(place, forecast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}" \
          f"&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    elif kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":

    y = get_data(place="Taiwan", forecast_days=1, kind="Temperature")
    print(y[0:])
