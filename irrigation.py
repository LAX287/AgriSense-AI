import requests

API_KEY = "8ced76fa35b112114402b5d041f8a526"

def irrigation_advice(city):

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

        response = requests.get(url)

        data = response.json()

        if "main" not in data:
            return f"API Error: {data}"

        humidity = data["main"]["humidity"]
        temperature = round(data["main"]["temp"] - 273.15, 1)

        if humidity > 80:
            advice = "No irrigation required."

        elif humidity > 60:
            advice = "Light irrigation recommended."

        else:
            advice = "Irrigation recommended."

        return (
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"{advice}"
        )

    except Exception as e:
        return f"Error: {str(e)}"