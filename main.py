import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox(label="Select data to view",
                      options=("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            temperatures_celsius = [temp/10 for temp in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures_celsius,
                             labels={"x": "Dates", "y": "Temperatures  °C"})
            st.plotly_chart(figure)
        elif option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_condition]
            # Create a sky condition image
            st.image(image_paths, width=116)
    except KeyError:
        st.warning("That place was not found. please write another",
                   icon="⚠️")
