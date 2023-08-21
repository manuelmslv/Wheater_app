from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
#Define tu API Key de OpenWeatherMap https://home.openweathermap.org/users/sign_up una vez registrado podras acceder a la tuya
API_KEY = 'xxxx_xxxxx_xxxx_xxxx'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    
    if data['cod'] == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return render_template('index.html', weather_data=weather_data)
    else:
        error_message = "City not found"
        return render_template('index.html', error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
